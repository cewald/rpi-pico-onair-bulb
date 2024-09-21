import network
import usocket as socket
from time import sleep
from machine import Pin

# Add LED
pin = Pin("LED", Pin.OUT)

# Set up your Wi-Fi connection
ssid = 'YourSSID'
password = 'YourPassword'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
while not wlan.isconnected():
    sleep(1)

print('Connected to WiFi:', wlan.ifconfig())

# Workaround: Set the hostname (might need specific configuration or router support)
custom_hostname = 'my-pico-w'
addr_info = socket.getaddrinfo(custom_hostname, 80)

print(f"Hostname set to {custom_hostname} with address info:", addr_info)

pin.toggle()
