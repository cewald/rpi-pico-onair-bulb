import network
from asyncio import sleep
from src.config import get_config
from src.display import display

config = get_config()
wlan = network.WLAN(network.STA_IF)


async def show_text(text, showFor: float):
    display.show_text(text=text)
    await sleep(showFor)


async def connect_to_wifi(ssid=config["wifiName"], password=config["wifiPassword"]):
    wlan.active(True)

    network.hostname(config["hostname"])
    wlan.connect(ssid, password)

    max_wait = 20

    print("Connecting to WiFi")
    await show_text(text="wlcm", showFor=1)

    count = 0
    while not wlan.isconnected() and max_wait > 0:
        print(".", end="")

        count = count + 1 if count < 4 else 1
        text = ""
        for i in range(count):
            text = text + "."

        await show_text(text=text, showFor=1)
        max_wait -= 1

    if max_wait == 0:
        print("\nFailed to connect")
        display.show_text("fail")
        return

    print("\nConnected to WiFi:", wlan.ifconfig()[0])
    print("Hostname:", network.hostname())

    await show_text(text="cnct", showFor=0.8)
    await show_text(text="IP:" + wlan.ifconfig()[0], showFor=20)
    display.clear()


async def maintain_wifi():
    print("Add Wifi maintenance")
    if not wlan.isconnected():
        print("WiFi disconnected, attempting to reconnect...")
        wlan.disconnect()
        connect_to_wifi()


def get_wifi():
    return wlan.ifconfig()
