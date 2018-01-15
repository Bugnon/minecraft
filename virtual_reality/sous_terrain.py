from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y ,z = mc.player.getPos()
    

def make_gallery():
    mc.setBlocks(x-1 ,y-10 , z-1 ,x+11 ,y-15,z+11 ,98 )#blocdebase
    mc.setBlocks(x ,y-11 , z,x+10, y-14,z+10 ,0 )#vide
    mc.setBlocks(x ,y , z,x ,y-11,z ,0)#entree

def make_bassine():
    mc.setBlocks(x+7 ,y-14 , z,x+10 ,y-14 ,z+10 ,14 )#bloc base bassine
    mc.setBlocks(x+8 ,y-14 , z,x+10 ,y-14 ,z+4 ,0 )#trou
    mc.setBlocks(x+8 ,y-14 , z+6,x+10 ,y-14 ,z+10 ,0 )#trou
    mc.setBlock(x+9 ,y-14 , z+7, 8 )#eau
    mc.setBlock(x+9 ,y-14 , z+9, 8 )#eau
    mc.setBlock(x+9 ,y-14 , z+3, 10 )#lave
    mc.setBlock(x+9 ,y-14 , z, 10 )#lave

def torches():
    mc.setBlock(x+9 ,y-12 , z, 50 )
    mc.setBlock(x+9 ,y-12 , z+10, 50 )
    mc.setBlock(x+1 ,y-12 , z+10, 50 )
    

    

def sous_terrains():
    make_gallery()
    make_bassine()
    torches()
    
sous_terrains()
