##Author: Gabriel Fleischer
##Organisation: Gymnase du Bugnon
##Date: 09.01.18

from mcpi import minecraft

import math    

mc = minecraft.Minecraft.create()

def house(length, height, width, wallBlock, secondaryWall, groundBlock, roofBlock):
    """
    Create a house at the player's current position with the given arguments :
        - length : the length of the house
        - height : the height of the house (Without the roof
        - width : the width of the house
        - wallBlock : The block used to make the wall
        - groundBlock : The block used to make the ground
        - roofBlock : The block used to make the roof
    """
    
    px, py, pz = mc.player.getPos()
    
    py=py-1
    px=px - float(length)/2
    pz=pz-2
    #ground
    mc.setBlocks(px, py, pz, px+length-1, py, pz+width-1, groundBlock)
    
    #walls
    for x in range(length):
        for y in range(height + 1):
            for z in range(width):
                if x == 0:
                    if z == 0 or z == width - 1:
                        mc.setBlock(px+x, py+y, pz+z, secondaryWall)
                    else:
                        mc.setBlock(px+x, py+y, pz+z, wallBlock)
                elif x == length-1:
                    if z == 0 or z == width-1:
                        mc.setBlock(px+x, py+y, pz+z, secondaryWall)
                    else:
                        mc.setBlock(px+x, py+y, pz+z, wallBlock)
                elif z == 0 or z == width-1:
                    mc.setBlock(px+x, py+y, pz+z, wallBlock)
    #door
    mc.setBlock(px + math.floor(length/4), py+1, pz, 64, 3)
    mc.setBlock(px + math.floor(length/4), py+2, pz, 64, 11)
    
    #windows
    mc.setBlocks(px, py+2, pz+math.floor(width/2)-1, px, py+2, pz+math.floor(width/2)+1, 102)
    
    mc.setBlock(px + math.floor(length/4*3), py+2, pz, 102)
    
    #roof
    for i in range(width+2):
        h = 0
        for j in range(length+2):
            x=j-1
            z=i-1
            if x > float(length)/2:
                h=h-1
            if x < float(length)/2:
                h=h+1
            if (z == 0 or z == width-1) and (x >= 0 and x <= length-1):
                if x == 0 or x == length-1:
                    mc.setBlocks(px+x, py+height, pz+z, px+x, py+height+h-1, pz+z, secondaryWall)
                else:
                    mc.setBlocks(px+x, py+height, pz+z, px+x, py+height+h-1, pz+z, wallBlock)

            mc.setBlock(px+x, py+height+h-1, pz+z, roofBlock)
    
house(5, 3, 7, 5, 17, 43, 45)