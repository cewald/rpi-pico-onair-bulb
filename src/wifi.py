import network
from time import sleep
from src.config import get_config
from src.display import display

config = get_config()
wlan = network.WLAN(network.STA_IF)


def connect_to_wifi(ssid=config["wifiName"], password=config["wifiPassword"]):
    wlan.active(True)

    network.hostname(config["hostname"])
    wlan.connect(ssid, password)

    max_wait = 20

    print("Connecting to WiFi")
    display.show_text("init")
    sleep(0.5)

    count = 0
    while not wlan.isconnected() and max_wait > 0:
        print(".", end="")

        count = count + 1 if count < 4 else 1
        text = ""
        for i in range(count):
            text = text + "."
        display.show_text(text)

        max_wait -= 1
        sleep(1)

    if max_wait == 0:
        print("\nFailed to connect")
        display.show_text("fail")
        return

    print("\nConnected to WiFi:", wlan.ifconfig()[0])
    print("Hostname:", network.hostname())

    display.show_text("cnct")
    sleep(0.8)
    display.clear()


def get_wifi():
    return wlan.ifconfig()
