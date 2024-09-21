from src.microdot import Microdot
from src.config import getConfig

print('Init server')

app = Microdot()
config = getConfig()

def startServer():
    port = config['port']
    print('Start server on port:', port)
    app.run(port=port)

@app.route('/')
async def index(request):
    return 'Hello, world!'

