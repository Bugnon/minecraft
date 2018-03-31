##Author: Gabriel Furbringer
##Organisation: Gymnase du Bugnon
##Date:10.01.18

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = mc.player
x, y, z = p.getPos()
mc.postToChat("ready")
#initialisation du monde 

p.setPos(-17, 100,0)
mc.setBlocks(-2,-1,-2,18, 100,18, 1)
mc.setBlocks(-1,0,-1, 17, 100, 17, 0)
mc.setBlocks(0,-1,0, 16, -1, 16, 15)



