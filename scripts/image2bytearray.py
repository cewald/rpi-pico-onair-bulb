from PIL import Image


def image_to_bytearray(image_path, width, height):
    # Open the image and convert it to black and white (1-bit pixels)
    image = Image.open(image_path).convert(
        "1"
    )  # '1' mode is 1-bit pixels, black and white

    # Resize the image to match the display dimensions
    image = image.resize((width, height))

    # Create a bytearray to hold the pixel data
    byte_array = bytearray()

    # Loop over the image's pixels
    for y in range(height):
        row_byte = 0
        for x in range(width):
            # Get the pixel value (0 or 255, where 0 is black and 255 is white)
            pixel = image.getpixel((x, y))

            # Pack the pixel into the byte (assuming 8 pixels per byte)
            if pixel == 0:  # Black pixel (set bit to 1)
                row_byte |= 1 << (7 - (x % 8))

            # Once we've processed 8 pixels, append the byte to the bytearray
            if x % 8 == 7:
                byte_array.append(row_byte)
                row_byte = 0

        # Append the remaining byte if width is not divisible by 8
        if width % 8 != 0:
            byte_array.append(row_byte)

    return byte_array


# Example usage: convert an image to a bytearray for a 32x8 MAX7219 display
byte_array_one = image_to_bytearray("image-1.png", 32, 8)
byte_array_zero = image_to_bytearray("image-0.png", 32, 8)

# Print the bytearray in src/image.py file
with open("src/image.py", "w+") as f:
    f.write("image_one = bytearray(" + "\n")
    f.write("    [" + "\n")
    for byte in byte_array_zero:
        f.write(f"        0b{byte:08b},\n")
    f.write("    ]\n")
    f.write(")\n\n")

    f.write("image_zero = bytearray(" + "\n")
    f.write("    [" + "\n")
    for byte in byte_array_one:
        f.write(f"        0b{byte:08b},\n")
    f.write("    ]\n")
    f.write(")\n")
