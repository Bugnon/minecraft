# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#                         MAGIC WAND, MINECRABRACADABRA                       #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#      Auteurs:   Albert et Ludovic
#  Affiliation:   Gymnase du Bugnon
#        Annee:   2017-2018
#       Classe:   OC-Informatique

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# =========================================================================== #
#                            Description du Projet                            #
# =========================================================================== #
"""
A completer

Minecraft et une camera enclenche
"""
# =========================================================================== #
#                                Code du Projet                               #
# =========================================================================== #

# --------------------------------------------------------------------------- #
# Importation des modules necessaires
# --------------------------------------------------------------------------- #

# Le module permettant d'accéder à minecraft-pi
from mcpi.minecraft import Minecraft

# Les modules permettant d'utiliser la caméra
from picamera.array import PiRGBArray
from picamera import PiCamera

# Les modules permettant de faire le traitement de l'image
import cv2
import numpy as np

# Le  module permettant d'utiliser le temps
import time

# Le module permettant d'executer une fonction dans un terminal linux
import os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# importation des quatres fonctions de construction
import Bridge
import House
import Midas
import Mine

# creer une liaison avec minecraft
mc = Minecraft.create()
# --------------------------------------------------------------------------- #
# Initialisation de la camera
# --------------------------------------------------------------------------- #
camera = PiCamera()  # creation de la liaison avec la camera


def init_camera():
    """Initalise la camera du raspberry avec les parametres suivant:

- resolution: 320 x 240 pixels
- taux de trame: 32
- desactivation de gains automatique
"""
    # enregistrement dans une variable globale => utiliser apres
    global camera

    camera.resolution = (320, 240)
    camera.framerate = 32

    rawCapture = PiRGBArray(camera, size=(320, 240))

    time.sleep(1)  # pour que la camera puisse se "calibrer"

    # Desactivation du gains
    gains = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = gains
# --------------------------------------------------------------------------- #
# Initialisation des valeurs
# --------------------------------------------------------------------------- #
taille_fenetre = 620
waiting_time = 2

lowerR = [0, 0, 60]
upperR = [50, 70, 255]
lowerB = [60, 0, 0]
upperB = [255, 70, 50]
redmin = 50
bluemin = 30
RED = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)

regions_blue = [False, False, False, False, False]  # = [LU, LD, Mid, RU, RD]
regions_red = [False, False, False, False, False]  # = [LU, LD, Mid, RU, RD]

flags = {'button1': 0, 'button2': 0, 'button3': 0, 'button4': 0, 'button5': 0,
         'button6': 0, 'button7': 0, 'button8': 0, 'button9': 0, 'button10': 0}

time_flag = {'button1': 0, 'button2': 0, 'button3': 0, 'button4': 0,
             'button5': 0, 'button6': 0, 'button7': 0, 'button8': 0,
             'button9': 0, 'button10': 0}
# ---------------------------------------
# functions
# ---------------------------------------


def detect_colour(img, colour):
    """ Detect colors which are in the range [lower, upper] """
    if colour == "RED":
        lower = lowerR
        upper = upperR
    if colour == "BLUE":
        lower = lowerB
        upper = upperB
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)
#    cv2.imshow("Mask", mask)
#    cv2.imshow("Detect color", np.hstack([img, output]))

    LUm = mask[0:120, 0:120]
    LDm = mask[120:240, 0:120]
    Midm = mask[0:240, 120:200]
    RUm = mask[0:120, 240:]
    RDm = mask[120:240, 240:]

    regions = [LUm, LDm, Midm, RUm, RDm]
    if colour == "RED":
        for i in range(5):
            regions_red[i] = np.average(regions[i]) > redmin
    if colour == "BLUE":
        for i in range(5):
            regions_blue[i] = np.average(regions[i]) > bluemin
#        print(regions_blue)


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)

    else:
        r = width / float(w)
        dim = width, int(h*r)

    resized = cv2.resize(image, dim, interpolation=inter)

    return resized


def Colorize(img, colour, FULL=5):
    a = img.shape[1]
    b = img.shape[0]
    if FULL == "FULL":
        FULL = -1
    return cv2.rectangle(img, (0, 0), (a, b), colour, FULL)


def button_fct_pressed(n):
    """Test if nb (button + number of button) is pressed, released, or beeing
pressed.
transform button flags :

n: int (0..9)
"""
    nb = 'button' + str(n+1)

    if n < 5:
        if(flags[nb] == 1 or flags[nb] == 'e') and time_flag[nb] > time.time():
            liste[n] = Colorize(liste[n], BLUE, "FULL")
            flags[nb] = 'e'
            return
        if flags[nb] == 'e' and time_flag[nb] < time.time():
            liste[n] = Colorize(liste[n], BLUE, "FULL")
            flags[nb] = 0
        if regions_blue[n] is True:
            liste[n] = Colorize(liste[n], BLUE)
            if flags[nb] == 0 and time_flag[nb] < time.time():
                flags[nb] = ' '
                time_flag[nb] = waiting_time + time.time()
                return
            if flags[nb] == ' ' and time_flag[nb] < time.time():
                flags[nb] = 1
                time_flag[nb] = waiting_time + time.time()
                liste[n] = Colorize(liste[n], BLUE, "FULL")
                return
        if regions_blue[n] is False:
            flags[nb] = 0
            return
    if n > 4:
        n = n - 5
        if(flags[nb] == 1 or flags[nb] == 'e') and time_flag[nb] > time.time():
            liste[n] = Colorize(liste[n], RED, "FULL")
            flags[nb] = 'e'
            return
        if flags[nb] == 'e' and time_flag[nb] < time.time():
            liste[n] = Colorize(liste[n], RED, "FULL")
            flags[nb] = 0
        if regions_red[n] is True:
            liste[n] = Colorize(liste[n], RED)
            if flags[nb] == 0 and time_flag[nb] < time.time():
                flags[nb] = ' '
                time_flag[nb] = waiting_time + time.time()
                return
            if flags[nb] == ' ' and time_flag[nb] < time.time():
                flags[nb] = 1
                time_flag[nb] = waiting_time + time.time()
                liste[n] = Colorize(liste[n], RED, "FULL")
                return
        if regions_red[n] is False:
            flags[nb] = 0
            return


def exefct():
    global mc_funct, param1, param2, start

    if flags['button1'] is True:  # 1 = True = beeing pressed
        param1 = True
        mc.postToChat("Size: Big")
    if flags['button2'] is True:  # 1 = True = beeing pressed
        mc_funct = 1
        mc.postToChat("Function: Bridge")
    if flags['button3'] is True:  # 1 = True = beeing pressed
        if mc_funct == 0:
            mc.postToChat("You need to choose a function!")
        if mc_funct == 1:
            mc.postToChat("Working, wait...")
            fctBridge(param1, param2)
            mc.postToChat("Work done!")
        if mc_funct == 2:
            mc.postToChat("Working, wait...")
            fctHouse(param1, param2)
            mc.postToChat("Work done!")
        if mc_funct == 3:
            mc.postToChat("Working, wait...")
            fctMidas(param1, param2)
            mc.postToChat("Work done!")
        if mc_funct == 4:
            mc.postToChat("Working, wait...")
            fctMine(param1, param2)
            mc.postToChat("Work done!")
    if flags['button4'] is True:  # 1 = True = beeing pressed
        param2 = True
        mc.postToChat("Material: 2")
    if flags['button5'] is True:  # 1 = True = beeing pressed
        mc_funct = 3
        mc.postToChat("Function: Midas")
    if flags['button6'] is True:  # 1 = True = beeing pressed
        param1 = False
        mc.postToChat("Size: Small")
    if flags['button7'] is True:  # 1 = True = beeing pressed
        mc_funct = 2
        mc.postToChat("Function: House")
    if flags['button8'] is True:  # 1 = True = beeing pressed
        start = -1
        mc.postToChat("Good by! See you soon!")
    if flags['button9'] is True:  # 1 = True = beeing pressed
        param2 = False
        mc.postToChat("Material: 1")
    if flags['button10'] is True:  # 1 = True = beeing pressed
        mc_funct = 4
        mc.postToChat("Function: Mine")


def fctBridge(p1, p2):
    xp, yp, zp = mc.player.getTilePos()

    if p2 is True:
        M = "WOOD"
    else:
        M = "COBBLESTONE"

    Bridge.bridge(xp, yp, zp, "North", M)
    os('omxplayer -o local Desktop/minecraft/Magic_Wand/songs/Bridge.mp3')


def fctHouse(p1, p2):
    xp, yp, zp = mc.player.getTilePos()
    xp = xp + 4

    if p1 is True:
        length = 12
        width = 14
        height = 12

    if p1 is False:
        length = 7
        width = 5
        height = 7

    if p2 is True:
        M = "COBBLESTONE"

    if p2 is False:
        M = "WOOD"

    House.house(xp, yp, zp, length, width, height, M)
    os('omxplayer -o local songs/House.mp3')


def fctMine(p1, p2):
    xp, yp, zp = mc.player.getTilePos()
    if p1 is True:
        size = 80

    if p1 is False:
        size == 15

    Mine.Mine(xp, yp, zp, "North", 15)
    os('omxplayer -o local Desktop/minecraft/Magic_Wand/songs/Mine.mp3')


def fctMidas(p1, p2):
    xp, yp, zp = mc.player.getTilePos()
    if p1 is True:
        s = 15

    if p1 is False:
        s = 5

    if p2 is True:
        idb = 57

    if p2 is False:
        idb = 41

    Midas.Midascube(xp, yp, zp, s, idb)
    os('omxplayer -o local Desktop/minecraft/Magic_Wand/songs/Midas.mp3')

# ---------------------------------------
# initialisation param minecraft
# ---------------------------------------
param1 = False  # False = petit, True = grand
param2 = False  # False = materiaux 1, True = materiaux 2
mc_funct = 0    # 0= None, 1= Bridge, 2= House, 3= Midas, 4= Mine

start = 0      # 0 = neutral, 1 = execution, -1= stop Magic_wand.py
# ---------------------------------------
# loop
# ---------------------------------------

# capture frames from the camera
for f in camera.capture_continuous(rawCapture,
                                   format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = f.array
    frameClone = cv2.flip(frame.copy(), 1)

    # ---------------------------------------
    # detect color and position:
    # ---------------------------------------
    detect_colour(frameClone, "RED")
    detect_colour(frameClone, "BLUE")

    # ---------------------------------------
    # Stack images
    # ---------------------------------------
    # All frames are separated
    Left = frameClone[0:240, 0:120]
    Right = frameClone[0:240, 200:320]

    LU = Left[0:120, 0:120]
    LD = Left[120:240, 0:120]
    Mid = frameClone[0:240, 120:200]
    RU = Right[0:120, 0:120]
    RD = Right[120:240, 0:120]

    liste = [LU, LD, Mid, RU, RD]

    for i in range(10):
        button_fct_pressed(i)

#        if regions_red[i]==True:
#            liste[i]= Colorize(liste[i],RED)
#            button_fct_pressed(i+5)

    exefct()
    print(flags['button1'], flags['button2'], flags['button3'],
          flags['button4'], flags['button5'])

    Right2 = np.vstack([RU, RD])
    Left2 = np.vstack([LU, LD])
    All = np.hstack([Left2, Mid, Right2])

    # ---------------------------------------
    # lines
    # ---------------------------------------
    All[0:240, 119:122] = YELLOW
    All[0:240, 199:202] = YELLOW
    All[119:122, 0:119] = YELLOW
    All[119:122, 202:320] = YELLOW
    # ---------------------------------------
    # apercu
    # ---------------------------------------
    All = resize(All, taille_fenetre)
    cv2.imshow("Detection", All)
    rawCapture.truncate(0)

    # ---------------------------------------
    # if you want to break the program
    # ---------------------------------------
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if start == -1:
        break
