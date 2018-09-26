## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 5. 1. 2018
## File: rotate.py

## Import modules
from sense_hat import SenseHat

sense = SenseHat()

## Display the letter J
sense.show_letter('J')

## Turn the displayed text according to orientation
while True:
    acc = sense.get_accelerometer_raw()
    x = round(acc['x'], 0)
    y = round(acc['y'], 0)
    z = round(acc['z'], 0)
    
    print('x={0}, y={1}, z={2}'.format(x, y, z))
    
    if  y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    elif x == 1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(90)
        