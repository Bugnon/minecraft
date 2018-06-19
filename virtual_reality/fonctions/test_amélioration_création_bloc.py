import time
import pyautogui
from mcpi.minecraft import Minecraft
import RPi.GPIO as gpio
from mcpi import block
mc = Minecraft.create()


buttonL = 14
buttonR = 15

gpio.setmode(gpio.BCM)
gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonR, gpio.IN, pull_up_down=gpio.PUD_UP)
    
left0 = True
right0 = False

def changement_brick(n):
    n = n+1
    return n


while True:
    left = gpio.input(buttonL)
    right = gpio.input(buttonR)
    n = 1
    if right and not right0:
        n = n+1
        
    if not left and left0:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x+1, y, z, x+1 ,y, z, n )

    left = left0
    
