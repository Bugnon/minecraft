# Authors: Albert and Ludovic
# Date: 04.10.2017

# Affiliation : Gymnase du Bugnon
# Année 2017-2018
# Classe : OC-Informatique

# ---------------------------------------

from  mcpi.minecraft import Minecraft

import RPi.GPIO as gpio
import time

mc = Minecraft.create()

## initial configurations
antirebond_time = 0.19

## pin numbers
button1 = 14
button2 = 15
button3 = 18
button4 = 23
button5 = 24


gpio.setmode(gpio.BCM)

def button_setup(nb):
    gpio.setup(eval(nb), gpio.IN, pull_up_down=gpio.PUD_UP)

def button_fct_pressed(nb):
    if  not gpio.input(eval(nb)):
        mc.postToChat("You've pressed "+ nb)
        while True:
            if gpio.input(eval(nb)):
                time.sleep(antirebond_time)
                break

def check_buttons_fct():
    button_fct_pressed('button1')
    button_fct_pressed('button2')
    button_fct_pressed('button3')
    button_fct_pressed('button4')
    button_fct_pressed('button5')

button_setup('button1')
button_setup('button2')
button_setup('button3')
button_setup('button4')
button_setup('button5')

while True:
    check_buttons_fct()

