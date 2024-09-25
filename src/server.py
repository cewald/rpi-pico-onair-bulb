from lib.microdot import Microdot, Response
from src.config import get_config
from src.display import display
from src.led import led

print("Init server")

app = Microdot()
config = get_config()


async def start_server(debug=True):
    port = config["port"]
    await app.start_server(port=port, debug=debug)


def returnResponse(success=True):
    return {"success": True, "state": led.value()}


@app.get("/")
async def index(request):
    return returnResponse()


@app.get("/on")
async def on(request):
    led.on()
    display.show_image()
    return returnResponse()


@app.get("/on/<text>")
async def on_with_text(request, text):
    if not text:
        return Response.redirect("/on")

    led.on()
    display.show_text(text=text)
    return returnResponse()


@app.get("/off")
async def off(request):
    led.off()
    display.clear()
    return returnResponse()


@app.get("/toggle")
async def toggle(request):
    led.toggle()

    if led.value() == 0:
        display.clear()
    else:
        display.show_image()

    return returnResponse()


@app.get("/toggle/<text>")
async def toggle_with_text(request, text):
    if not text:
        return Response.redirect("/toggle")

    led.toggle()

    if led.value() == 0:
        display.clear()
    else:
        display.show_text(text=text)

    return returnResponse()
