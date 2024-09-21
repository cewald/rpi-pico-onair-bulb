from machine import Pin, SPI
import src.max7219

spi = SPI(0, sck=Pin(2), mosi=Pin(3))
cs = Pin(5, Pin.OUT)
display = src.max7219.Matrix8x8(spi, cs, 4)
display.brightness(1)


def showText(text="PICO"):
    clear()
    display.text(text, 0, 0, 1)
    display.show()


def clear():
    display.fill(0)
    display.show()
