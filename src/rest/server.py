from src.microdot import Microdot
from machine import Pin
from src.config import getConfig

print('Init server')

app = Microdot()
config = getConfig()

led = Pin('LED', Pin.OUT)

def startServer():
    port = config['port']
    print('Start server on port:', port)
    app.run(port=port)

def returnResponse(success=True):
    return {'success': True, 'state': led.value()}

@app.route('/', methods=['GET'])
async def index(request):
    return returnResponse()

@app.route('/on', methods=['GET'])
async def on(request):
    led.on()
    return returnResponse()

@app.route('/off', methods=['GET'])
async def off(request):
    led.off()
    return returnResponse()


@app.route('/toggle', methods=['GET'])
async def toggle(request):
    led.toggle()
    return returnResponse()
