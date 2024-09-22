from machine import Pin, SPI
import src.max7219


class Display(object):
    def __init__(self):
        print("Init display")

        self.spi = SPI(0, sck=Pin(2), mosi=Pin(3))
        self.cs = Pin(5, Pin.OUT)
        self.display = src.max7219.Matrix8x8(self.spi, self.cs, 4)

        self.display.brightness(0)
        self.display.fill(0)
        self.display.show()
        self.display.brightness(1)

    def show_text(self, text="PICO"):
        self.clear()

        self.display.text(text, 0, 0, 1)
        self.display.show()

    def clear(self):
        self.display.fill(0)
        self.display.show()


display = Display()
