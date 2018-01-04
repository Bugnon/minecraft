##Author: Raphael Holzer
##Organisation: Gymnase du Bugnon
##Date: 4. 1. 2018

from mcpi import minecraft

mc = minecraft.Minecraft.create()

def placeBlock(id):
    '''Place block (id) in front and move one position backwards.'''    
    material = ['air', 'rock', 'grass', 'soil'][id]
    mc.postToChat("Place block:   "+material)
 
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1, y, z, id)
    mc.player.setPos(x-1, y, z)

while True:
    id = int(input("1=rock, 2=grass, 3=soil: "))
    placeBlock(id)
    
