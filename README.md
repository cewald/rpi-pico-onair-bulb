# DIY On-Air-Display controlled by a REST-API

This is the repository for a DIY on-air-display using a [MAX7219 8x32 LED matrix](https://www.amazon.de/Youmile-Control-LED-Anzeigemodul-Arduino-Raspberry/dp/B099F2MN15) controlled by a [Raspberry Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) running a [micropython](https://micropython.org/) REST-API.

## Configuration

Make a copy of `config.sample.json`, name it `config.json` and apply your configs.

## Create a custom image (transform image into `byte_array`)

By default the `byte_array` representation of the `image.png` in the root folder in `src/image.py` is displayed.

To create a custom image follow these steps:

1. install `pillow` library:
   ```
   pip3 install pillow
   ```
1. create your monochrome PNG image in the dimensions of 8x32px and replace the `image.png` in the root folder
1. run the image2bytearray script in the root folder:
   ```
   python3 image2bytearray.py
   ```
1. the `src/image.py` should now be updated with your `byte_array` representation of your image