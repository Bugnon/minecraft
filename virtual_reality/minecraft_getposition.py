from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
	angle = mc.player.getRotation(30)
	pitch = mc.player.getPitch(30)
	mc.postToChat(str(angle)+":"+str(pitch))
