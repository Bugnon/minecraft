##Author: Gabriel Fleischer
##Organisation: Gymnase du Bugnon
##Date: 09.01.18

from mcpi import minecraft

mc = minecraft.Minecraft.create()

def house(length, height, width, wallBlock, groundBlock, roofBlock):
	"""
	Create a house at the player's current position with the given arguments :
		- length : the length of the house
		- height : the height of the house (Without the roof
		- width : the width of the house
		- wallBlock : The block used to make the wall
		- groundBlock : The block used to make the ground
		- roofBlock : The block used to make the roof
	"""
	
	px, py, pz = mc.player.getPos()
	
	py=py-1
	px=px - float(length)/2
	pz=pz-2
	#ground
	mc.setBlocks(px, py, pz, px+length-1, py, pz+width, groundBlock)
	
	#walls
	for x in range(length):
		for y in range(height):
			for z in range(width):
				if x == 0 or x == length-1 or z == 0 or z == width-1:
					mc.setBlock(px+x, py+y, pz+z, wallBlock)
	#door
	mc.setBlock(int(px + float(length)/2), py+1, pz, 64, 0)
	mc.setBlock(int(px + float(length)/2), py+2, pz, 64, 0)
	
	#window
	mc.setBlock(px, py+2, int(pz+float(width)/2), 102)
	
	#roof
	for i in range(width+2):
		h =0
		for j in range(length+2):
			x=j-1
			z=i-1	
			if x > float(length)/2:
				h=h-1
			if x < float(length)/2:
				h=h+1
			if x >=1 and x <= length+1:
				mc.setBlocks(px+x, py+height+1, pz+z, px+x, py+height+h, pz+z, wallBlock)
			
			mc.setBlock(px+x, py+height+h, pz+z, roofBlock)
	
house(5, 5, 7, 5, 43, 45)