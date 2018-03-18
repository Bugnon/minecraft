import time
import pyautogui
from mcpi.minecraft import Minecraft
import RPi.GPIO as gpio
mc = Minecraft.create()
x, y, z = mc.player.getPos()

buttonL = 14
buttonR = 15
buttonH = 
buttonI = 
buttonA = 
buttonB =
buttonS =
buttonJ =

gpio.setmode(gpio.BCM)
gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonR, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonH, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonI, gpio.IN, pull_up_down=gpio.PUD_UP)    
gpio.setup(buttonA, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonB, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonS, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonJ, gpio.IN, pull_up_down=gpio.PUD_UP)

L0 = False
R0 = False
H0 = True
I0 = True
A0 = True
B0 = True
S0 = True
J0 = True

while True:
    L = gpio.input(buttonL)
    R = gpio.input(buttonR)
    H = gpio.input(buttonH)
    I = gpio.input(buttonI)
    A = gpio.input(buttonA)
    B = gpio.input(buttonB)
    S = gpio.input(buttonS)
    J = gpio.input(buttonJ)
    
    x,y,z = mc.player.getPos()

# Début code avancer buttons

    if not L and L0:
	    pyautogui.keyDown('w')
    if L and not L0:
	    pyautogui.keyUp('w')
		
    L0 = L
    
    if not R and R0:
	    pyautogui.keyDown('w')
    if R and not R0:
	    pyautogui.keyUp('w')
		
		
    R0 = R

# Début code création d'une brique (type 1 = pierre)
    
    if not H and H0:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x, y, z+1, x, y, z+1, 1)
        
    H = H0
    
    
    if not I and I0:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x+1, y, z, x+1 ,y, z, 1)

    I = I0
    
# Début code casser une brique

    if not A and A0:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x+1, y, z, x+2 ,y, z, 0)

    A = A0
    
    if not B and B0:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x, y, z+1, x, y, z+2, 0)
        
    B = B0
    
# Début code changement de bloc/arme en main

    if not S and S0:
        pyautogui.vscroll(-1)

    S = S0

# Début code saut et vol

    if not J and J0:
        pyautogui.keyDown('space')
    
    if J and not J0:
        pyautogui.keyUp('space')
        
    J0 = J

# Début code rotation personnage
    
    
