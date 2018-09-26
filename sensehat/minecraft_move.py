## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 5. 1. 2018
## File: minecraft_move.py

# Import modules
from sense_hat import SenseHat
from mcpi import minecraft
from mcpi import block
from time import sleep

## Instantiate an object
sense = SenseHat()
mc = minecraft.Minecraft.create()

## Move the player
def move(dx, dy, dz):
    x, y, z = mc.player.getTilePos()
    mc.player.setTilePos(x+dx, y+dy, z+dz)
        

x0, y0, z0 = mc.player.getTilePos()
dx, dy, dy = 0, 0, 0
path = []

## Recorde the player's path
def trace():
    global x0, y0, z0
    x, y, z = mc.player.getTilePos()
    dx, dy, dz = x-x0, y-y0, z-z0    
    if (dx or dy or dz):
        print(x, y, z, dx, dy, dz)
        path.append([x, y, z])
    x0, y0, z0 = x, y, z


## Use the joystick to move the player
while True:
    for event in sense.stick.get_events():
        if event.direction == 'left':
            move(-1, 0, 0)
        elif event.direction == 'right':
            move(1, 0, 0)
        elif event.direction == 'up':
            move(0, 0, 1)
        elif event.direction ==  'down':
           move(0, 0, -1)
        elif event.direction == 'middle':
            move(0, 1, 0)
    trace() 