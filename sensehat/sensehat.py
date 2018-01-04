## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 4. 1. 2018
## File: sensehat.py

from sense_hat import SenseHat
sense = SenseHat()


# Display text on the Sense HAT
msg = 'Minecraft'
sense.scroll_speed = 0.5
sense.text_color = (255, 0, 0)
sense.show_message(msg)

# Turn all LEDS to red, green or blue
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
sense.clear(blue)