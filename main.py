from machine import Pin
from src.wifi import connect_to_wifi

# Add LED
pin = Pin("LED", Pin.OUT)
pin.on()

connect_to_wifi()

while True:
  pass
