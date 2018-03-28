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

def SetAngleL(angle):
	duty = angle / 18 + 2
	gpio.output(2, True)
	pwmL.ChangeDutyCycle(duty)
	sleep(0.5)
	gpio.output(2, False)
	pwmL.ChangeDutyCycle(0)
	
def SetAngleR(angle):
	duty = angle / 18 + 2
	gpio.output(3, True)
	pwmR.ChangeDutyCycle(duty)
	sleep(0.75)
	gpio.output(3, False)
	pwmR.ChangeDutyCycle(0)
# Code couplé bouton et Servo


while True:
    left = gpio.input(buttonL)
    right = gpio.input(buttonR)

    if not left and left0:
            pwmL.start(0)
            SetAngleL(90)

    if left and not left0:
            pwmL.start(90)
            SetAngleL(0)
	    
    left0 = left

    if not right and right0:
            pwmR.start(100)
            SetAngleR(10)
            
    if right and not right0:
            pwmR.start(10)
            SetAngleR(100)
            
    right0 = right



pwm.stop()
gpio.cleanup()