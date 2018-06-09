# la taille doit etre impaire

from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def isAir(x, y, z):
    """Verifie si le bloc est de l'air
    """
    if mc.getBlock(x, y, z) == 0:
        return True
    else:
        return False


def Midasline(x, y, z, size, blockid):
    """Transforme une ligne de blocs pleins en autres blocs
    """
    # distance entre le centre et les extrémités
    n = size//2
    for i in range(size):
        # si le bloc n'est pas de l'air il le transforme
        if isAir(x, y-n+i, z) is False:
            mc.setBlock(x, y-n+i, z, blockid)


def Midassquare(x, y, z, size, blockid):
    """Transforme une face de blocs pleins en autres blocs
    """
    n = size//2
    # transforme colone apres colonne une face
    for i in range(size):
        Midasline(x-n+i, y, z, size, blockid)


def Midascube(x, y, z, size, blockid):
    """Transforme une cube de blocs pleins en autres blocs
    """
    n = size//2
    # transforme face apres face le cube
    for i in range(size):
        Midassquare(x, y, z-n+i, size, blockid)
