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
	
	#ground
	mc.setBlocks(px, py, pz, px+length, py, pz+width, groundBlock)
	
	#walls
	for x in range(length):
		for y in range(height):
			for z in range(width):
				if x == 0 or x == length-1 or z == 0 or z == width-1:
					mc.setBlock(px+x, py+y, pz+z, wallBlock)
	#door
	mc.setBlocks(int(px + length/2), py+1, pz, int(px + length/2), py+2, pz, 0)
	
	#window
	mc.setBlock(px, py+1, int(pz+width/2), 102)
	
	#roof
	mc.setBlocks(px+1, py+height, pz+1, px+length-1, py+height, pz+width-1, roofBlock)
	
house(5, 5, 7, 5, 43, 45)