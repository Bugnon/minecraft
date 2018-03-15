import time
import pyautogui
from mcpi.minecraft import Minecraft
import RPi.GPIO as gpio
mc = Minecraft.create()
x, y, z = mc.player.getPos()

buttonL = 14
buttonR = 15

gpio.setmode(gpio.BCM)
gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonR, gpio.IN, pull_up_down=gpio.PUD_UP)
    
left0 = False
right0 = False

while True:
    left = gpio.input(buttonL)
    right = gpio.input(buttonR)

    x,y,z = mc.player.getPos()
    
    if left and not left0:
        pyautogui.click()
        
    left = left0

    