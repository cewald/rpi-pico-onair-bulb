from time import sleep
from machine import Pin
from src.display import display
from src.led import led

button = Pin(4, Pin.IN, Pin.PULL_UP)
previous_value = button.value()


async def init_button():
    print("Init button")

    global previous_value
    while True:
        if button.value() == 0 and button.value() != previous_value:
            led.toggle()

            if led.value() == 0:
                display.clear()
            else:
                display.show_image()

        previous_value = button.value()
        sleep(0.1)
