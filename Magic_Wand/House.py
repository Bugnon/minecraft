from mcpi.minecraft import Minecraft
mc=Minecraft.create()

xp,yp,zp=mc.player.getTilePos()
        
xp=xp+4
#vitre = 102
#porte = 64
#brique de pierre = 98
#planches =5
##z- north z+ south x+ east x- west
mc.setBlocks(xp+20,yp+2000,zp+20,xp-20,yp,zp-20,0)


#o={N:0,S:0,E:0,W:1}
def house(x,y,z,length, width, height):
    """Make an house in minecraft with the front at x,y,z.

x,y,z,length,width,height : int
"""
    mc.setBlocks(x,y-1,z,x+length,y+height,z+width,5) #cube en bois a "travailler"
    up = (height*2)//3
    
    #structure en pierre tout le tour
    mc.setBlocks(x,y,z,x+length,y,z,98)
    mc.setBlocks(x,y,z,x,y,z+width,98)
    mc.setBlocks(x,y,z+width,x+length,y,z+width,98)
    mc.setBlocks(x+length,y,z,x+length,y,z+width,98)
    
    #cadre en bois
    mc.setBlocks(x,y,z,x,y+height,z,17)
    mc.setBlocks(x+length,y,z+width,x+length,y+height,z+width,17)
    mc.setBlocks(x+length,y,z,x+length,y+height,z,17)
    mc.setBlocks(x,y,z+width,x,y+height,z+width,17)
    
    mc.setBlocks(x,y+up,z,x+length,y+up,z,17)
    mc.setBlocks(x+length,y+up,z,x+length,y+up,z+width,17)
    mc.setBlocks(x,y+up,z,x,y+up,z+width,17)
    mc.setBlocks(x+length,y+up,z+width,x,y+up,z+width,17)
    
    #vider interieur
    mc.setBlocks(x+1,y,z+1,x+length-1,y+up-1,z+width-1,0)




house(xp,yp,zp,7,8,7)