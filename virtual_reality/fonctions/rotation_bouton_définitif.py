import time
import RPi.GPIO as gpio

#rotation bouton définitf

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


# Code couplé bouton et Servo
x = 5
pwm.start(x)

while True:
    left = gpio.input(buttonL)
    right = gpio.input(buttonR)


    if not left and left0 and x < 12.5:
        pwm.ChangeDutyCycle(x+2.5)
        x = x+2.5
        
    if  left and not left0:
            pass 

    left0 = left
    
    if not right and right0 and x > 2.5:
        pwm.ChangeDutyCycle(x-2.5)
        x = x-2.5

    if right and not right0:
        pass		
		
    right0 = right
