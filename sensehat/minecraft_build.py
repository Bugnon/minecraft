## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 5. 1. 2018
## File: minecraft_move.py

# Import modules
from sense_hat import SenseHat
from mcpi import minecraft
from mcpi import block
from time import sleep

sense = SenseHat()
mc = minecraft.Minecraft.create()

## Keep track of the player's last movement
x0, y0, z0 = mc.player.getTilePos()
dx, dy, dz = 0, 0, 0
path = []

## Record the player's path
def trace():
    global x0, y0, z0
    global dx, dy, dz
    
    x, y, z = mc.player.getTilePos()
  
    if (x!=x0 or y!=y0 or z!=z0):
        dx, dy, dz = x-x0, y-y0, z-z0  
        print(x, y, z, dx, dy, dz)
        path.append([x, y, z])
    x0, y0, z0 = x, y, z


def garden():
    print("garden")
    d=4
    x, y, z = mc.player.getTilePos()    
    mc.setBlocks(x-d, y-1, z-d, x+d, y-1, z+d, block.GRASS)
    mc.setBlocks(x-d, y, z-d, x+d, y, z+d, block.FENCE)
##    mc.setBlock(x-d, y, z, block.FENCE_GATE, 5)
##    mc.setBlock(x+d, y, z, block.FENCE_GATE, 5)
    mc.setBlock(x, y, z-d, block.FENCE_GATE)
    mc.setBlock(x, y, z+d, block.FENCE_GATE)
   
    mc.setBlocks(x-d, y+1, z-d, x+d, y+2, z+d, block.AIR)
    
    d-=1
    mc.setBlocks(x-d, y, z-d, x+d, y, z+d, block.FLOWER_YELLOW)
    
    

def house():
    d=5
    h=4
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x-d, y-1, z-d, x+d, y-1, z+d, block.STONE)
    mc.setBlocks(x-d, y+h, z-d, x+d, y+h, z+d, block.STONE)
    mc.setBlocks(x-d, y, z-d, x+d, y+h-1, z+d, block.GLASS)
    d-=1
    mc.setBlocks(x-d, y, z-d, x+d, y+h-1, z+d, block.AIR)
    
def snow():
    d=4
    x, y, z = mc.player.getTilePos()
    for i in range(x-d, x+d):
        for j in range(z-d, z+d):
            h = mc.getHeight(i, j)
            mc.setBlock(i, h, j, block.SNOW)


def tunnel():
    print('tunnel')
    global dx, dy, dz
    print(dx, dy, dz)
    d=20
    x, y, z = mc.player.getTilePos()
    if dx:
        mc.setBlocks(x, y, z, x+d*dx, y+2, z, block.AIR)
        for x in range(x, x+d*dx, 2*dx):
            mc.setBlock(x, y+1, z, block.TORCH)
    if dz:
        mc.setBlocks(x, y, z, x, y+2, z+d*dz, block.AIR)
        for z in range(z, z+d*dz, 2*dz):
            mc.setBlock(x, y+1, z, block.TORCH)       
        
while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'left':
                house()
            elif event.direction == 'right':
                tunnel()
            elif event.direction == 'up':
                garden()
            elif event.direction ==  'down':
                house()
    trace()