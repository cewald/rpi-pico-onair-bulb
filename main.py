import uasyncio as asyncio
from src.wifi import connect_to_wifi
from src.server import start_server
from src.button import init_button


async def main():
    await connect_to_wifi()
    await asyncio.gather(start_server(), init_button())


asyncio.run(main())
