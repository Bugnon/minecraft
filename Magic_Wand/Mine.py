from mcpi.minecraft import Minecraft
mc=Minecraft.create()
xp,yp,zp=mc.player.getTilePos()

def airx(x,y):
    """Set air on x axis
    """
    mc.setBlocks(x,y,zp,x,y+2,zp,0)


def airz(z,y):
    """ Set air on z axis
    """
    mc.setBlocks(xp,y,z,xp,y+2,z,0)


def isAirx(x,y):
    """ Check air on x axis
    """
    if mc.getBlock(x,y,zp) == 0:
        return True
    else:
        return False

def isAirz(z,y):
    """Check air on z axis
    """
    if mc.getBlock(xp,y,z) == 0: #check air on z axis
        return True
    else:
        return False
    
    
    

def Mine(x,y,z,direction,size):
    """Create a Mine descending with given size
    """
    if size >= yp+50: # in order not to reach bedrock
        mc.postToChat("it is too big")
    if direction == "North":
        for i in range(size):
            airz(z-(i+1),y-(i+1))
            mc.setBlock(x,y-(i+2),z-(i+1),67,2) #stairs
        mc.setBlock(x,y-1,z,67,2)
        for i in range(size):
            if isAirz(z-(1+i),y-(1+i)) is False: #check if gravel or sand fell down
                Mine(x,y,z,direction,size)
        for i in range(size//5):
            mc.setBlock(x,y-(1+i)*5,z-(1+i)*5,50,2) #torches must be after the isAir to prevent bug
        mc.postToChat("Work Done")
    if direction == "South":
        for i in range(size):
            airz(z+(i+1),y-(i+1))
            mc.setBlock(x,y-(i+2),z+(i+1),67,3)
        mc.setBlock(x,y-1,z,67,3)
        for i in range(size):
            if isAirz(z+(1+i),y-(1+i)) is False:
                Mine(x,y,z,direction,size)
        for i in range(size//5):
            mc.setBlock(x,y-(1+i)*5,z+(1+i)*5,50,1) 
        mc.postToChat("Work Done")
    if direction == "East":
        for i in range(size):
            airx(x+(i+1),y-(i+1))
            mc.setBlock(x+(i+1),y-(i+2),z,67,1)
        mc.setBlock(x,y-1,z,67,1)
        for i in range(size):
            if isAirx(x-(1+i),y-(1+i)) is False:
                Mine(x,y,z,direction,size)
        for i in range(size//5):
            mc.setBlock(x+(1+i)*5,y-(1+i)*5,z,50,4) 
        mc.postToChat("Work Done")
    if direction == "West":
        for i in range(size):
            airx(x-(i+1),y-(i+1))
            mc.setBlock(x-(i+1),y-(i+2),z,67,0)
            mc.setBlock(x,y-1,z,67,0)
        for i in range(size):
            if isAirx(x-(1+i),y-(1+i)) is False:
                Mine(x,y,z,direction,size)
        for i in range(size//5):
            mc.setBlock(x-(1+i)*5,y-(1+i)*5,z,50,3)
        mc.postToChat("Work Done")


Mine(xp,yp,zp,"North",23) 


            
    
            
        
            
            
            
        
