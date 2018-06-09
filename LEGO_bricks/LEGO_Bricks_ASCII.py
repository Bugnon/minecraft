# Author: Gabriel Fleischer et Furbringer
# Date: 5. 10. 2017
# Affiliation: Gymnase du Bugnon
# OC informatique

# Importation du module pour acceder au GPIO
import RPi.GPIO as gpio
# Importation du module cv2
import cv2
# Importation des modules utilitaires
import time
# Importation du module pour interagir avec minecraft
from mcpi.minecraft import Minecraft

# Importation du module de la camera
from picamera.array import PiRGBArray
from picamera import PiCamera

print("Initialising")

# Initialise les variables mc et player
mc = Minecraft.create()
mc.postToChat("Initialising")
p = mc.player


def placeBlock(x, z):
    """Place un bloc de laine noire aux coordonnees (x, height, z)"""
    global height
    global mc

    mc.setBlock(x, height, z, 35, 15)

#Méthodes de génération de constructions dans minecraft
def house(px, py, pz, length = 5, height = 4, width = 5, wallBlock = 5, secondaryWall = 17, groundBlock = 43, roofBlock = 45):
    """
    Create a house at the player's current position with the given arguments :
        - px : X position of the house
        - py : Y position of the house
        - pz : Z position of the house
        - length : the length of the house
        - height : the height of the house (Without the roof)
        - width : the width of the house
		- secondaryWall : The wall borders (pillars)
        - wallBlock : The block used to make the wall
        - groundBlock : The block used to make the ground
        - roofBlock : The block used to make the roof
    """
    
    #ground
    mc.setBlocks(px, py, pz, px+length-1, py, pz+width-1, groundBlock)
    
    #walls
    for x in range(length):
        for y in range(height + 1):
            for z in range(width):
                if x == 0:
                    if z == 0 or z == width - 1:
                        mc.setBlock(px+x, py+y, pz+z, secondaryWall)
                    else:
                        mc.setBlock(px+x, py+y, pz+z, wallBlock)
                elif x == length-1:
                    if z == 0 or z == width-1:
                        mc.setBlock(px+x, py+y, pz+z, secondaryWall)
                    else:
                        mc.setBlock(px+x, py+y, pz+z, wallBlock)
                elif z == 0 or z == width-1:
                    mc.setBlock(px+x, py+y, pz+z, wallBlock)
    #door
    mc.setBlock(px + math.floor(length/4), py+1, pz, 64, 3)
    mc.setBlock(px + math.floor(length/4), py+2, pz, 64, 11)
    
    #windows
    mc.setBlocks(px, py+2, pz+math.floor(width/2)-1, px, py+2, pz+math.floor(width/2)+1, 102)
    
    mc.setBlock(px + math.floor(length/4*3), py+2, pz, 102)
    
    #roof
    for i in range(width+2):
        h = 0
        for j in range(length+2):
            x=j-1
            z=i-1
            if x > float(length)/2:
                h=h-1
            if x < float(length)/2:
                h=h+1
            if (z == 0 or z == width-1) and (x >= 0 and x <= length-1):
                if x == 0 or x == length-1:
                    mc.setBlocks(px+x, py+height, pz+z, px+x, py+height+h-1, pz+z, secondaryWall)
                else:
                    mc.setBlocks(px+x, py+height, pz+z, px+x, py+height+h-1, pz+z, wallBlock)

            mc.setBlock(px+x, py+height+h-1, pz+z, roofBlock)

def garden(x, y, z):
    for l in [6, 4, 2]:
        #Create a part of the garden, the center square and the outer walls. The outer walls' dimention is l x e. 
        e = l
        #Empty the place
        mc.setBlocks(x-l, y,z-e,x+l,y+10,z+e, 0)
        #Place tall_grass inside the square
        mc.setBlocks(x-l+1,y,z+e,x+l-1,y,z+e-1,31,1)
        mc.setBlocks(x-l+1,y,z-e,x+l-1,y,z-e+1,31,1)
        mc.setBlocks(x-l+1,y,z-e,x-l+1,y,z+e-1,31,1)
        mc.setBlocks(x+l-1,y,z-e,x+l-1,y,z+e-1,31,1)
                #Place the inside walls
        mc.setBlocks(x-2,y,z+2,x+2,y+1,z+2,18)
        mc.setBlocks(x-2,y,z-2,x+2,y+1,z-2,18)
        mc.setBlocks(x-2,y,z-2,x-2,y+1,z+2,18)
        mc.setBlocks(x+2,y,z-2,x+2,y+1,z+2,18)
                #place grass floor
        mc.setBlocks(x-l,y-1,z-e,x+l,y-1,z+e, 2)
                
        #Place the outside walls
        mc.setBlocks(x-l,y,z+e,x+l,y+2,z+e,18)
        mc.setBlocks(x-l,y,z-e,x+l,y+2,z-e,18)
        mc.setBlocks(x-l,y,z-e,x-l,y+2,z+e,18)
        mc.setBlocks(x+l,y,z-e,x+l,y+2,z+e,18)
                
        #Makes the wooden floor
        mc.setBlocks(x+l,y,z,x-l,y+1,z, 0)
        mc.setBlocks(x,y,z+e,x,y+1,z-e,0)
        mc.setBlocks(x+l,y-1,z,x-l,y-1,z, 5 )
        mc.setBlocks(x,y-1,z+e,x,y-1,z-e,5)

def fountain(x,y,z):
    mc.setBlocks(x-5,y,z-5,x,y+1,z,1)
    mc.setBlocks(x-4,y+1,z-4,x-1,y+1,z-1,0)
    mc.setBlocks(x-4,y+1,z-4,x-1,y+1,z-1,8)
    mc.setBlocks(x-2,y+1,z-2,x-2,y+3,z-2,1)

# =======================================
# Initialisation
# =======================================
def init_frame(angle, center, radius):
    """Initialise les valeurs utiles pour l'interpretation de l'image
        angle : angle de rotation de l'image
        center : (x, y), centre de la plateforme de
construction en pixel sur l'image.
        radius : rayon en pixel du carre utilise comprenant la platforme.

       Retourne : (angle, min, max, center)
        angle : angle de rotation de l'image
        min : (minX, minY), coordonnees minimales de l'image de la platforme
        max : (maxX, maxY), coordonnees maximales de l'image de la platforme
        center : (x, y), centre de la platforme
    """
    (cx, cy) = center
    minX = int(cx - radius)
    minY = int(cy - radius)
    maxX = int(cx + radius)
    maxY = int(cy + radius)
    return (angle, (minY, minX), (maxY, maxX), (int(cy), int(cx)))


def buildPositions(n, bordure, largeurTotale):
    """Cree la liste des tuples sauvegardant les positions a verifier sur l'image
    et leur position correspondante dans mineraft.
        n : Nombre de positions par ligne
        bordure : taille de la bordure sur le cote
        largeurTotale : largeur totale de la plateforme en pixel sur l'image
    """
    poses = []
    for mcx in range(n):
        for mcy in range(n):
            poses.append((mcx,
                          mcy,
                          int(bordure+(largeurTotale-2*bordure)/(n-1)*mcx),
                          int(bordure+(largeurTotale-2*bordure)/(n-1)*mcy)))
    return poses


# ---------------------------------------
# Init des configurations
# ---------------------------------------
antirebond_time = 0.10
# Pin sur le GPIO
button = 14

# Frame data : (angle, min, max, center)
# angle : angle de rotation de l'image
# min : (minX, minY), coordonnees minimales de l'image de la platforme
# max : (maxX, maxY), coordonnees maximales de l'image de la platforme
# center : (x, y), centre de la platforme
frameData = init_frame(2.5, (362, 270), 105)

# Point de l'image qui restera inchange entre chaque manipulation de
# l'utilisateur. Est utilise pour limiter les problemes lies a la luminosite
pointToWatch = (3, 30)

# Liste de tuples, sauvegardant les position a verifier sur l'image et
# leur position correspondante dans mineraft.
# tuple : (mcx, mcy, x, y)
#   x : pixel x
#   y : pixel y
#   mcx : minecraft x
#   mcy : minecraft y
positions = buildPositions(8, 22, 150)

#Positons (x, y) des points qui doivent être vérifiés pour créer les structures prédéfinies.
garden = (67, 145)
fountain = (81, 145)
house = (97, 145)

# Temps en secondes durant lequel le bouton doit
# rester presse avant que le systeme ne se reinitialise.
resetPushTime = 5

# Flag
# 0  = relache
# 1  = en train d'etre appuye
# ' ' = appuye
flag = 0
# Time flag : Sauvegarde le temps de pression
time_flag = 0

# Reset detection
alreadyReset = False

# Pictures
first_pic = None
last_pic = None
new_pic = None

# ---------------------------------------
# Gpio initalisation
# ---------------------------------------
gpio.setmode(gpio.BCM)
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_UP)

# ---------------------------------------
# Initialisation de l'environnement dans minecraft
# ---------------------------------------
# Teleporation du joueur et generation de l'emplacement des constructions
p.setPos(9, 10, 0)
mc.setBlocks(-2, -1, -2, 10, 100, 10, 155)
mc.setBlocks(-1, 0, -1, 9, 100, 9, 0)
mc.setBlocks(0, -1, 0, 8, -1, 8, 2)
# int : utilise pour definir la hauteur a laquelle les blocs seront places
height = 1

# ---------------------------------------
# Initialisation de la camera
# ---------------------------------------
# initialise la camera et prend les reference pour rawCapture
camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640, 480))

debug = -1


def button_fct_pressed():
    """Test si le bouton est appuye, relache ou en train d'etre appuye.
modifie le flag du bouton :
        -0  = relache
        -1  = en train d'etre appuye
        -' ' = appuye
"""
    global flag
    global time_flag
    global button
    global antirebond_time

    if (not gpio.input(button) and
            flag == 0 and
            (time_flag == 0 or time_flag + antirebond_time < time.time())):
        flag = 1
        time_flag = time.time()
    elif (flag == 1 or flag == ' ') and not gpio.input(button):
        flag = ' '

    elif ((flag == ' ' or flag == 1) and
            gpio.input(button) and
            (time_flag == 0 or time_flag + antirebond_time < time.time())):
        flag = 0
        time_flag = time.time()


def onButtonPressed():
    """S'execute lorsque l'on  appuye sur le bouton."""
    global first_pic
    global last_pic
    global new_pic
    global positions
    global pointToWatch
    global height

    last = first_pic
    new = new_pic

    # Calcule la difference de couleur entre last et new,
    (b1, g1, r1) = last[pointToWatch[0], pointToWatch[1]]
    (b2, g2, r2) = new[pointToWatch[0], pointToWatch[1]]

    r = r1-r2
    g = g1-g2
    b = b1-b2

    (B1, G1, R1) = cv2.split(last)
    (B2, G2, R2) = cv2.split(new)
    # Verifie pour chaque couleur a chaque position definie
    # par build_positions() si la difference de couleur est
    # plus grande que le seuil de tolerence.
    for (mcx, mcy, x, y) in positions:
        if (checkDif(B1, B2, x, y, b) or
                checkDif(G1, G2, x, y, g) or
                checkDif(R1, R2, x, y, r)):
            # Si la difference depasse la tolerence pour on moins une couleur,
            # place un bloc dans minecraft aux coordonnees correspondantes.
            placeBlock(mcx, mcy)
    # Augmente la hauteur de 1.
    height += 1
    
    #Cette variable sert à définir quelle construction a été identifiée.
    i = 0
    for (x, y) in [garden, fountain, house]:
        if (checkDif(B1, B2, x, y, b) or
                checkDif(G1, G2, x, y, g) or
                checkDif(R1, R2, x, y, r)):
            if i == 0:
                garden(0, 1, 0)
            elif i == 1:
                foutain(0, 1, 0)
            elif i == 2:
                house(0, 1, 0)
                
        i+=1 

def takePicture(frame, frameData):
    """Applique les transformations sur l'image, voir frame_data
"""
    (angle, (minX, minY), (maxX, maxY), (centerX, centerY)) = frameData
    dims = frame.shape[:2]
    # Rotation
    M = cv2.getRotationMatrix2D((centerX, centerY), angle, 1)
    frame = cv2.warpAffine(frame, M, dims)
    # Recardage
    frame = frame[minX:maxX, minY:maxY]
    # Redimentionnage
    frame = cv2.resize(frame, (150, 150), interpolation=cv2.INTER_AREA)
    # Floutage pour eviter les trop gros changmement de couleur.
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    return frame


def checkDif(img1, img2, x, y, dif2, tolerence=70):
    """Regarde si la difference d'intensite de couleur au points (x, y)
entre img1 et img2 depasse la tolerence.
         -dif2 : La difference d'intensite entre
         last et new au point qui ne devrait pas changer.
         Permet d'etre moins dependant d'une luminosite constante.
"""
    pos1 = int(img1[x, y])
    pos2 = int(img2[x, y])
    dif = pos1 - pos2 - dif2
    if dif < 0:
        dif = -dif
    return dif >= tolerence


def reset():
    """Reinitialise la platforme dans minecraft et remet la hauteur a 1"""
    global mc
    global height
    print("Reinitialisation")
    mc.setBlocks(-2, -1, -2, 9, 100, 9, 155)
    mc.setBlocks(-1, 0, -1, 8, 100, 8, 0)
    mc.setBlocks(0, -1, 0, 7, -1, 7, 2)
    mc.postToChat("Reinitialisation")
    height = 1


def showInit(positions, image):
    """Affiche l'image avec les transformation effectuee par la configuration.
Permet de verifier que les valeurs fonctionne.
    -positions : Positions des points par rapport a l'image, cf build_positions
    -image : L'image
    """
    global pointToWatch
    global garden
    global foutain
    global house

    p = image.copy()
    for (mcx, mcy, x, y) in positions:
        p[x-1:x+1, y-1:y+1] = (0, 0, 0)
    p[pointToWatch[0], pointToWatch[1]] = (0, 0, 0)
    #Les positions des constructions préfaites
    p[garden[0]-2:garden[0]+2, garden[1]-2:garden[1]+2] = (255, 0, 0)
    p[fountain[0]-2:fountain[0]+2, fountain[1]-2:fountain[1]+2] = (0, 255, 0)
    p[house[0]-2:house[0]+2, house[1]-2:house[1]+2] = (0, 0, 255)
    return p


# Boucle infinie de la camera, f est l'image capturee.
for f in camera.capture_continuous(rawCapture,
                                   format="bgr",
                                   use_video_port=True):
    # Prend une photo
    frame = takePicture(f.array, frameData)

    # Permet d'eviter les 2 premieres images captees par la camera et de
    # laisser a celle-ci le temps de s'adapter a la luminosite de la piece.
    debug += 1
    if new_pic is None and debug > 2:
        first_pic = frame
        new_pic = frame
        last_pic = frame
        print("Initialisation complete !")
        mc.postToChat("Initialisation complete !")

    # ----------------------------------------
    # Boutons
    # ----------------------------------------
    pushed = False
    if flag:
        pushed = True
    # Mise a jour de l'etat du bouton
    button_fct_pressed()

    # Tests pour savoir si l'on doit exectuer la fonction onButtonPressed(),
    # la fonction reset() ou ne rien faire
    if not flag:
        if pushed and not alreadyReset:
            last_pic = new_pic
            new_pic = frame
            onButtonPressed()
        alreadyReset = False

    t = time.time()
    if (flag and t - time_flag >= resetPushTime and not alreadyReset):
        reset()
        alreadyReset = True

    # Affiche l'image initialisee, permet de verifier que les valeurs entree
    # lors de la configuration sont justes.
    if new_pic is not None:
        if debug < 100:
            cv2.imshow("Image", showInit(positions, new_pic))
        else:
            cv2.imshow("Image", new_pic)

    rawCapture.truncate(0)

    # Si la touche 'q' est pressee, arrete la boucle
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
