from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
from mcpi import block

mc = Minecraft.create()
mcdrawing = MinecraftDrawing(mc)


def ferry_wheel(r):
    x,y,z = mc.player.getPos()
    mcdrawing.drawCircle(x,y+r+5,z+10,r,block.IRON_BLOCK.id)
    mc.setBlocks(x,y+r+5,z+9,x,y,z+9,block.IRON_BLOCK.id)
    s1 = y-1
    socle1 = mc.getBlock(x,s1,z+9)
    while socle1 is (0):
        mc.setBlock(x,s1,z+9,block.IRON_BLOCK.id)
        s1 = s1-1
        socle1 = mc.getBlock(x,s1,z+9)
    mc.setBlocks(x,y+r+5,z+11,x,y,z+11,block.IRON_BLOCK.id)
    s2 = y-1
    socle2 = mc.getBlock(x,s2,z+11)
    while socle2 is (0):
        mc.setBlock(x,s2,z+11,block.IRON_BLOCK.id)
        s2 = s2-1
        socle2 = mc.getBlock(x,s2,z+11)
    mc.setBlock(x,y+r+5,z+10,block.IRON_BLOCK.id)
    
def bumper_cars(L,l) :
    x,y,z = mc.player.getPos()
    mc.setBlocks(x,y-1,z+10,x+l,y-1,z+10+L,block.IRON_BLOCK.id)
    mc.setBlocks(x,y+4,z+10,x+l,y,z+10+L,0)
    mc.setBlocks(x,y,z+10,x,y+4,z+10,block.FENCE.id)
    mc.setBlocks(x,y,z+10+L,x,y+4,z+10+L,block.FENCE.id)
    mc.setBlocks(x+l,y,z+10,x+l,y+4,z+10,block.FENCE.id)
    mc.setBlocks(x+l,y,z+10+L,x+l,y+4,z+10+L,block.FENCE.id)
    mc.setBlocks(x,y+5,z+10,x+l,y+5,z+10+L,block.IRON_BLOCK.id)
    

        

                        
    



