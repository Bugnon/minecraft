# Authors:Albert and Ludovic
# Date: 03.2018

# Affiliation : Gymnase du Bugnon
# Year 2017-2018
# Classe : OC-Informatique
# =======================================
# ---------------------------------------
# import the necessary packages
# ---------------------------------------
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import os
from  mcpi.minecraft import Minecraft

##mc = Minecraft.create()

# ---------------------------------------
# import minecraft construction functions
# ---------------------------------------
import Bridge
import House
import Midas
import Mine

# ---------------------------------------
# initialize the camera and grab a reference to the raw camera
# ---------------------------------------
# capture
camera = PiCamera()
#camera.resolution = (640, 480)
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(1)
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

#inspired from https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/        
# ---------------------------------------
# functions
# ---------------------------------------
def detect_red(img, lower, upper):
    """ Detect colors which are in the range [lower, upper] """
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
     
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)
##    cv2.imshow("Mask", mask)
##    cv2.imshow("Detect color", np.hstack([img, output]))
    
    LUm = mask[0:120,0:120]
    LDm = mask[120:240,0:120]
    Midm = mask[0:240,120:200]
    RUm= mask[0:120,240:]
    RDm = mask[120:240,240:]
    
    regions =[LUm, LDm, Midm, RUm, RDm]

    for i in range(5):
        regions_red[i]=np.average(regions[i])>redmin
        
def detect_blue(img, lower, upper):
    """ Detect colors which are in the range [lower, upper] """
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
     
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)
##    cv2.imshow("Mask", mask)
##    cv2.imshow("Detect color", np.hstack([img, output]))
    
    LUm = mask[0:120,0:120]
    LDm = mask[120:240,0:120]
    Midm = mask[0:240,120:200]
    RUm= mask[0:120,240:]
    RDm = mask[120:240,240:]
    
    regions =[LUm, LDm, Midm, RUm, RDm]

    for i in range(5):
        regions_blue[i]=np.average(regions[i])>bluemin
##    print(regions_blue)

def button_fct_pressed(nb):
    """Test if nb (button + number of button) is pressed, released, or beeing pressed.
transform button flags :
        -0  for released
        -1 for beeing pushed
        -' ' for pushed
        
nb: str
"""
    if  not gpio.input(eval(nb)) and flags[nb]==0 and (time_flag[nb]==0 or time_flag[nb]+antirebond_time<time.time()):
        flags[nb]=1
        time_flag[nb]=time.time()
        return
    if (flags[nb]== 1 or flags[nb]==' ') and not gpio.input(eval(nb)):
        flags[nb] = ' '
        return
    
    if (flags[nb]==' ' or flags[nb]==1 )and gpio.input(eval(nb)) and (time_flag[nb]==0 or time_flag[nb]+antirebond_time<time.time()):       
        flags[nb]=0
        time_flag[nb]=time.time()
        return

def check_buttons_fct():
    """execute for every button (1,2,3,4,5,6,7,8,9,10) the fonction : button_fct_pressed(nb):
"""
    button_fct_pressed('button1')
    button_fct_pressed('button2')
    button_fct_pressed('button3')
    button_fct_pressed('button4')
    button_fct_pressed('button5')
    button_fct_pressed('button6')
    button_fct_pressed('button7')
    button_fct_pressed('button8')
    button_fct_pressed('button9')
    button_fct_pressed('button10')
    

# ---------------------------------------
#initialisation of values
# ---------------------------------------
lowerR = [0, 0, 60]
upperR = [50, 70, 255]
lowerB = [60, 0, 0]
upperB = [255, 70, 50]
redmin=50
bluemin=30



regions_red =[False, False, False, False, False]     #=[LU, LD, Mid, RU, RD]
regions_blue =[False, False, False, False, False]     #=[LU, LD, Mid, RU, RD]

flags={'button1':0,'button2':0,'button3':0,'button4':0,'button5':0,'button6':0,'button7':0,'button8':0,'button9':0,'button10':0}
time_flag={'button1':0,'button2':0,'button3':0,'button4':0,'button5':0,'button6':0,'button7':0,'button8':0,'button9':0,'button10':0}
# ---------------------------------------
# initialisation param minecraft
# ---------------------------------------
param1=False  #False = petit, True = grand
param2=False  #False = materiaux 1, True = materiaux 2
mc_funct=0    # 0= None, 1= Bridge, 2= House, 3= Midas, 4= Mine

start= 0      # 0 = neutral, 1 = execution, -1= stop Magic_wand.py
# ---------------------------------------
# loop
# ---------------------------------------

# capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = f.array   
    frameClone = cv2.flip(frame.copy(),1)
    
    # ---------------------------------------
    #detect color and position:
    # ---------------------------------------
    detect_red(frameClone, lowerR, upperR)
    detect_blue(frameClone, lowerB, upperB)
    
    # ---------------------------------------
    # works like a button:
##=[LU, LD, Mid, RU, RD]
##    button1 
##    button2 
##    button3 
##    button4 
##    button5 
##    button6
##    button7
##    button8
##    button9
##    button10
    
    # ---------------------------------------
    #Stack images
    # ---------------------------------------
    #All frames are separated
    Left= frameClone[0:240,0:120]
    LU=Left[0:120,0:120]
    LD=Left[120:240,0:120]
    Mid=frameClone[0:240,120:200]
    Right= frameClone[0:240,200:320]
    RU=Right[0:120,0:120]
    RD=Right[120:240,0:120]
    Right2=np.vstack([RU,RD])
    Left2=np.vstack([LU,LD]) 
    All=np.hstack([Left2,Mid,Right2])
    
    # ---------------------------------------
    # lines
    # ---------------------------------------
    All[0:240,119:122]=(0,255,255)
    All[0:240,199:202]=(0,255,255)
    All[119:122,0:119]=(0,255,255)
    All[119:122,202:320]=(0,255,255)
    # ---------------------------------------
    # apercu
    # ---------------------------------------
    cv2.imshow("All", All)
    rawCapture.truncate(0)


    # ---------------------------------------
    # if you want to break the program
    # ---------------------------------------
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    if start == -1:
        break
