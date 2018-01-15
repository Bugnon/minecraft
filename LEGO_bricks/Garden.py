##Author: Gabriel Furbringer
##Organisation: Gymnase du Bugnon
##Date:10.01.18

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = mc.player
x, y, z = p.getPos()
mc.postToChat("Garden")

def garden(l,e):
	"""
	Create a part of the garden, the center square and the outer walls. The outer walls' dimention is l x e. 
	"""
		#Empty the place
        mc.setBlocks(x-l, y,z-e,x+l,y+10,z+e, 0)
		#Place tall_grass inside the square
        mc.setBlocks(x-l+1,y,z+e,x+l-1,y,z+e-1,31,1)
        mc.setBlocks(x-l+1,y,z-e,x+l-1,y,z-e+1,31,1)
        mc.setBlocks(x-l+1,y,z-e,x-l+1,y,z+e-1,31,1)
        mc.setBlocks(x+l-1,y,z-e,x+l-1,y,z+e-1,31,1)
		#Place the inside walls
        mc.setBlocks(x-2,y,z+2,x+2,y+1,z+2,18)
        mc.setBlocks(x-2,y,z-2,x+2,y+1,z-2,18)
        mc.setBlocks(x-2,y,z-2,x-2,y+1,z+2,18)
        mc.setBlocks(x+2,y,z-2,x+2,y+1,z+2,18)
		#place grass floor
        mc.setBlocks(x-l,y-1,z-e,x+l,y-1,z+e, 2)
		
		#Place the outside walls
        mc.setBlocks(x-l,y,z+e,x+l,y+2,z+e,18)
        mc.setBlocks(x-l,y,z-e,x+l,y+2,z-e,18)
        mc.setBlocks(x-l,y,z-e,x-l,y+2,z+e,18)
        mc.setBlocks(x+l,y,z-e,x+l,y+2,z+e,18)
		
		#Makes the wooden floor
        mc.setBlocks(x+l,y,z,x-l,y+1,z, 0)
        mc.setBlocks(x,y,z+e,x,y+1,z-e,0)
        mc.setBlocks(x+l,y-1,z,x-l,y-1,z, 5 )
        mc.setBlocks(x,y-1,z+e,x,y-1,z-e,5)

garden(6,6)
garden(4,4)
garden(2,2)