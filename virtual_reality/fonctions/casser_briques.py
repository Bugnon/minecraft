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
right0 = True

while True:
    left = gpio.input(buttonL)
    right = gpio.input(buttonR)

    
    if not left and left0:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x+1, y, z, x+2 ,y, z, 0)

    left = left0
    
    if not right and right0:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x, y, z+1, x, y, z+2, 0)
        
    right = right0
