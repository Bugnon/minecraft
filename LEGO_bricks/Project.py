## Author: Gabriel Fleischer et Furbringer
## Date: 5. 10. 2017
## File: 03_led2.py
## Affiliation: Gymnase du Bugnon
## OC informatique
## import the modules to access the GPIO

import RPi.GPIO as gpio

import time

## import os to execute the raspistill
import os
import os.path

def reset():
    print("reset 2")

def onButtonPressed():
    if not os.path.isfile("new_picture.jpg"):
        print("Wait a bit for the programme to take the last picture.")
        return
    if os.path.isfile("lsat_picture.jpg"):
        os.system("rm last_picture.jpg")
    os.system("mv new_picture.jpg last_picture.jpg")
    os.system("raspistill -o new_picture.jpg ")
    print("New picture taken")
  
print("Initialisation")  

## pin numbers
resetPushTime = 5
button = 18
gpio.setmode(gpio.BCM)
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_UP)

#Create the first image of the picture
os.system("raspistill -o new_picture.jpg ")

pushed = False

print("Program ready")

alreadyReset = False
pressingTime = 0

while True:
    if not gpio.input(button):
        if not pushed:
            pushed = True
    else:
##        Execute the function on release and when it wasn't reset
        if pushed and not alreadyReset:
            print("button pressed")
            onButtonPressed()
        pressingTime = time.time()
        pushed = False
        alreadyReset = False
        
##    used to reset the building platform
    if time.time() - pressingTime >= resetPushTime and not alreadyReset:
        reset()
        alreadyReset = True
