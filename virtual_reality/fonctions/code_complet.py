import time
import pyautogui
from mcpi.minecraft import Minecraft
import RPi.GPIO as gpio
from time import sleep
mc = Minecraft.create()
x, y, z = mc.player.getPos()

buttonL = 
buttonR = 
buttonH = 
buttonA = 
buttonS = 
buttonJ = 

gpio.setmode(gpio.BCM)
gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonR, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonH, gpio.IN, pull_up_down=gpio.PUD_UP)    
gpio.setup(buttonA, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonS, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonJ, gpio.IN, pull_up_down=gpio.PUD_UP)

L0 = False
R0 = False
H0 = True
A0 = False
S0 = True
J0 = True

gpio.setup(2, gpio.OUT)
pwmAH = gpio.PWM(2, 50)

# fonction servo casser briques

def SetAngle(angle):
	duty = angle / 18 + 2
	gpio.output(2, True)
	pwmAH.ChangeDutyCycle(duty)
	sleep(1)
	gpio.output(2, False)
	pwmAH.ChangeDutyCycle(0)



while True:
    L = gpio.input(buttonL)
    R = gpio.input(buttonR)
    H = gpio.input(buttonH)
    A = gpio.input(buttonA)
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
            pwmAH.start(100)
            SetAngle(50)

    if H and not H0:
            pwmAH.start(50)
            SetAngle(100)
	    
    H0 = H
    
# Début code casser une brique

    if not A and A0:
            pwmAH.start(100)
            SetAngle(50)

    if A and not A0:
            pwmAH.start(50)
            SetAngle(100)
	    
    A0 = A
    
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
    
  
  
# fin code
pwm.stop()
gpio.cleanup()