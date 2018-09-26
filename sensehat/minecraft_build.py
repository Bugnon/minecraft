## Author: Raphael Holzer
## Organisation: Gymnase du Bugnon
## Date: 5. 1. 2018
## File: minecraft_build.py

## This project uses the Sense HAT joystick to select among four structures
## to create within Minecraft (tunnel, house, garden, snow).

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


def garden(d=4):
    """Create a garden with yellow flowers."""
    print("garden")
    mc.postToChat('Create garden')
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
    

def house(d=5, h=4):
    """Build a house around the player."""
    mc.postToChat('Create house')
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x-d, y-1, z-d, x+d, y-1, z+d, block.STONE)
    mc.setBlocks(x-d, y+h, z-d, x+d, y+h, z+d, block.STONE)
    mc.setBlocks(x-d, y, z-d, x+d, y+h-1, z+d, block.GLASS)
    d-=1
    mc.setBlocks(x-d, y, z-d, x+d, y+h-1, z+d, block.AIR)


def snow(d=2):
    """Put snow on the ground around the player."""
    x, y, z = mc.player.getTilePos()
    for i in range(x-d, x+d):
        for j in range(z-d, z+d):
            h = mc.getHeight(i, j)
            mc.setBlock(i, h, j, block.SNOW)

def tunnel(d=20):
    """Create a tunnel in the direction of the last player movement."""
    mc.postToChat('Tunnel tunnel')
    global dx, dy, dz
    print(dx, dy, dz)
    x, y, z = mc.player.getTilePos()
    if dx:
        mc.setBlocks(x, y, z, x+d*dx, y+2, z, block.AIR)
        for x in range(x, x+d*dx, 2*dx):
            mc.setBlock(x, y+1, z, block.TORCH)
    if dz:
        mc.setBlocks(x, y, z, x, y+2, z+d*dz, block.AIR)
        for z in range(z, z+d*dz, 2*dz):
            mc.setBlock(x, y+1, z, block.TORCH)       
    
def tower(x, y, z):
    """Create a tower at position."""
    (id, data) = mc.getBlockWithData(x, y, z)
    mc.setBlocks(x, y, z, x, y+10, z, id, data)
    
    
## Main loop. Read joystick and take action.    
while True:
    trace()
    
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'left':
                house()
            elif event.direction == 'right':
                tunnel()
            elif event.direction == 'up':
                garden()
            elif event.direction ==  'down':
                snow()
  
    for hit in mc.events.pollBlockHits():
        x, y, z = hit.pos
        print(hit.pos)
        print(mc.getBlockWithData(x, y, z))
        tower(x, y, z)
        print(mc.getBlockWithData(hit.pos))
