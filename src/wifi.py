import network
from time import sleep
from src.config import getConfig

config = getConfig()
wlan = network.WLAN(network.STA_IF)


def connectToWifi(ssid=config["wifiName"], password=config["wifiPassword"]):
    wlan.active(True)

    network.hostname(config["hostname"])
    wlan.connect(ssid, password)

    print("Connecting to WiFi...")

    secondsWaited = 0
    while not wlan.isconnected():
        secondsWaited = secondsWaited + 1
        sleep(1)
        print("Try to connect: " + secondsWaited + "s")

    print("Connected to WiFi:", wlan.ifconfig()[0])
    print("Hostname:", network.hostname())


def getWifi():
    return wlan.ifconfig()
