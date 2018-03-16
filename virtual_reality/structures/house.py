from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x, y, z = mc.player.getPos()
planches = block.WOOD_PLANKS

def limites_maison():
    mc.setBlocks(x+2, y-1, z+2, x+12, y+10, z+12, planches)
    mc.setBlocks(x+3, y, z+3, x+11, y+9, z+11, 0)

def murs_intérieurs ():
    mc.setBlocks(x+2, y, z+7, x+12, y+5, z+7, planches)
    mc.setBlocks(x+7, y, z+7, x+7, y+5, z+12, planches)

def portes():
    mc.setBlocks(x+4,y,z+2,x+5,y+1,z+2, 0)
    mc.setBlocks(x+4, y, z+7, x+4, y+1, z+7, 0)
    mc.setBlocks(x+9, y, z+7, x+9, y+1, z+7, 0)

def passage_niveau():
    mc.setBlocks(x+2, y+6, z+2, x+12, y+6, z+12, planches)
    mc.setBlocks(x+3, y+6, z+9, x+3, y+6, z+11, 0)

def vitres():
    mc.setBlocks(x+2, y+1, z+4, x+2, y+1, z+5, 20)
    mc.setBlocks(x+12, y+1, z+4, x+12, y+1, z+5, 20)
    mc.setBlocks(x+3, y+8, z+2, x+11, y+8, z+2, 20)
    mc.setBlocks(x+2, y+8, z+3, x+2, y+8, z+11, 20)
    mc.setBlocks(x+12, y+8, z+3, x+12, y+8, z+11, 20)
    mc.setBlocks(x+3, y+8, z+12, x+11, y+8, z+12, 20)

def toit():
    mc.setBlocks(x+3, y+10, z+3, x+11, y+10, z+11, 0)
    mc.setBlocks(x+2, y+11, z+2, x+12, y+11, z+12, 45)
    mc.setBlocks(x+3, y+11, z+3, x+11, y+11, z+11, 0)
    mc.setBlocks(x+3, y+12, z+3, x+11, y+12, z+11, 45)
    mc.setBlocks(x+4, y+12, z+4, x+10, y+12, z+10, 0)
    mc.setBlocks(x+4, y+13, z+4, x+10, y+13, z+10, 45)
    mc.setBlocks(x+5, y+13, z+5, x+9, y+13, z+9, 0)
    mc.setBlocks(x+5, y+14, z+5, x+9, y+14, z+9, 45)
    mc.setBlocks(x+6, y+14, z+6, x+8, y+14, z+8, 0)
    mc.setBlocks(x+6, y+15, z+6, x+8, y+15, z+8, 45)
    mc.setBlocks(x+7, y+15, z+7, x+7, y+15, z+7, 45)
 
def torches():
    mc.setBlocks(x+10, y+1, z+8, x+10, y+1, z+8, 50)
    mc.setBlocks(x+5, y+1, z+8, x+5, y+1, z+8, 50)

def create_house():
    limites_maison()
    murs_intérieurs()
    portes()
    passage_niveau()
    vitres()
    toit()
    torches()

create_house()



    
 
    