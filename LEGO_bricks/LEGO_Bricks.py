## Author: Gabriel Fleischer et Furbringer
## Date: 5. 10. 2017
## Affiliation: Gymnase du Bugnon
## OC informatique
## import the modules to access the GPIO
import RPi.GPIO as gpio
## import cv2 modules
import cv2
import numpy as np

import math

import time
##import minecraft module
import mcpi

#import camera module
from picamera.array import PiRGBArray
from picamera import PiCamera

from mcpi.minecraft import Minecraft

print("Initialising")

mc = Minecraft.create()
mc.postToChat("Initialising")
p = mc.player

hight = 1

def placeBlock(x,y):
    global hight
    global mc
    
    mc.postToChat(str((x, hight, y)))
    
    mc.setBlock(x,hight,y, 35, 15)

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
    global flag
    global time_flag
    global button
    global antirebond_time
    
    if  not gpio.input(button) and flag==0 and (time_flag==0 or time_flag+antirebond_time<time.time()):
        flag=1
        time_flag=time.time()
    elif (flag== 1 or flag==' ') and not gpio.input(button):
        flag = ' '
    
    elif (flag==' ' or flag==1 )and gpio.input(button) and (time_flag==0 or time_flag+antirebond_time<time.time()):       
        flag=0
        time_flag=time.time()

def init(angle, center, radius):
    global mc
    p = mc.player
    
    p.setPos(9, 10,0)
    mc.setBlocks(-2,-1,-2, 10, 100, 10, 155)
    mc.setBlocks(-1,0,-1, 9, 100, 9, 0)
    mc.setBlocks(0,-1,0, 8, -1, 8, 2)
    
    (cx, cy) = center
    minX = int(cx - radius)
    minY = int(cy - radius)
    maxX = int(cx + radius)
    maxY = int(cy + radius)
    return (angle, (minY, minX), (maxY, maxX), (int(cy), int(cx)))

def checkDif(img1, img2, x, y, dif2, image, tolerence=70):
    pos1 = int(img1[x, y])
    pos2 = int(img2[x, y])
    dif = pos1 - pos2 - dif2
    if dif < 0:
        dif = -dif
    return dif >= tolerence

def takePicture(frame, frameData):
    (angle, (minX, minY), (maxX, maxY), (centerX, centerY)) = frameData
    dims = frame.shape[:2]
    M = cv2.getRotationMatrix2D((centerX, centerY), angle, 1)
    frame = cv2.warpAffine(frame, M, dims)
    frame = frame[ minX:maxX , minY:maxY ]
    frame = cv2.resize(frame, (150, 150), interpolation = cv2.INTER_AREA)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    return frame

def onButtonPressed():
    global last_pic
    global new_pic
    global positions
    global pointToWatch
    global hight
    
    (b1, g1, r1) = last_pic[pointToWatch[0], pointToWatch[1]]
    (b2, g2, r2) = last_pic[pointToWatch[0], pointToWatch[1]]
    
    r = r1-r2
    g = g1-g2
    b = b1-b2

    (B1, G1, R1)=cv2.split(last_pic)
    (B2, G2, R2)=cv2.split(new_pic)
    for (mcx, mcy, x, y) in positions:
        if checkDif(B1, B2, x, y, b, "Bleu") or checkDif(G1, G2, x, y, g, "vert") or checkDif(R1, R2, x, y, r, "rouge"):
            placeBlock(mcx, mcy)
    hight = hight+1
   
def buildPositions(n, border, totalLenght):
    poses = []
    for mcx in range(n):
        for mcy in range(n):
            poses.append((mcx, mcy, int(border + (totalLenght-2*border)/(n - 1)*mcx), int(border + (totalLenght-2*border)/(n - 1)*mcy)))
    return poses
    
def reset():
    global mc
    global hight
    print("reset")
    mc.setBlocks(-2,-1,-2, 9, 100, 9, 155)
    mc.setBlocks(-1,0,-1, 8, 100, 8, 0)
    mc.setBlocks(0,-1,0, 7, -1, 7, 2)
    mc.postToChat("reset")
    hight = 1
    
def showInit(positions, image):
    global pointToWatch
    
    p = image.copy()
    for (mcx, mcy, x, y) in positions:
        p[x-1:x+1 , y-1:y+1] = (0, 0, 255)
    p[pointToWatch[0], pointToWatch[1]] = (0, 255, 0)
    return p


# initialize the camera and grab a reference to the raw camera
# capture
camera = PiCamera()
#camera.resolution = (640, 480)
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640, 480))


##Manual
frameData = init(-2, (350, 292), 95)
pointToWatch = (3, 30)

#reset detection
resetPushTime = 5
alreadyReset=False

#pictures
last_pic = None
new_pic = None

#List of tuples storing the diffrent positions of the LEGO bricks to check.
#tuple : (mcx, mcy, x, y)
# x : pixel x 
# y : pixel y
# mcx : minecraft x
# mcy : minecraft y
##Manual
positions = buildPositions(8, 16, 150)

i = -1
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = takePicture(f.array, frameData)
    i = i + 1
    if new_pic == None and i > 2:
        new_pic = frame
        last_pic = frame
        print("Initialisation complete !")
        mc.postToChat("Initialisation complete !")
    pushed = False
    if flag:
        pushed = True
        
    button_fct_pressed()
    
    if not flag:
        if pushed and not alreadyReset:
            last_pic = new_pic
            new_pic = frame
            onButtonPressed()
        alreadyReset = False
    
    t = time.time()
    if flag and t - time_flag  >= resetPushTime and not alreadyReset:
        reset()
        alreadyReset=True
        
    
    if new_pic != None :
        cv2.imshow("Diff", showInit(positions, new_pic))
        #cv2.imshow("Diff", np.hstack([new_pic, last_pic]))
    rawCapture.truncate(0)
    
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break