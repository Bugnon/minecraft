import time
import pyautogui
import RPi.GPIO as gpio
from time import sleep

buttonA = 23# clique gauche souris, connecter à pwmL
buttonB = 24# clique droit souris, connecter à pwmR

gpio.setmode(gpio.BCM)
gpio.setup(buttonA, gpio.IN, pull_up_down=gpio.PUD_UP)    
gpio.setup(buttonB, gpio.IN, pull_up_down=gpio.PUD_UP)

A0 = False 
B0 = False

# Servo pour clique gauche, connecté à bouton A

gpio.setup(18, gpio.OUT)
pwmL = gpio.PWM(18, 50)

# Servo pour clique droit, connecté à bouton B

gpio.setup(13, gpio.OUT)
pwmR = gpio.PWM(13, 50)

##Etat de base des servo

pwmL.start(5)# Etat de base du servo pwmL
pwmR.start(6.5)#  Etat de base du servo pwmR

while True:
## Code créer et casser brique avec servo pwmL et pwmR button A et button B

    A = gpio.input(buttonA)
    B = gpio.input(buttonB)

# clique gauche de la souris, casser une brique

    if not A and A0:
            pwmL.ChangeDutyCycle(9.4)
            time.sleep(0.5)
            pwmL.ChangeDutyCycle(5)
    if A and not A0:
            pass
	    
    A0 = A
    
# clique droite de la souris, créer une brique

    if not B and B0:
            pwmR.ChangeDutyCycle(2.5)
            time.sleep(0.75)
            pwmR.ChangeDutyCycle(6.5)
            
    if B and not B0:
            pass
            
    B0 = B
    