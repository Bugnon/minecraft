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
R0 = False

while True:
    left = gpio.input(buttonL)
    R = gpio.input(buttonR)

    x,y,z = mc.player.getPos()

    if not left and left0:
	    pyautogui.keyDown('w')
    if left and not left0:
	    pyautogui.keyUp('w')
		

    left0 = left

    
    if not R and R0:
	    pyautogui.keyDown('w')
    if R and not R0:
	    pyautogui.keyUp('w')
		
		
    R0 = R
    
    
    
    

    
    
    
    


























