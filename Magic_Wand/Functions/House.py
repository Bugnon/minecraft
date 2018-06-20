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
Creation d'une maison autour du joueur.
La maison peut etre en pierre ou en bois et de taille variable.
La porte est orientee au nord du joueur.
Un espace vide est cree 2 blocs autour de la maison.
un bloc de fondation se trouve sous la maison.
"""
# =========================================================================== #
#                         2. Code                                             #
# =========================================================================== #

from mcpi import minecraft
mc = minecraft.Minecraft.create()

# quelques id de blocs
glass = 102
door_low = 64, 1
door_high = 64, 11

# =========================================================================== #
#                         2.1 Espace vide                                     #
# =========================================================================== #


def clear_space(x, y, z, range):
    """Transforme les blocs autour du joueur en air"""
    mc.setBlocks(
        x-range, y+200, z-range, x+range, y, z+range, 0)

# =========================================================================== #
#                         2.2 Construction de la maison                       #
# =========================================================================== #


def house(x, y, z, material, n):
    """Cree une petite maison autour du joueur"""
    if material == "WOOD":
        M1 = 5
        M2 = 17
        stairs = 53
    if material == "COBBLESTONE":
        M1 = 98
        M2 = 4
        stairs = 109
    # Espace vide de 2 blocs autour de la maison
    clear_space(x, y, z, n+3)
    # Blocs sous la maison
    mc.setBlocks(
        x-n-3, y-1, z-n-3, x+n+3, y-200, z+n+3, M1)
    # Base de la maison
    mc.setBlocks(
        x-n-1, y, z-n-1, x+n+1, y+n+2, z+n+1, M1)
    mc.setBlocks(
        x-n, y, z-n, x+n, y+n+2, z+n, 0)
    # Porte et face nord
    mc.setBlocks(
        x-n, y+1, z-n-1, x+n, y+n+1, z-n-1, M2)
    mc.setBlock(x, y, z-n-1, door_low)
    mc.setBlock(x, y+1, z-n-1, door_high)
    # Face Est, Ouest et Sud
    mc.setBlocks(
        x-n-1, y+1, z-n, x-n-1, y+n+1, z+n, M2)
    mc.setBlocks(
        x+n+1, y+1, z-n, x+n+1, y+n+1, z+n, M2)
    mc.setBlocks(
        x-n, y+1, z+n+1, x+n, y+n+1, z+n+1, M2)
    # Fenetres
    mc.setBlocks(
        x-n-1, y+1, z-n+1, x-n-1, y+n+1, z+n-1, glass)
    mc.setBlocks(
        x+n+1, y+1, z-n+1, x+n+1, y+n+1, z+n-1, glass)
    mc.setBlocks(
        x-n+1, y+1, z+n+1, x+n-1, y+n+1, z+n+1, glass)
    # Toit couche 1
    mc.setBlocks(
        x-n, y+n+2, z-n, x+n, y+n+3, z+n, M1)
    mc.setBlocks(
        x+n+1, y+n+3, z-n-1, x+n+1, y+n+3, z+n+1, stairs, 1)
    mc.setBlocks(
        x-n-1, y+n+3, z-n-1, x-n-1, y+n+3, z+n+1, stairs, 0)
    mc.setBlocks(
        x-n, y+n+3, z-n-1, x+n, y+n+3, z-n-1, stairs, 2)
    mc.setBlocks(
        x-n, y+n+3, z+n+1, x+n, y+n+3, z+n+1, stairs, 3)
    # Toit couche 2
    mc.setBlocks(
        x-n+1, y+n+4, z-n+1, x+n-1, y+n+4, z+n-1, M1)
    mc.setBlocks(
        x+n, y+n+4, z-n, x+n, y+n+4, z+n, stairs, 1)
    mc.setBlocks(
        x-n, y+n+4, z-n, x-n, y+n+4, z+n, stairs, 0)
    mc.setBlocks(
        x-n+1, y+n+4, z-n, x+n-1, y+n+4, z-n, stairs, 2)
    mc.setBlocks(
        x-n+1, y+n+4, z+n, x+n-1, y+n+4, z+n, stairs, 3)
