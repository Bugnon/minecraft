import time
import pyautogui
import RPi.GPIO as gpio
from time import sleep


#Installations boutons
buttonL = 14
buttonR = 15

gpio.setmode(gpio.BCM)
gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonR, gpio.IN, pull_up_down=gpio.PUD_UP)

left0 = False
right0 = False

#Installations Servo

gpio.setup(2, gpio.OUT)
gpio.setup(3, gpio.OUT)

pwmL = gpio.PWM(2, 50)
pwmR = gpio.PWM(3, 50)

# Code couplé bouton et Servo

pwmL.start(5) 
pwmR.start(6.5)
while True:
    left = gpio.input(buttonL)
    right = gpio.input(buttonR)

    if not left and left0:
            pwmL.ChangeDutyCycle(9.4)
            time.sleep(0.5)
            pwmL.ChangeDutyCycle(5)
    if left and not left0:
            pass
	    
    left0 = left

    if not right and right0:
            pwmR.ChangeDutyCycle(2.5)
            time.sleep(0.75)
            pwmR.ChangeDutyCycle(6.5)
            
    if right and not right0:
            pass
            
    right0 = right



#pwm.stop() si besoin