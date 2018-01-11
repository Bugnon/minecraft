
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello World")
mc.postToChat("Moving Forward 5 blocks")

x, y, z  = mc.player.getPos()
mc.player.setPos(x+5, y, z)

