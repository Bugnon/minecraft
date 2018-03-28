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

pwm = gpio.PWM(2, 50)

def SetAngle(angle):
	duty = angle / 18 + 2
	gpio.output(2, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	gpio.output(2, False)
	pwm.ChangeDutyCycle(0)

def rot(x,angle):
    if not left and left0:
        if angle <= 100:
            pwm.start(x)
            SetAngle(angle+20)
            return angle
    
    if left and not left0:
        pass
    
    if not right and right0:
        if angle <= 100:
            pwm.start(x)
            SetAngle(angle-20)
            return angle
        
    if right and not right0:
            pass

# Code couplé bouton et Servo

while True:
    left = gpio.input(buttonL)
    right = gpio.input(buttonR)

    rot(10,40)
    left0 = left
    right0 = right
    
pwm.stop()
gpio.cleanup()

