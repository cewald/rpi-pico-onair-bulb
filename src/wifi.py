import network
from time import sleep
from src.config import getConfig

config = getConfig()
wlan = network.WLAN(network.STA_IF)

def connectToWifi(ssid = config['wifiName'], password = config['wifiPassword']):
    wlan.active(True)

    network.hostname(config['hostname'])
    wlan.connect(ssid, password)

    print("Connecting to WiFi...")
    while not wlan.isconnected():
        print(".")
        sleep(1)

    print("Connected to WiFi:", wlan.ifconfig()[0])
    print("Hostname:", network.hostname())

def getWifi():
    return wlan.ifconfig()
