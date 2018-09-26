## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 4. 1. 2018
## File: trace.py

from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

flower = 38
grass = 2

while True:
    x, y, z = mc.player.getPos() # player position
    block_beneath = mc.getBlock(x, y-1, z) # block ID
    sleep(0.1)
    
    if block_beneath == grass:
        mc.setBlock(x, y, z, flower)
    else:
        mc.setBlock(x, y-1, z, grass)
       
