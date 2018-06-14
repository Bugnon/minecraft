##Author: Gabriel Furbringer
##Organisation: Gymnase du Bugnon
##Date:10.01.18

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = mc.player

t=1

def placeBlock(x,y):	
	mc.postToChat("block", t)
	mc.setBlock(x,0,y, 2)
	t=t+1

placeBlock(x,y)

