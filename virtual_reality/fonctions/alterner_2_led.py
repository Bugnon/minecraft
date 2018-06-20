
import RPi.GPIO as gpio
import time

led1 = 14
led2 = 15
led = led1
button = 18
t= 0.1
gpio.setmode(gpio.BCM)
gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_UP)

while True:
	gpio.output(led, gpio.HIGH)
	time.sleep(t)
	gpio.output(led, gpio.LOW)
	time.sleep(t)

	if gpio.input(button):
		led = led1
	else:
		led = led2


