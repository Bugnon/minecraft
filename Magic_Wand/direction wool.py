from mcpi.minecraft import Minecraft
mc=Minecraft.create()
#z- north z+ south x+ east x- west


def isWool(pos):
    if mc.getBlock(pos) == 35:
        return True
    else:
        return False


def removeWool(a,b,c):
    mc.setBlock(a,0)
    mc.setBlock(b,0)
    mc.setBlock(c,0)
    
   
def direction():
    mc.postToChat("Place 3 wool blocks like an arrow to choose direction")
    while True:
        xp,yp,zp=mc.player.getTilePos()
        n=(xp,yp,zp-1)
        s=(xp,yp,zp+1)
        w=(xp-1,yp,zp)
        e=(xp+1,yp,zp)
        if isWool(s) is True and isWool(e) is True and isWool(w) is True and isWool(n) is False:
            direction="South"
            mc.postToChat("Direction: South")
            removeWool(s,e,w)
            return direction
        if isWool(n) is True and isWool(e) is True and isWool(w) is True and isWool(s) is False:
            direction="North"
            mc.postToChat("Direction: North")
            removeWool(n,e,w)
            return direction
        if isWool(n) is True and isWool(s) is True and isWool(w) is True and isWool(e) is False:
            direction="West"
            mc.postToChat("Direction: West")
            removeWool(n,s,w)
            return direction
        if isWool(n) is True and isWool(e) is True and isWool(s) is True and isWool(w) is False:
            direction="East"
            mc.postToChat("Direction: East")
            removeWool(n,s,e)
            return direction
        

direction()
        
            
        
        
    
    
    
    
