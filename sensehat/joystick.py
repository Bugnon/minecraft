## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 5. 1. 2018
## File: joystick.py

## Import modules
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

## Display the letters UDLRM (up, down, left, right, middle)
while True:
    for event in sense.stick.get_events():
        direction = event.direction[0].upper()
        sense.show_letter(direction) 
    sleep(0.2)
    sense.clear()