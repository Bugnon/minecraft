from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y ,z = mc.player.getPos()


def terrain():
    '''Cree une surface simple 15 *15'''
    mc.setBlocks(x ,y-1 , z ,x+300 ,y-300,z+300 ,3 )
    mc.setBlocks(x ,y , z ,x+300 ,y+150,z+300 ,0 )
    mc.setBlocks(x ,y-1 , z ,x+300 ,y-1,z+300 ,2 )
    mc.setBlocks(x+1 ,y , z+1 ,x+300 ,y,z+300 ,0 )
    
    
def cascade():
    mc.setBlocks(x+9 ,y , z+10 ,x+15 ,y+10,z+15 ,2 )
    mc.setBlocks(x+11 ,y+9 , z+10 ,x+13 ,y+9,z+14 ,8 )#eau
    mc.setBlocks(x+9 ,y-1 , z+7 ,x+14 ,y-1,z+9 ,0 )
    mc.setBlocks(x+9 ,y-1 , z+5 ,x+14 ,y-1,z+6 ,12 )
    mc.setBlocks(x+8 ,y-1 , z+5 ,x+7 ,y-1,z+9 ,12 )

def arbre():
    mc.setBlocks(x+6 ,y , z+4 ,x+6 ,y+4,z+4 ,17 )#tronc
    mc.setBlocks(x+4 ,y+4 , z+2 ,x+8 ,y+4,z+6 ,18 )
    mc.setBlocks(x+5 ,y+5 , z+3 ,x+7 ,y+5,z+5 ,18 )
    mc.setBlocks(x+6 ,y+6 , z+4 ,x+6 ,y+6 ,z+4 ,18 )
    
def structures_ext():
    terrain()
    cascade()
    arbre()
    
structures_ext()
