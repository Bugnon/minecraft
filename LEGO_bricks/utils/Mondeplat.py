##Author: Gabriel Furbringer
##Organisation: Gymnase du Bugnon
##Date:10.01.18

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = mc.player
x, y, z = p.getPos()
mc.postToChat("pretty world")

mc.setBlocks(256,0,256,-256,256,-256,0)
mc.setBlocks256, 0, 256, -256, 0, -256, 2)
