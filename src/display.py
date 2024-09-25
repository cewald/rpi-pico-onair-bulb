from asyncio import Event, create_task, sleep, CancelledError
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

        self.display.brightness(0)
        self.display.fill(0)
        self.display.show()
        self.display.brightness(1)

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
        print('bounce_text', text)

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
                # Determine which byte in the bitmap corresponds to the current pixel
                byte_index = (y * self.matrix_count) + (x // 8)
                # Get the specific byte from the bitmap
                byte = image_byte_array[byte_index]
                # Extract the individual bit corresponding to the current pixel
                bit = (byte >> (7 - (x % 8))) & 1
                # Set the pixel on the display (1 = on, 0 = off)
                self.display.pixel(x, y, bit)

        self.display.show()

    def show_image(self):
        global image_zero
        global image_one
        self.draw_image(image_zero)

    def stop_bounce_text(self):
        if self.bounce_task and not self.bounce_task.done():
            self.bounce_task.cancel()

        self.bounce_task = None

    def clear(self):
        self.text = ""
        self.stop_bounce_text()

        self.display.fill(0)
        self.display.show()


display = Display()
