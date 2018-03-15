# Authors:Albert and Ludovic
# Date: 15.01.2018

# Affiliation : Gymnase du Bugnon
# Year 2017-2018
# Classe : OC-Informatique
# =======================================

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import math
xp,yp,zp=mc.player.getTilePos()
        
xp=xp+4
#vitre = 102
#porte = 64
#brique de pierre = 98
#planches =5
##z- north z+ south x+ east x- west
mc.setBlocks(xp+20,yp+2000,zp+20,xp-20,yp,zp-20,0)


def One_range_roof(x1,y):
    mc.setBlocks(x,y)

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
    mc.setBlocks(x,y+up+1,z,x+length,y+height,z+width,0)
    #porte
    mc.setBlock(x, y, z+width//4+1, 64, 3)
    mc.setBlock(x , y+1, z+width//4+1, 64, 11)    

    #fenetre
     
    mc.setBlock(x+length//2,y+up//2,z,102)
    mc.setBlock(x+length,y+up//2,z+width//2,102)
    mc.setBlock(x+length//2,y+up//2,z+width,102)
    mc.setBlock(x,y+up//2,z+width//2,102)
    
    #toit
    for b in range(height-up):
        mc.setBlocks(x+b-1,y+up+1+b,z+b-1,x+length-b+1,y+up+1+b,z+1+width-b,98)



house(xp,yp,zp,7,7,7)
