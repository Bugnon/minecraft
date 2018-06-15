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
Transformation de blocs non vides autour du joueur a l'instar du roi Midas.
Les blocs transformes peuvent etre de n'importe quel materiau.
la taille du bloc autour du joueur doit etre impaire.
La transformation se fait colonne apres colonne donc la fonction prend
relativement beaucoup de temps.
"""
# =========================================================================== #
#                         2. Code                                             #
# =========================================================================== #

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# =========================================================================== #
#                         2.1 Verificaton des blocs                           #
# =========================================================================== #


def isAir(x, y, z):
    """Verifie si le bloc est de l'air
    """
    if mc.getBlock(x, y, z) == 0:
        return True
    else:
        return False

# =========================================================================== #
#                         2.2 Transformation des blocs                        #
# =========================================================================== #


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


xp,yp,zp = mc.player.getTilePos()
Midascube(xp,yp,zp,7, 41)