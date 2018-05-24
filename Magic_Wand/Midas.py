
#la taille doit ertre impaire


def isAir(x, y, z):
    """verifie si le bloc est de l'air
    """
    if mc.getBlock(x, y, z) == 0:
        return True
    else:
        return False

def Midasline(x, y, z, size, blockid):
    """Transforme une ligne de blocs pleins en autres blocs
    """
    n = size//2
    for i in range(size):
        if isAir(x, y-n+i, z) is False:
            mc.setBlock(x, y-n+i, z, blockid)
    


def Midassquare(x, y, z, size, blockid): 
    """Transforme une face de blocs pleins en autres blocs
    """
    n = size//2
    for i in range(size):
        Midasline(x-n+i, y, z, size, blockid)
        


def Midascube(x, y, z, size, blockid):
    """Transforme une cube de blocs pleins en autres blocs
    """
    n = size//2
    for i in range(size):
        Midassquare(x, y, z-n+i, size, blockid)


