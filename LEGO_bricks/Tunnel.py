##Author: Gabriel Fleischer
##Organisation: Gymnase du Bugnon
##Date: 09.01.18

from mcpi import minecraft

mc = minecraft.Minecraft.create()

def tunnel(width, height, length):
	
	"""
	Create a tunnel at the player's current position in the direction he's facing :
		- width : The width of the tunnel (from the center to the side)
		- height : The height of the tunnel
		- length : The length of the tunnel
	"""
	
	px, py, pz = mc.player.getPos()
	
	angle = mc.player.getRotation()
	#Length
	for i in range(length):
		#width
		for j in range(width*2+1):
			#Height
			for y in range(height):
				if angle >= 315 or angle <= 45:
					setBlock(px+i, py+y, pz+j-width, 0)
				elif angle >= 45 and angle <= 135:
					setBlock(px+j-width, py+y, pz+i, 0)
				elif angle >= 135 and angle <= 225:
					setBlock(px-i, py+y, pz+j-width, 0)
				elif angle >= 225 and angle <= 315:
					setBlock(px+j-width, py+y, pz-i, 0)
tunnel(2, 6, 15)