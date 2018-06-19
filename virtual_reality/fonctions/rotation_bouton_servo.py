import time
import RPi.GPIO as gpio



#Installations boutons
buttonL = 20
buttonR = 21


gpio.setmode(gpio.BCM)
gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonR, gpio.IN, pull_up_down=gpio.PUD_UP)

left0 = False
right0 = False

#Installations Servo

gpio.setup(2, gpio.OUT)

pwm = gpio.PWM(2, 50)

<<<<<<< HEAD

# Code couplé bouton et Servo
x = 7.5
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

#pwm.stop()



=======
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
>>>>>>> ec999de9cc35b16e2bc8a2ef6c6410df4f69f2ef

