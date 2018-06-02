import time


def airx(x, y):
    """Transforme les blocs en air sur l'axe x
    """
    mc.setBlocks(x, y, zp, x, y+2, zp, 0)


def airz(z, y):
    """Transforme les blocs en air sur l'axe x
    """
    mc.setBlocks(xp, y, z, xp, y+2, z, 0)


def isAirx(x, y):
    """Verifie si les blocs sont de l'air sur l'axe x
    """
    if mc.getBlock(x, y, zp) == 0:
        return True
    else:
        return False


def isAirz(z, y):
    """Verifie si les blocs sont de l'air sur l'axe z
    """
    if mc.getBlock(xp, y, z) == 0:
        return True
    else:
        return False


def Mine(x, y, z, direction, size):
    """Cree une mine d'une taille donee
    """
    # Afin de ne pas depasser la bedrock
    # Couche de bedrock environ -50 sur Minecraft
    if size >= yp+50:
        mc.postToChat("it is too big")
    if direction == "North":
        for i in range(size):
            airz(z-(i+1), y-(i+1))
            # Escaliers
            mc.setBlock(x, y-(i+2), z-(i+1), 67, 2)
        # Premier bloc d'escalier sous le joueur
        mc.setBlock(x, y-1, z, 67, 2)
        # Pour que le sable/gravier tombe
        time.sleep(1)
        for i in range(size):
            # Verifie si du sable ou du gravier est tombé
            if isAirz(z-(1+i), y-(1+i)) is False:
                for i in range(size):
                    airz(z-(i+1), y-(i+1))
        # Les torches doivent etre placees apres la verification
        # Pour prevenir les bugs
        for i in range(size//5):
            mc.setBlock(x, y-(1+i)*5, z-(1+i)*5, 50, 2)
    if direction == "South":
        for i in range(size):
            airz(z+(i+1), y-(i+1))
            mc.setBlock(x, y-(i+2), z+(i+1), 67, 3)
        mc.setBlock(x, y-1, z, 67, 3)
        time.sleep(1)
        for i in range(size):
            if isAirz(z+(1+i), y-(1+i)) is False:
                Mine(x, y, z, direction, size)
        time.sleep(1)
        for i in range(size//5):
            mc.setBlock(x, y-(1+i)*5, z+(1+i)*5, 50, 1)
    if direction == "East":
        for i in range(size):
            airx(x+(i+1), y-(i+1))
            mc.setBlock(x+(i+1), y-(i+2), z, 67, 1)
        mc.setBlock(x, y-1, z, 67, 1)
        time.sleep(1)
        for i in range(size):
            if isAirx(x-(1+i), y-(1+i)) is False:
                Mine(x, y, z, direction, size)
        time.sleep(1)
        for i in range(size//5):
            mc.setBlock(x+(1+i)*5, y-(1+i)*5, z, 50, 4)
    if direction == "West":
        for i in range(size):
            airx(x-(i+1), y-(i+1))
            mc.setBlock(x-(i+1), y-(i+2), z, 67, 0)
            mc.setBlock(x, y-1, z, 67, 0)
        for i in range(size):
            if isAirx(x-(1+i), y-(1+i)) is False:
                Mine(x, y, z, direction, size)
        time.sleep(1)
        for i in range(size//5):
            mc.setBlock(x-(1+i)*5, y-(1+i)*5, z, 50, 3)
