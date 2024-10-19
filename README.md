# DIY On-Air-Display controlled by a REST-API

This is the repository for a DIY on-air-display using a [MAX7219 8x32 LED matrix](https://www.amazon.de/Youmile-Control-LED-Anzeigemodul-Arduino-Raspberry/dp/B099F2MN15) controlled by a [Raspberry Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) running a [micropython](https://micropython.org/) REST-API.

## Setup

### Parts

* [MAX7219 8x32 LED matrix]((https://www.amazon.de/Youmile-Control-LED-Anzeigemodul-Arduino-Raspberry/dp/B099F2MN15))
* [Raspberry Pico W]((https://www.raspberrypi.com/products/raspberry-pi-pico/))
* [Push-Button](https://www.amazon.de/DAOKAI-Momentary-Miniature-Electronic-Components/dp/B09WVFHMSV)
* 5V Micro-USB power-source or USB cable
* Wires

### Wiring

![wirechart](./fritzing/rpi-pico-onair-bulb_bb.png)

## Configuration

Make a copy of `config.sample.json`, name it `config.json` and apply your configs, like your WiFi credentials etc. .

Flash your Raspberry Pi Zero W with the [latest Micropython](https://micropython.org/download/RPI_PICO_W/) version (instructions on page).

Upload all files to the root folder of the Raspberry Pi Zero W.

After that you can unmount your Pi and put plug it to a suitable power-source. The device should power-up instantly and show its state on the display until it is connected.

Now the device is running and accesible via it's API and the button.

## API Docs

<details>
   <summary>
      <code>GET</code> <code>/toggle</code> Turn the default image on/off
   </summary>

   #### Parameters
   > None

   #### Responses
   > | http-code | content-type | response |
   > | --------- | ------------ | -------- |
   > | `200` | `text/plain;charset=UTF-8` | JSON |

   ##### Example cURL
   > ```bash
   >  curl -X GET http://192.168.0.111/toggle
   > ```
</details>
<details>
   <summary>
      <code>GET</code> <code>/toggle/:text</code> Turn any text value on/off
   </summary>

   #### Parameters
   > | name | type | data-type | description |
   > | ---- | ---- | --------- | ----------- |
   > | `text` | required | string (url-encoded) | the text-string you want to display, if it is longer than 4 letters it will scroll back and forth |


   #### Responses
   > | http-code | content-type | response |
   > | --------- | ------------ | -------- |
   > | `200` | `text/plain;charset=UTF-8` | JSON |

   ##### Example cURL
   > ```bash
   >  curl -X GET http://192.168.0.111/toggle/Hello%20World
   > ```
</details>

## Create a custom image (transform image into `byte_array`)

By default the `byte_array` representations of the `image-0.png` and `image-1.png` in the root folder in `src/image.py` is displayed.

To create a custom images follow these steps:

1. install `pillow` library:
   ```bash
   pip3 install pillow
   ```
1. create your monochrome (black and white) PNG images in the dimensions of 8x32px and replace the `image-0.png` and `image-1.png` in the root folder
1. run the `image2bytearray` script in the `/scripts` folder:
   ```bash
   python3 scripts/image2bytearray.py
   ```
1. the `src/image.py` should now be updated with your `byte_array` representation of your image