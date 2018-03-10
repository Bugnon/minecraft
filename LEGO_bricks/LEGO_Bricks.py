## Author: Gabriel Fleischer et Furbringer
## Date: 5. 10. 2017
## File: 03_led2.py
## Affiliation: Gymnase du Bugnon
## OC informatique
## import the modules to access the GPIO

import RPi.GPIO as gpio
## import cv2 modules
import cv2
import numpy as np

import time
##import minecraft module
import mcpi

#import camera module
from picamera.array import PiRGBArray
from picamera import PiCamera

# =======================================
# Initialisation
# =======================================
# ---------------------------------------
# Initial configurations
# ---------------------------------------
antirebond_time = 0.10


# ---------------------------------------
# Pin numbers
# ---------------------------------------
button = 14

# ---------------------------------------
# Flags
# ---------------------------------------
# 0  = released
# 1  = beeing pushed
#' ' = pushed

flag=0
# ---------------------------------------
time_flag=0

# ---------------------------------------
# Gpio initalisation
# ---------------------------------------
gpio.setmode(gpio.BCM)

gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_UP)

def button_fct_pressed():
    """Test if button is pressed, released, or beeing pressed.
transform button flags :
        -0  for released
        -1 for beeing pushed
        -' ' for pushed
"""
    if  not gpio.input(button) and flag==0 and (time_flag==0 or time_flag+antirebond_time<time.time()):
        flag=1
        time_flag=time.time()
        return
    if (flag== 1 or flag==' ') and not gpio.input(button):
        flag = ' '
        return
    
    if (flag==' ' or flag==1 )and gpio.input(button) and (time_flag==0 or time_flag+antirebond_time<time.time()):       
        flag=0
        time_flag=time.time()
        return

def placeBlock(x, y):
    

def checkDif(img1, img2, x, y, tolerence=30):
    dif = img1[x, y]-img2[x, y]
    return (dif >= 0 and dif <= tolerence) or (dif < 0 and -dif <= tolerence)
    

def onButtonPressed():
    print("Pressed")
    f = camera.capture(rawCapture, format="bgr")
    last_pic = new_pic
    new_pic = f.array
    (B1, G1, R1) = cv2.split(last_pic)
    (B2, G2, R2) = cv2.split(new_pic)
    for (x, y, mcx, mcy) in positions:
        if checkDif(B1, B2, x, y) or checkDif(G1, G2, x, y) or checkDif(R1, R2, x, y):
            placeBlock(mcx, mcy)
    
    
def reset():
    print("reset")
    
    
# initialize the camera and grab a reference to the raw camera
# capture
camera = PiCamera()
#camera.resolution = (640, 480)
camera.resolution = (160, 120)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

#reset detection
resetPushTime = 5
alreadyReset=False

#pictures
last_pic
new_pic

while True:
    if flag:
        pushed = True
        
    button_fct_pressed()
    
    if not flag:
        if pushed and not alreadyReset:
            onButtonPressed()
        alreadyReset = False
    
    t = time.time()
    if t - time_flag  >= resetPushTime:
        reset()
        alreadyReset=True
