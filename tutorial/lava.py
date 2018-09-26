## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 4. 1. 2018
## File: lava.py

from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

lava = 10
water = 8
air = 0

mc.postToChat("Lava flow")
x, y, z = mc.player.getPos()

mc.setBlock(x+3, y+3, z, lava)
sleep(20)
mc.setBlock(x+3, y+5, z, water)
sleep(4)
mc.setBlock(x+3, y+5, z, air)

