## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 4. 1. 2018
## File: led_matrix.py

## Import modules
from sense_hat import SenseHat
from time import sleep
from random import randint, uniform, choice

## Create an instance of the SenseHat object
sense = SenseHat()
##sense.set_rotation(180)

# color definitions
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

colors = (red, green, blue, yellow, magenta, cyan, white, black)
          
# Display text on the Sense HAT
msg = 'Minecraft'
sense.show_message(msg, text_colour=blue, scroll_speed=0.05)

# Turn all LEDS to a range of colors
for color in colors:
    sense.clear(color)
    sleep(0.2)

## Display a letter
sense.show_letter('P')
sleep(0.5)
sense.show_letter('P', back_colour=white, text_colour=red)
sleep(0.5)

## Display the letters of a word
for i, c in enumerate("Minecraft"):
    sense.show_letter(c, colors[i%3])
    sleep(0.2)
    
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

for i, c in enumerate("Minecraft"):
    sense.show_letter(c, random_color())
    sleep(0.2)

## Set individual pixels
for x in range(8):
    for y in range(8):
        sense.set_pixel(x, y, blue)
        sleep(0.05)

g = (0, 255, 0) # green
b = (0, 0, 0) # black

creeper = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,b,b,g,g,b,b,g,
    g,b,b,g,g,b,b,g,
    g,g,g,b,b,g,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,g,g,b,g,g]

## Display an image on the LED matrix
sense.set_pixels(creeper)
sleep(1)

B = (102, 51, 0)
b = (0, 0, 255)
S = (205, 133, 63)
W = (255, 255, 255)

steve = [
    B,B,B,B,B,B,B,B,
    B,B,B,B,B,B,B,B,
    B,S,S,S,S,S,S,B,
    S,S,S,S,S,S,S,S,
    S,W,b,S,S,b,W,S,
    S,S,S,B,B,S,S,S,
    S,S,B,S,S,B,S,S,
    S,S,B,B,B,B,S,S]

## Display an image on the LED matrix
sense.set_pixels(steve)