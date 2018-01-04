##Author: Raphael Holzer
##Organisation: Gymnase du Bugnon
##Date: 4. 1. 2018


from mcpi import minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Get position")
x, y, z = mc.player.getPos()

d=3
mc.setBlocks(x-d, y-1, z-d, x+d, y+1, z+d, 1)

d-=1
mc.setBlocks(x-d, y, z-d, x+d, y+1, z+d, 0)

