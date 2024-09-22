from machine import Pin
from src.microdot import Microdot
from src.config import get_config
from src.display import display

print("Init server")

app = Microdot()
config = get_config()

led = Pin("LED", Pin.OUT)


def start_server():
    port = config["port"]
    print("Start server on port:", port)
    app.run(port=port, debug=True)


def returnResponse(success=True):
    return {"success": True, "state": led.value()}


@app.route("/", methods=["GET"])
async def index(request):
    return returnResponse()


@app.route("/on", methods=["GET"])
async def on(request):
    led.on()
    display.draw_bitmap()
    return returnResponse()


@app.route("/off", methods=["GET"])
async def off(request):
    led.off()
    display.clear()
    return returnResponse()


@app.route("/toggle", methods=["GET"])
async def toggle(request):
    led.toggle()

    if led.value() == 0:
        display.clear()
    else:
        display.draw_bitmap()

    return returnResponse()
