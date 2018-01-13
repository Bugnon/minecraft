## Author: Gabriel Fleischer et Furbringer
## Date: 5. 10. 2017
## File: 03_led2.py
## Affiliation: Gymnase du Bugnon
## OC informatique
## import the modules to access the GPIO

import RPi.GPIO as gpio

## import os to execute the raspistill
import os

def onButtonPressed():
    os.system("rm last_picture.jpg")
    os.system("mv new_picture.jpg last_picture.jpg")
    os.system("raspistill -o new_picture.jpg ")
    
## pin numbers
pushed = False
button = 18
gpio.setmode(gpio.BCM)
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_UP)

#Create the first image of the picture
os.system("raspistill -o new_picture.jpg ")

while True:
    if gpio.input(button) and not pushed:
        pushed = True
        onButtonPressed()
    else:
        pushed = False