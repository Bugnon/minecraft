from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x, y, z = mc.player.getPos()


mc.setBlocks(x-300, y, -300, x+300, y, z+300, 2)
mc.setBlocks(x-300, y+1, z-300, x+300, y+300, z+300,0)

def arbre(a,b,c):
    mc.setBlocks(x+a ,y , z+c ,x+a ,y+b,z+c ,17 )
    mc.setBlocks(x+(a-2) ,y+b , z+(c-2) ,x+(a+2) ,y+b,z+(c+2) ,18 )
    mc.setBlocks(x+(a-1) ,y+(b+1) , z+(c-1) ,x+(a+1) ,y+(b+1),z+(c+1) ,18 )
    mc.setBlocks(x+a ,y+(b+2) , z+c ,x+a ,y+(b+2) ,z+c ,18 )
    
    
arbre(6,4,4)
arbre(10,3,4)
arbre(20,4,8)
arbre(3,8,9)
arbre(5,9,9)
arbre(7,7,7)
arbre(3,9,67)
arbre(50,10,34)
arbre(65,3,56)
arbre(34,13,90)
arbre(90,7,45)
arbre(27,8,74)
arbre(78,4,5)
