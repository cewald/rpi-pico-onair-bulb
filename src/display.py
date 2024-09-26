from asyncio import create_task, sleep
from machine import Pin, SPI
from lib.max7219 import Matrix8x8
from src.image import image_one, image_zero


class Display(object):
    def __init__(self):
        print("Init display")

        self.text = ""
        self.matrix_count = 4
        self.spi = SPI(0, sck=Pin(2), mosi=Pin(3))
        self.cs = Pin(5, Pin.OUT)
        self.display = Matrix8x8(self.spi, self.cs, self.matrix_count)

        self.bounce_task = None
        self.blink_task = None

        self.display.brightness(0)
        self.display.fill(0)
        self.display.show()
        self.display.brightness(1)

    def stop_async_tasks(self):
        if self.bounce_task and not self.bounce_task.done():
            self.bounce_task.cancel()

        if self.blink_task and not self.blink_task.done():
            self.blink_task.cancel()

        self.blink_task = None
        self.bounce_task = None

    def show_text(self, text="PICO", delay=0.1):
        if self.text == text:
            return

        self.clear()
        self.text = text

        if len(text) > 4:
            self.bounce_task = create_task(self.bounce_text(text=text, delay=delay))
        else:
            self.display.text(text, 0, 0, 1)
            self.display.show()

    async def bounce_text(self, text, delay=0.1, end_wait=0.5):
        length = len(text) * 8
        max_offset = length - 32
        direction = 1
        pos = 0

        switch = False
        is_initialized = False

        while True:
            self.display.fill(0)
            self.display.text(text, -pos, 0, 1)
            self.display.show()

            await sleep(delay)

            if switch or not is_initialized:
                await sleep(end_wait)
                switch = False
                is_initialized = True

            pos += direction

            if pos >= max_offset or pos <= 0:
                direction *= -1
                switch = True

    def draw_image(self, image_byte_array=bytearray([])):
        for y in range(8):
            for x in range(self.matrix_count * 8):
                byte_index = (y * self.matrix_count) + (x // 8)
                byte = image_byte_array[byte_index]
                bit = (byte >> (7 - (x % 8))) & 1
                self.display.pixel(x, y, bit)

        self.display.show()

    def show_image(self, blink=True):
        global image_zero
        global image_one

        self.clear()

        if not blink:
            self.draw_image(image_zero)
            return

        self.blink_task = create_task(self.blink_image())

    async def blink_image(self):
        while True:
            self.draw_image(image_zero)
            await sleep(0.5)
            self.draw_image(image_one)
            await sleep(0.5)

    def clear(self):
        self.text = ""
        self.stop_async_tasks()

        self.display.fill(0)
        self.display.show()


display = Display()
