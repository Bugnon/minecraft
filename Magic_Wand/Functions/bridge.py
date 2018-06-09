def isvoid(x, y, z):
    """Verifie si le bloc est de l'air ou de l'eau"""
    b = mc.getBlock(x, y, z)
    if b == 0 or b == 8 or b == 9:
        return True
    else:
        return False


def lengthbridge(x, y, z):
    """Retourne la longueur du pont"""
    l = 0
    # si l'un des deux blocs est vide le pont doit continuer
    # le bloc doit etre en-dessous du joueur
    if isvoid(x, y-1, z-1) is True or isvoid(x+1, y-1, z-1) is True:
        i = 1
        while isvoid(x, y-1, z-i) is True or isvoid(x+1, y-1, z-i) is True:
            i += 1
            # si les deux blocs sont pleins le pont se termine
            if isvoid(x, y-1, z-i) is False and isvoid(x+1, y-1, z-i) is False:
                # la longueur sous le pont
                l += i-1
        return l
    else:
        # si le joueur ne se trouve pas a coté du vide
        # la fonction est appelée un bloc plus au nord
        return lengthbridge(x, y, z-1)


def first_stage(x, y, z, l, stairs, block):
    """Construit le premier étage du pont"""
    # deux escaliers décoratifs à l'avant du pont
    mc.setBlock(x-1, y+1, z+2, stairs, 3)
    mc.setBlock(x+2, y+1, z+2, stairs, 3)
    # escaliers sur lesquels le joueur marche
    mc.setBlocks(x, y+1, z+1, x+1, y+1, z+1, stairs, 3)
    # deux blocs décoratifs sur le coté du pont
    mc.setBlock(x-1, y+1, z+1, block)
    mc.setBlock(x+2, y+1, z+1, block)
    # escaliers à l'envers derrière les escaliers précédents
    mc.setBlocks(x-1, y+1, z, x+2, y+1, z, stairs, 6)
    # deux escaliers décoratifs à l'arrière du pont
    mc.setBlock(x-1, y+1, z-l-1, stairs, 2)
    mc.setBlock(x+2, y+1, z-l-1, stairs, 2)
    # escaliers sur lesquels le joueur marche
    mc.setBlocks(x, y+1, z-l, x+1, y+1, z-l, stairs, 2)
    # escaliers à l'envers devant les escaliers précédents
    mc.setBlocks(x-1, y+1, z-l+1, x+2, y+1, z-l+1, stairs, 7)
    # deux blocs décoratifs sur le coté du pont
    mc.setBlock(x-1, y+1, z-l, block)
    mc.setBlock(x+2, y+1, z-l, block)


def second_stage(x, y, z, l, stairs, block):
    """Construit le deuxième étage du pont"""
    # deux escaliers décoratifs sur le coté du pont
    mc.setBlock(x-1, y+2, z+1, stairs, 3)
    mc.setBlock(x+2, y+2, z+1, stairs, 3)
    # escaliers sur lesquels le joueur marche
    mc.setBlocks(x, y+2, z, x+1, y+2, z, stairs, 3)
    # deux blocs décoratifs sur le coté du pont
    mc.setBlock(x-1, y+2, z, block)
    mc.setBlock(x+2, y+2, z, block)
    # deux escaliers décoratifs à l'envers sur le coté du pont
    mc.setBlock(x-1, y+2, z-1, stairs, 6)
    mc.setBlock(x+2, y+2, z-1, stairs, 6)
    # deux escaliers décoratifs sur le coté du pont
    mc.setBlock(x-1, y+2, z-l, stairs, 2)
    mc.setBlock(x+2, y+2, z-l, stairs, 2)
    # deux blocs décoratifs sur le coté du pont
    mc.setBlock(x-1, y+2, z-l+1, block)
    mc.setBlock(x+2, y+2, z-l+1, block)
    # deux escaliers décoratifs à l'envers sur le coté du pont
    mc.setBlock(x-1, y+2, z-l+2, stairs, 7)
    mc.setBlock(x+2, y+2, z-l+2, stairs, 7)
    # escaliers sur lesquels le joueur marche
    mc.setBlocks(x, y+2, z-l+1, x+1, y+2, z-l+1, stairs, 2)
    # partie principale du pont
    mc.setBlocks(x, y+2, z-1, x+1, y+2, z-l+2, block)
    # escaliers décoratifs à l'envers
    mc.setBlocks(x-1, y+2, z-2, x-1, y+2, z-l+3, stairs, 4)
    mc.setBlocks(x+2, y+2, z-2, x+2, y+2, z-l+3, stairs, 5)


def bridge(x, y, z, blocktype):
    """Construit le pont"""
    l = lengthbridge(x, y, z)
    # minimum 2 escaliers, 1 bloc et 2 escaliers
    if l > 5:
        # attribue un id correspondant pour les escaliers et blocs
        # pour la pierre et le bois
        if blocktype is "COBBLESTONE":
            stairs = 67
            block = 4
        if blocktype is "WOOD":
            stairs = 53
            block = 5
        i = 1
        while True:
            # Trouve le point de départ du pont
            # si le joueur est sur un terrain plat
            if isvoid(x, y-1, z-i) is True or isvoid(x+1, y-1, z-i) is True:
                xs, ys, zs = x, y-1, z-i
                break
            else:
                i += 1
        # 1er étage
        first_stage(xs, ys, zs, l, stairs, block)
        # 2nd étage
        second_stage(xs, ys, zs, l, stairs, block)
        # 3eme étage
        # rembarde de blocs
        mc.setBlocks(xs-1, ys+3, zs, xs-1, ys+3, zs-l+1, block)
        mc.setBlocks(xs+2, ys+3, zs, xs+2, ys+3, zs-l+1, block)


from mcpi import minecraft
mc = minecraft.Minecraft.create()
x,y,z = mc.player.getTilePos()

bridge(x,y,z,"WOOD")