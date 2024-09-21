import network
from time import sleep
from machine import Pin

# Add LED
pin = Pin("LED", Pin.OUT)

# Set up your Wi-Fi connection
ssid = 'Your Wifi name'
password = 'XXXXXXXX'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
print('Connecting to WiFi')
while not wlan.isconnected():
    sleep(1)
    print('.')

print('Connected to WiFi:', wlan.ifconfig())

pin.on()
