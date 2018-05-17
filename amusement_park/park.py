from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
from mcpi import block

mc = Minecraft.create()
mcdrawing = MinecraftDrawing(mc)

def ferry_wheel(r):
    x,y,z = mc.player.getPos()
    mcdrawing.drawCircle(x,y+r+5,z+10,r,block.IRON_BLOCK.id)
    mcdrawing.drawCircle(x,y+r+5,z+14,r,block.IRON_BLOCK.id)
    s1 = y+r+5
    socle1 = mc.getBlock(x,s1,z+9)
    while socle1 is (0):
        mc.setBlock(x,s1,z+9,block.IRON_BLOCK.id)
        s1 = s1-1
        socle1 = mc.getBlock(x,s1,z+9)
    s2 = y+r+5
    socle2 = mc.getBlock(x,s2,z+15)
    while socle2 is (0):
        mc.setBlock(x,s2,z+15,block.IRON_BLOCK.id)
        s2 = s2-1
        socle2 = mc.getBlock(x,s2,z+15)
    mc.setBlocks(x,y+r+5,z+10,x,y+r+5,z+14,block.IRON_BLOCK.id)
    mc.setBlocks(x+r-1,y+r+6,z+11,x+r+1,y+r+4,z+13,block.WOOL.id,11)
    mc.setBlock(x+r,y+r+5,z+12,block.STAIRS_WOOD.id,0)
    mc.setBlock(x+r-1,y+r+5,z+12,0)
    mc.setBlocks(x+1,y+6,z+11,x-1,y+4,z+13,block.WOOL.id,14)
    mc.setBlock(x,y+5,z+12,block.STAIRS_WOOD.id,0)
    mc.setBlock(x-1,y+5,z+12,0)
    mc.setBlocks(x+1,y+2*r+4,z+11,x-1,y+2*r+6,z+13,block.WOOL.id,13)
    mc.setBlock(x,y+2*r+5,z+12,block.STAIRS_WOOD.id,0)
    mc.setBlock(x-1,y+2*r+5,z+12,0)
    mc.setBlocks(x-r+1,y+r+4,z+11,x-r-1,y+r+6,z+13,block.WOOL.id,4)
    mc.setBlock(x-r,y+r+5,z+12,block.STAIRS_WOOD.id,0)
    mc.setBlock(x-r-1,y+r+5,z+12,0)
    mc.postToChat("A ferry wheel has been built !")
    
def bumper_cars(L,l) :
    x,y,z = mc.player.getPos()
    mc.setBlocks(x,y-1,z+10,x+l,y-1,z+10+L,block.IRON_BLOCK.id)
    mc.setBlocks(x,y+4,z+10,x+l,y,z+10+L,0)
    mc.setBlocks(x,y,z+10,x,y+4,z+10,block.FENCE.id)
    mc.setBlocks(x,y,z+10+L,x,y+4,z+10+L,block.FENCE.id)
    mc.setBlocks(x+l,y,z+10,x+l,y+4,z+10,block.FENCE.id)
    mc.setBlocks(x+l,y,z+10+L,x+l,y+4,z+10+L,block.FENCE.id)
    mc.setBlocks(x,y+5,z+10,x+l,y+5,z+10+L,block.IRON_BLOCK.id)
    mc.setBlocks(x+l/2,y,z+11,x+l/2+2,y,z+13,block.WOOL.id,11)
    mc.setBlock(x+l/2+1,y,z+12,block.STAIRS_WOOD.id,0)
    mc.setBlocks(x+l/2-2,y,z+L+9,x+l/2,y,z+L+7,block.WOOL.id,14)
    mc.setBlock(x+l/2-1,y,z+L+8,block.STAIRS_WOOD.id,1)
    mc.postToChat("A bumper cars arena has been built !")
    

    

        

                        
    



