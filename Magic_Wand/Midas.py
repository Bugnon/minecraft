from mcpi.minecraft import Minecraft
mc=Minecraft.create()
##xp,yp,zp=mc.player.getTilePos()
#size must be odd


def isAir(x,y,z):
    """check if block is an air block
    """
    if mc.getBlock(x,y,z) == 0:
        return True
    else:
        return False

def Midasline(x,y,z,size,blockid):
    """transform a line of non-air block into other blocks
    """
    n=size//2
    for i in range(size):
        if isAir(x,y-n+i,z) is False:
            mc.setBlock(x,y-n+i,z,blockid)
    


def Midassquare(x,y,z,size,blockid): 
    """se Midasline multiple times to change a square of blocks
    """
    n=size//2
    for i in range(size):
        Midasline(x-n+i,y,z,size,blockid)
        


def Midascube(x,y,z,size,blockid):
    """use Midassquare multiple times to change a cube of blocks
    """
    n=size//2
    for i in range(size):
        Midassquare(x,y,z-n+i,size,blockid)
    mc.postToChat("Work Done")


##Midascube(xp,yp,zp,9,41)

        
        
