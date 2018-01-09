##Author: Gabriel Fleischer
##Organisation: Gymnase du Bugnon
##Date: 09.01.18

from mcpi import minecraft

mc = minecraft.Minecraft.create()

def tunnel(width, length):
	
	"""
	Create a tunnel at the player's current position in the direction he's facing :
		- width : The width of the tunnel
		- length : The length of the tunnel
	"""
	
	px, py, pz = mc.player.getPos()
	
	angle = mc.player.getPos().getRotation()
	
	if angle >= 315 or angle <= 45 :
		for i in range(length):
			
	elif angle >= 45 and angle <= 135:
		for i in range(length):
			
	elif angle >= 135 and angle <= 225:
		for i in range(length):
			
	elif angle >= 225 and angle <= 315:
		for i in range(length):
			
tunnel(2, 15)