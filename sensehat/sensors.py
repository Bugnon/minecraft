## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 5. 1. 2018
## File: sensors.py

## Import modules
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

## Print pressure, temperature and humidity
pressure = sense.get_pressure()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

print('pressure=', pressure)
print('temperature=', temperature)
print('humidity=', humidity)
print()

## Print pitch, roll and yaw
while True:
    o = sense.get_orientation()
    pitch = int(o['pitch'])
    roll = int(o['roll'])
    yaw = int(o['yaw'])
    print('pitch={:4}, roll={:4}, yaw={:4}'.format(pitch, roll, yaw))
    sleep(0.5)
    
