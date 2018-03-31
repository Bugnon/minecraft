import time
import pyautogui
from mcpi.minecraft import Minecraft
import RPi.GPIO as gpio
mc = Minecraft.create()
x, y, z = mc.player.getPos()

buttonL = 14

gpio.setmode(gpio.BCM)
gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)

left0 = True

while True:
    left = gpio.input(buttonL)
    x,y,z = mc.player.getPos()
    
    if left and not left0:
        pyautogui.keyUp('space')
    
    if not left and left0:
        pyautogui.keyDown('space')
        
    left0 = left