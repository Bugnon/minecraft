# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#                         MAGIC WAND, MINECRABRACADABRA                       #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#      Auteurs:   Albert et Ludovic
#  Affiliation:   Gymnase du Bugnon
#        Annee:   2017-2018
#       Classe:   OC-Informatique

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# =========================================================================== #
#                         1. Description du Fichier                           #
# =========================================================================== #
"""
Creation d'une mine de taille variable dans la direction nord ou sud
depuis la position du joueur.
La mine est un escalier et des torches sont posees tous les 5 blocs
"""
# =========================================================================== #
#                         2. Code                                             #
# =========================================================================== #

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# Position du joueur
xp, yp, zp = mc.player.getTilePos()

# =========================================================================== #
#                         2.1 Verification et transformation                  #
#                            de blocs en air                                  #
# =========================================================================== #


def airz(z, y):
    """Transforme les blocs en air sur l'axe x
    """
    mc.setBlocks(xp, y, z, xp, y+2, z, 0)


def isAirz(z, y):
    """Verifie si les blocs sont de l'air sur l'axe z
    """
    if mc.getBlock(xp, y, z) == 0:
        return True
    else:
        return False

# =========================================================================== #
#                         2.2 Creation de la mine                             #
# =========================================================================== #


def Mine(x, y, z, direction, size):
    """Cree une mine d'une taille donee dans la direction Sud ou Nord
    """
    # Afin de ne pas depasser la bedrock
    # Couche de bedrock environ -50 sur Minecraft
    if size >= y+50:
        mc.postToChat("It is too big")
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
