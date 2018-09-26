from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
from mcpi import block

mc = Minecraft.create()
mcdrawing = MinecraftDrawing(mc)

def ferry_wheel(r, x, y, z, c):
    mcdrawing.drawCircle(x,y+r+5,z,r,block.IRON_BLOCK.id)
    mcdrawing.drawCircle(x,y+r+5,z+4,r,block.IRON_BLOCK.id)
    s1 = y+r+5
    socle1 = mc.getBlock(x,s1,z-1)
    while socle1 is (0):
        mc.setBlock(x,s1,z-1,block.IRON_BLOCK.id)
        s1 = s1-1
        socle1 = mc.getBlock(x,s1,z-1)
    s2 = y+r+5
    socle2 = mc.getBlock(x,s2,z+5)
    while socle2 is (0):
        mc.setBlock(x,s2,z+5,block.IRON_BLOCK.id)
        s2 = s2-1
        socle2 = mc.getBlock(x,s2,z+5)
    mc.setBlocks(x,y+r+5,z,x,y+r+5,z+4,block.IRON_BLOCK.id)
    mc.setBlocks(x+r-1,y+r+6,z+1,x+r+1,y+r+4,z+3,block.WOOL.id,c)
    mc.setBlock(x+r,y+r+5,z+2,block.STAIRS_WOOD.id,0)
    mc.setBlock(x+r-1,y+r+5,z+2,0)
    mc.setBlocks(x+1,y+6,z+1,x-1,y+4,z+3,block.WOOL.id,c)
    mc.setBlock(x,y+5,z+2,block.STAIRS_WOOD.id,0)
    mc.setBlock(x-1,y+5,z+2,0)
    mc.setBlocks(x+1,y+2*r+4,z+1,x-1,y+2*r+6,z+3,block.WOOL.id,c)
    mc.setBlock(x,y+2*r+5,z+2,block.STAIRS_WOOD.id,0)
    mc.setBlock(x-1,y+2*r+5,z+2,0)
    mc.setBlocks(x-r+1,y+r+4,z+1,x-r-1,y+r+6,z+3,block.WOOL.id,c)
    mc.setBlock(x-r,y+r+5,z+2,block.STAIRS_WOOD.id,0)
    mc.setBlock(x-r-1,y+r+5,z+2,0)
    mc.postToChat("A ferry wheel has been built !")
    
def bumper_cars(L, l, x, y, z, c) :
    mc.setBlocks(x,y-1,z,x+l,y-1,z+L,block.IRON_BLOCK.id)
    mc.setBlocks(x,y+4,z,x+l,y,z+L,0)
    mc.setBlocks(x,y,z,x,y+4,z,block.FENCE.id)
    mc.setBlocks(x,y,z+L,x,y+4,z+L,block.FENCE.id)
    mc.setBlocks(x+l,y,z,x+l,y+4,z,block.FENCE.id)
    mc.setBlocks(x+l,y,z+L,x+l,y+4,z+L,block.FENCE.id)
    mc.setBlocks(x,y+5,z,x+l,y+5,z+L,block.IRON_BLOCK.id)
    mc.setBlocks(x+l/2,y,z+1,x+l/2+2,y,z+3,block.WOOL.id,c)
    mc.setBlock(x+l/2+1,y,z+2,block.STAIRS_WOOD.id,0)
    mc.setBlocks(x+l/2-2,y,z+L-1,x+l/2,y,z+L-3,block.WOOL.id,c)
    mc.setBlock(x+l/2-1,y,z+L-2,block.STAIRS_WOOD.id,1)
    mc.postToChat("A bumper cars arena has been built !")
    

    

        

                        
    



