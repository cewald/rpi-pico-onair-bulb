from machine import Pin, SPI
from time import sleep
from lib.max7219 import Matrix8x8
from src.image import image


class Display(object):
    def __init__(self):
        print("Init display")

        self.text = ""
        self.matrix_count = 4
        self.spi = SPI(0, sck=Pin(2), mosi=Pin(3))
        self.cs = Pin(5, Pin.OUT)
        self.display = Matrix8x8(self.spi, self.cs, self.matrix_count)

        self.display.brightness(0)
        self.display.fill(0)
        self.display.show()
        self.display.brightness(1)

    def show_text(self, text="PICO", delay=0.1):
        self.clear()
        self.text = text

        if len(text) > 4:
            total_length = len(text) * 8
            for i in range(-(self.matrix_count * 8), total_length + 1):
                self.display.fill(0)
                self.display.text(text, i, 0, 1)  # Adjust the position of the text
                self.display.show()
                sleep(delay)
        else:
            self.display.text(text, 0, 0, 1)
            self.display.show()

    def show_image(self):
        global image
        for y in range(8):
            for x in range(self.matrix_count * 8):
                # Determine which byte in the bitmap corresponds to the current pixel
                byte_index = (y * self.matrix_count) + (x // 8)
                # Get the specific byte from the bitmap
                byte = image[byte_index]
                # Extract the individual bit corresponding to the current pixel
                bit = (byte >> (7 - (x % 8))) & 1
                # Set the pixel on the display (1 = on, 0 = off)
                self.display.pixel(x, y, bit)

        self.display.show()

    def clear(self):
        self.text = ""
        self.display.fill(0)
        self.display.show()


display = Display()
