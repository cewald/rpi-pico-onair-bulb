from machine import Pin, SPI
import src.max7219

bitmap = bytearray(
    [
        0x7F,
        0xFF,
        0xFF,
        0xFE,
        0x80,
        0x00,
        0x00,
        0x01,
        0x9C,
        0x63,
        0x3B,
        0x81,
        0xA2,
        0x94,
        0x92,
        0x99,
        0xA2,
        0x97,
        0x93,
        0x19,
        0x9C,
        0x94,
        0xBA,
        0x81,
        0x80,
        0x00,
        0x00,
        0x01,
        0x7F,
        0xFF,
        0xFF,
        0xFE,
    ]
)


class Display(object):
    def __init__(self):
        print("Init display")

        self.matrix_count = 4
        self.spi = SPI(0, sck=Pin(2), mosi=Pin(3))
        self.cs = Pin(5, Pin.OUT)
        self.display = src.max7219.Matrix8x8(self.spi, self.cs, self.matrix_count)

        self.display.brightness(0)
        self.display.fill(0)
        self.display.show()
        self.display.brightness(1)

        self.draw_bitmap()

    def show_text(self, text="PICO"):
        self.clear()

        self.display.text(text, 0, 0, 1)
        self.display.show()

    def draw_bitmap(self):
        global bitmap
        for y in range(8):
            for x in range(self.matrix_count * 8):
                # Determine which byte in the bitmap corresponds to the current pixel
                byte_index = (y * self.matrix_count) + (x // 8)
                # Get the specific byte from the bitmap
                byte = bitmap[byte_index]
                # Extract the individual bit corresponding to the current pixel
                bit = (byte >> (7 - (x % 8))) & 1
                # Set the pixel on the display (1 = on, 0 = off)
                self.display.pixel(x, y, bit)

        self.display.show()

    def clear(self):
        self.display.fill(0)
        self.display.show()


display = Display()
