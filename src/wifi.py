import network
from time import sleep
from src.config import get_config

config = get_config()
wlan = network.WLAN(network.STA_IF)

def connect_to_wifi(ssid = config['wifiName'], password = config['wifiPassword']):
    wlan.active(True)

    get_config()

    network.hostname(config['hostname'])
    wlan.connect(ssid, password)

    print("Connecting to WiFi...")
    while not wlan.isconnected():
        print(".")
        sleep(1)

    print("Connected to WiFi:", wlan.ifconfig()[0])
    print("Hostname:", network.hostname())

def get_wifi():
    return wlan.ifconfig()
