import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5

choix = input()

if choix == 1:
    
    angle = input()
    duree = input()
    
    pwm = GPIO.PWM(17, 100)
    pwm.start(5)
    
    angleChoisi = float(angle)/10 + ajoutAngle
    pwm.ChangeDutyCycle(angleChoisi)
    time.sleep(duree)
    GPIO.cleanup()
    
