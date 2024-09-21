import network
from time import sleep
from src.config import load_config

config = load_config()
wlan = network.WLAN(network.STA_IF)

def connect_to_wifi(ssid = config['wifiName'], password = config['wifiPassword']):
    wlan.active(True)
    wlan.connect(ssid, password)

    print("Connecting to WiFi...")
    while not wlan.isconnected():
        print(".")
        sleep(1)

    print("Connected to WiFi:", wlan.ifconfig())

def get_wifi():
    return wlan.ifconfig()