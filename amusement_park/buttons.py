##Author: Raphael Holzer
##Organisation: Gymnase du Bugnon
##Date: 14. 1. 2018

import RPi.GPIO as GPIO
from time import sleep

## configure the list of input channels
button_channels = [14, 15, 18]

GPIO.setmode(GPIO.BCM)

def button_callback(channel):
    """Print the channel number to the console."""
    print("callback function for button ", channel)

## setup all channels as inputs with a pull-up resistor. When pushing a
## button the state goes from HIGH to LOW (falling edge)
for channel in button_channels:
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(channel, GPIO.FALLING, bouncetime=200)
    GPIO.add_event_callback(channel, button_callback)

## Testing the module
if __name__ == "__main__" :
    while True:
        sleep(1)
