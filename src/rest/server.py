from machine import Pin
from src.microdot import Microdot
from src.config import getConfig
from src.display import showText, clear

print("Init server")

app = Microdot()
config = getConfig()

led = Pin("LED", Pin.OUT)


def startServer():
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
    showText(text="ONAIR")
    return returnResponse()


@app.route("/off", methods=["GET"])
async def off(request):
    led.off()
    clear()
    return returnResponse()


@app.route("/toggle", methods=["GET"])
async def toggle(request):
    led.toggle()

    if led.value() == 0:
        clear()
    else:
        showText(text="ONAIR")

    return returnResponse()
