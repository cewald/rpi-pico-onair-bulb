from asyncio import sleep
from machine import Pin
from src.display import display

button = Pin(6, Pin.IN, Pin.PULL_DOWN)
current_value = button.value()


async def init_button():
    print("Init button")

    global current_value
    while True:
        if button.value() != current_value:
            print("Button pressed:", button.value())
            current_value = button.value()
            if current_value == 1:
                display.show_image()
            else:
                display.clear()

        await sleep(0.1)
