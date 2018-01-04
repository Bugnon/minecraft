## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 4. 1. 2018
## File: tnt.py

from mcpi import minecraft

mc = minecraft.Minecraft.create()

tnt = 46
d = 10

mc.postToChat("TNT explosion")
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+d, y+d, z+d, tnt, 1)
