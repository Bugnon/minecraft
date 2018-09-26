##Author: Gabriel Furbringer
##Organisation: Gymnase du Bugnon
##Date:10.01.18

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = mc.player
x, y, z = p.getPos()
mc.postToChat("wall world")

mc.setBlocks(x+30,y+30,z+30,x-30,y,z-30, 4)

mc.setBlocks(x+3,y,z+3,x-3,y+31,z-3, 0)
