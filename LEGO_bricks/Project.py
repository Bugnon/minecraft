## Author: Gabriel Fleischer et Furbringer
## Date: 5. 10. 2017
## File: 03_led2.py
## Affiliation: Gymnase du Bugnon
## OC informatique
## import the modules to access the GPIO

import RPi.GPIO as gpio
import numpy as np
import time
import mcpi

import cv2

## import os to execute the raspistill
import os
import os.path

def reset():
    print("reset 2")

## images
new_pic = None
last_pic = None

def init():
    #takePic("new_picture.jpg")
    
    #time.sleep(4)
    global new_pic
    new_pic=cv2.imread("new_picture.jpg")
    
    (l, h)=new_pic.shape[:2]
    new_pic = cv2.resize(new_pic, (int(300*h/l), 300), interpolation = cv2.INTER_AREA)
    
    (B, G, R) = cv2.split(new_pic)
    gray= cv2.cvtColor(new_pic, cv2.COLOR_BGR2GRAY)
    gray= G

    gray = rotate()
    
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(gray, 170, 170)
    (_, cnts, _) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("", cv2.drawContours(gray, cnts, -1, (0, 255, 0), 1))
    cv2.waitKey(0)
    
def takePic(name):
    os.system("raspistill -o " + name)

def onButtonPressed():
    if not os.path.isfile("new_picture.jpg"):
        print("Wait a bit for the programme to take the last picture.")
        return
    if os.path.isfile("last_picture.jpg"):
        os.system("rm last_picture.jpg")
    os.system("mv new_picture.jpg last_picture.jpg")
    takePic("new_picture.jpg")
    print("New picture taken")
  
print("Initialisation")  

init()

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
