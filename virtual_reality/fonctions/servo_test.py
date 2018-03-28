import time
import pyautogui
import RPi.GPIO as gpio


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




pwm.start(7.5)


try:
        while True:
                pwm.ChangeDutyCycle(2.5)
                time.sleep(1)
                pwm.ChangeDutyCycle(5) 
                time.sleep(1)
                pwm.ChangeDutyCycle(7.5) 
                time.sleep(1)
                pwm.ChangeDutyCycle(10)
                time.sleep(1)
                pwm.ChangeDutyCycle(12.5)
                time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()

    
    