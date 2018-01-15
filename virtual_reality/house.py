from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x, y, z = mc.player.getPos()
planches = block.WOOD_PLANKS

mc.setBlocks(x+2, y-1, z+2, x+12, y+10, z+12, planches)
mc.setBlocks(x+3, y, z+3, x+11, y+9, z+11, 0)
mc.setBlocks(x+4,y,z+2,x+5,y+1,z+2, 64)






 
