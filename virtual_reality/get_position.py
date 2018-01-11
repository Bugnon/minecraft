from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
mc.postToChat("Get position")
while True:
	pos = mc.player.getPos()
	print(pos)
	sleep(1)
