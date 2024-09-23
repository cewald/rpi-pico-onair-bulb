import uasyncio as asyncio
from src.wifi import connect_to_wifi
from src.server import start_server
from src.button import init_button


async def main():
    await asyncio.gather(start_server(), init_button())


connect_to_wifi()
asyncio.run(main())
