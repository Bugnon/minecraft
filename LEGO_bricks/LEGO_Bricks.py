<<<<<<< HEAD
## Author: Gabriel Fleischer et Furbringer
## Date: 5. 10. 2017
## Affiliation: Gymnase du Bugnon
## OC informatique
## import the modules to access the GPIO
=======
# Auteurs: Gabriel Fleischer et Furbringer
# Date: 05.10.2017
# Affiliation: Gymnase du Bugnon
# OC informatique

# Importation du module pour accéder au GPIO
>>>>>>> eb4f264dfacb66a19cdfaddbf30a08e50b2f2a5a
import RPi.GPIO as gpio
# Importation du module cv2
import cv2
import numpy as np
# Importation des modules utilitaires
import time
import math
# Importation du module pour interagir avec Minecraft
from mcpi.minecraft import Minecraft
# Importation du module de la caméra
from picamera.array import PiRGBArray
from picamera import PiCamera

<<<<<<< HEAD
from mcpi.minecraft import Minecraft

print("Initialising")

mc = Minecraft.create()
mc.postToChat("Initialising")
p = mc.player

hight = 1

def placeBlock(x,y):
    global hight
    global mc
    
    mc.postToChat(str((x, hight, y)))
    
    mc.setBlock(x,hight,y, 35, 15)
=======
print("Initialising")


# ===========================================
# Initialisation des variables configurables
# Utilisez le jupyter initialization_helper
# pour vous faciliter la configuration.
# ===========================================

# Sommets du carré que le programme doit observer.
upper_left = (227, 146)
upper_right = (450, 142)
down_left = (230, 362)
down_right = (447, 362)

# Largeur de l'image sur laquelle le programme travaille.
final_size = 150
# Nombre de points à vérifier
nombre_de_points = 8
# Bordure en pixel
bordure = 25

# Positons (x; y) des points qui doivent être vérifiés
# pour créer les structures prédéfinies.
garden = (67, 145)
fountain = (81, 145)
house = (97, 145)

# Point de l'image qui restera inchangé entre chaque manipulations.
# Utilisé pour limiter les problèmes liés à la luminosité.
pointToWatch = (5, 30)

# Pin du bouton sur le GPIO
button = 14

# Temps en secondes durant lequel le bouton doit rester pressé
# avant que le système ne se réinitialise.
resetPushTime = 5


def placeBlock(x, z):
    """Place un bloc de laine noire aux coordonnees (x, height, z)"""
    global height
    global mc

    mc.setBlock(x, height, z, 35, 15)

# ===========================================
# Méthodes de génération des constructions
# ===========================================


def build_house(px, py, pz,
                length=5, height=4, width=5,
                wallBlock=5, secondaryWall=17, groundBlock=43, roofBlock=45):
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
    # Ground
    mc.setBlocks(px, py, pz, px+length-1, py, pz+width-1, groundBlock)

    # Walls
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
    # Door
    mc.setBlock(px + math.floor(length/4), py+1, pz, 64, 3)
    mc.setBlock(px + math.floor(length/4), py+2, pz, 64, 11)

    # Windows
    mc.setBlocks(px, py+2, pz+math.floor(width/2)-1,
                 px, py+2, pz+math.floor(width/2)+1, 102)

    mc.setBlock(px + math.floor(length/4*3), py+2, pz, 102)

    # Roof
    for i in range(width+2):
        h = 0
        for j in range(length+2):
            x = j-1
            z = i-1
            if x > float(length)/2:
                h = h-1
            if x < float(length)/2:
                h = h+1
            if (z == 0 or z == width-1) and (x >= 0 and x <= length-1):
                if x == 0 or x == length-1:
                    mc.setBlocks(px+x, py+height, pz+z, px+x,
                                 py+height+h-1, pz+z, secondaryWall)
                else:
                    mc.setBlocks(px+x, py+height, pz+z, px+x,
                                 py+height+h-1, pz+z, wallBlock)

            mc.setBlock(px+x, py+height+h-1, pz+z, roofBlock)


def build_garden(x, y, z):
    """Crée une structures jardin aux coordonnees x, y, z"""
    for l in [4, 2]:
        # Create a part of the garden, the center square and the outer walls.
        # The outer walls' dimention is l x e.
        e = l
        # Empty the place
        mc.setBlocks(x-l, y, z-e, x+l, y+10, z+e, 0)
        # Place tall_grass inside the square
        mc.setBlocks(x-l+1, y, z+e, x+l-1, y, z+e-1, 31, 1)
        mc.setBlocks(x-l+1, y, z-e, x+l-1, y, z-e+1, 31, 1)
        mc.setBlocks(x-l+1, y, z-e, x-l+1, y, z+e-1, 31, 1)
        mc.setBlocks(x+l-1, y, z-e, x+l-1, y, z+e-1, 31, 1)
        # Place the inside walls
        mc.setBlocks(x-2, y, z+2, x+2, y+1, z+2, 18)
        mc.setBlocks(x-2, y, z-2, x+2, y+1, z-2, 18)
        mc.setBlocks(x-2, y, z-2, x-2, y+1, z+2, 18)
        mc.setBlocks(x+2, y, z-2, x+2, y+1, z+2, 18)
        # place the grass floor
        mc.setBlocks(x-l, y-1, z-e, x+l, y-1, z+e, 2)

        # Place the outside walls
        mc.setBlocks(x-l, y, z+e, x+l, y+2, z+e, 18)
        mc.setBlocks(x-l, y, z-e, x+l, y+2, z-e, 18)
        mc.setBlocks(x-l, y, z-e, x-l, y+2, z+e, 18)
        mc.setBlocks(x+l, y, z-e, x+l, y+2, z+e, 18)

        # Makes the wooden floor
        mc.setBlocks(x+l, y, z, x-l, y+1, z, 0)
        mc.setBlocks(x, y, z+e, x, y+1, z-e, 0)
        mc.setBlocks(x+l, y-1, z, x-l, y-1, z, 5)
        mc.setBlocks(x, y-1, z+e, x, y-1, z-e, 5)


def build_fountain(x, y, z):
    """Crée une foutaine aux coordonnees x, y, z."""
    mc.setBlocks(x-3, y, z-3, x+1, y+1, z+1, 1)
    mc.setBlocks(x-2, y+1, z-2, x, y+1, z, 8)
    mc.setBlocks(x-1, y+1, z-1, x-1, y+3, z-1, 1)
>>>>>>> eb4f264dfacb66a19cdfaddbf30a08e50b2f2a5a

# =======================================
# Initialisation
# =======================================


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

# Flag
# 0  = Relâché
# 1  = Appuyée
# ' ' = Juste relâché
flag = 0
# Time flag : Sauvegarde le temps de pression
time_flag = 0
# Délai durant lequel un changement d'état du bouton est ignoré,
# il peut être causé par une simple inconstance.
antirebond_time = 0.10
# Booléen sauvegardant une réinitialisation pour ne pas l'effectuer deux fois
alreadyReset = False

# Images
first_pic = None
last_pic = None
new_pic = None

# Liste de tuples, sauvegardant les positions a vérifié sur l'image
# et leur position correspondante dans Minecraft.
# Tuple : (mcx, mcy, x, y)
#    x : pixel x
#    y : pixel y
#    mcx : minecraft x
#    mcy : Minecraft y
positions = buildPositions(nombre_de_points, bordure, final_size)

# Création de la matrice de perspective M.
inCorners = np.float32([[upper_left[0], upper_left[1]],
                        [upper_right[0], upper_right[1]],
                        [down_left[0], down_left[1]],
                        [down_right[0], down_right[1]]])
outCorners = np.float32([[0, 0],
                         [final_size, 0],
                         [0, final_size],
                         [final_size, final_size]])
M = cv2.getPerspectiveTransform(inCorners, outCorners)

# ---------------------------------------
# Gpio initialisation
# ---------------------------------------
gpio.setmode(gpio.BCM)
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_UP)

# ---------------------------------------
# Initialisation de l'environnement dans Minecraft
# ---------------------------------------

# Initialise les variables mc et player
mc = Minecraft.create()
mc.postToChat("Initialising")
p = mc.player

# Téléportation du joueur et génération de l'emplacement des constructions
p.setPos(5, 20, 5)
mc.setBlocks(-2, -1, -2, 9, 100, 9, 155)
mc.setBlocks(-1, 0, -1, 8, 100, 8, 0)
mc.setBlocks(0, -1, 0, 7, -1, 7, 2)
# int : utilise pour définir la hauteur à laquelle les blocs seront placés
height = 0

# ---------------------------------------
# Initialisation de la caméra
# ---------------------------------------
# Initialise la caméra et prend les références pour rawCapture
camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640, 480))

debug = -5


def update_button():
    """Test si le bouton est appuye, relache ou en train d'etre appuye.
modifie le flag du bouton :
        -0  = Relâché
        -1  = Appuye
        -' ' = Juste relâché
"""
    global flag
    global time_flag
    global button
    global antirebond_time
<<<<<<< HEAD
    
    if  not gpio.input(button) and flag==0 and (time_flag==0 or time_flag+antirebond_time<time.time()):
        flag=1
        time_flag=time.time()
    elif (flag== 1 or flag==' ') and not gpio.input(button):
        flag = ' '
    
    elif (flag==' ' or flag==1 )and gpio.input(button) and (time_flag==0 or time_flag+antirebond_time<time.time()):       
        flag=0
        time_flag=time.time()

def init(angle, center, radius):
    global mc
    p = mc.player
    
    p.setPos(9, 10,0)
    mc.setBlocks(-2,-1,-2, 10, 100, 10, 155)
    mc.setBlocks(-1,0,-1, 9, 100, 9, 0)
    mc.setBlocks(0,-1,0, 8, -1, 8, 2)
    
    (cx, cy) = center
    minX = int(cx - radius)
    minY = int(cy - radius)
    maxX = int(cx + radius)
    maxY = int(cy + radius)
    return (angle, (minY, minX), (maxY, maxX), (int(cy), int(cx)))

def checkDif(img1, img2, x, y, dif2, image, tolerence=70):
    pos1 = int(img1[x, y])
    pos2 = int(img2[x, y])
    dif = pos1 - pos2 - dif2
    if dif < 0:
        dif = -dif
    return dif >= tolerence

def takePicture(frame, frameData):
    (angle, (minX, minY), (maxX, maxY), (centerX, centerY)) = frameData
    dims = frame.shape[:2]
    M = cv2.getRotationMatrix2D((centerX, centerY), angle, 1)
    frame = cv2.warpAffine(frame, M, dims)
    frame = frame[ minX:maxX , minY:maxY ]
    frame = cv2.resize(frame, (150, 150), interpolation = cv2.INTER_AREA)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    return frame

def onButtonPressed():
=======

    pressed = not gpio.input(button)
    last_pressed = flag == 1

    if pressed:
        if time_flag == 0:
            flag = 1
            time_flag = time.time()
    elif time.time() - time_flag > antirebond_time:
        if last_pressed:
            flag = ' '
        else:
            flag = 0
            time_flag = 0


def onButtonPressed():
    """S'execute lorsque l'on  appuye sur le bouton."""
>>>>>>> eb4f264dfacb66a19cdfaddbf30a08e50b2f2a5a
    global first_pic
    global last_pic
    global new_pic
    global positions
    global pointToWatch
<<<<<<< HEAD
    global hight
    
	last = first_pic
	new = new_pic
	
    (b1, g1, r1) = last[pointToWatch[0], pointToWatch[1]]
    (b2, g2, r2) = new[pointToWatch[0], pointToWatch[1]]
    
    r = r1-r2
    g = g1-g2
    b = b1-b2

    (B1, G1, R1)=cv2.split(last)
    (B2, G2, R2)=cv2.split(new)
    for (mcx, mcy, x, y) in positions:
        if checkDif(B1, B2, x, y, b, "Bleu") or checkDif(G1, G2, x, y, g, "vert") or checkDif(R1, R2, x, y, r, "rouge"):
            placeBlock(mcx, mcy)
    hight = hight+1
   
def buildPositions(n, border, totalLenght):
    poses = []
    for mcx in range(n):
        for mcy in range(n):
            poses.append((mcx, mcy, int(border + (totalLenght-2*border)/(n - 1)*mcx), int(border + (totalLenght-2*border)/(n - 1)*mcy)))
    return poses
    
def reset():
    global mc
    global hight
    print("reset")
    mc.setBlocks(-2,-1,-2, 9, 100, 9, 155)
    mc.setBlocks(-1,0,-1, 8, 100, 8, 0)
    mc.setBlocks(0,-1,0, 7, -1, 7, 2)
    mc.postToChat("reset")
    hight = 1
    
def showInit(positions, image):
    global pointToWatch
    
    p = image.copy()
    for (mcx, mcy, x, y) in positions:
        p[x-1:x+1 , y-1:y+1] = (0, 0, 255)
    p[pointToWatch[0], pointToWatch[1]] = (0, 255, 0)
    return p


# initialize the camera and grab a reference to the raw camera
# capture
camera = PiCamera()
#camera.resolution = (640, 480)
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640, 480))


##Manual
frameData = init(-2, (350, 292), 95)
pointToWatch = (3, 30)

#reset detection
resetPushTime = 5
alreadyReset=False

#pictures
first_pic = None
last_pic = None
new_pic = None

#List of tuples storing the diffrent positions of the LEGO bricks to check.
#tuple : (mcx, mcy, x, y)
# x : pixel x 
# y : pixel y
# mcx : minecraft x
# mcy : minecraft y
##Manual
positions = buildPositions(8, 16, 150)

i = -1
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = takePicture(f.array, frameData)
    i = i + 1
    if new_pic == None and i > 2:
		first_pic = frame
=======
    global height

    last = first_pic
    new = new_pic

    # Calcule la différence de couleur entre last et new
    (b1, g1, r1) = last[pointToWatch[0], pointToWatch[1]]
    (b2, g2, r2) = new[pointToWatch[0], pointToWatch[1]]

    r = math.fabs(int(r1)-int(r2))
    g = math.fabs(int(g1)-int(g2))
    b = math.fabs(int(b1)-int(b2))

    print(r, g, b)

    (B1, G1, R1) = cv2.split(last)
    (B2, G2, R2) = cv2.split(new)
    # Vérifie pour chaque couleur à chaque position définie
    # par build_positions() si la différence de couleur est
    # plus grande que le seuil de tolérance.
    for (mcx, mcy, x, y) in positions:
        if (checkDif(B1, B2, x, y, b) or
                checkDif(G1, G2, x, y, g) or
                checkDif(R1, R2, x, y, r)):
            # Si la différence dépasse la tolérance pour
            # au moins une des couleurs, place un bloc dans
            # Minecraft aux coordonnées correspondantes.
            placeBlock(mcx, mcy)
    # Augmente la hauteur de 1.
    height += 1

    # Cette variable sert à définir quelle construction a été identifiée.
    i = 0
    for (x, y) in [garden, fountain, house]:
        if (checkDif(B1, B2, x, y, b) or
                checkDif(G1, G2, x, y, g) or
                checkDif(R1, R2, x, y, r)):
            if i == 0:
                build_garden(4, 0, 4)
            elif i == 1:
                build_fountain(6, 0, 6)
            elif i == 2:
                build_house(1, -1, 1)

        i += 1


def takePicture(frame, M):
    """Applique les transformations sur l'image
"""
    global final_size
    # Application de l'algorithme de perspective
    frame = cv2.warpPerspective(frame, M, (final_size, final_size))
    # Floutage pour éviter les trop gros changements de couleur.
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
    p = mc.player
    p.setPos(5, 20, 5)
    mc.setBlocks(-2, -1, -2, 9, 100, 9, 155)
    mc.setBlocks(-1, 0, -1, 8, 100, 8, 0)
    mc.setBlocks(0, -1, 0, 7, -1, 7, 2)
    mc.postToChat("Reinitialisation")
    height = 0


def showInit(positions, frame, image):
    """Affiche l'image avec les transformation effectuee par la configuration.
Permet de verifier que les valeurs fonctionne.
    -positions : Positions des points par rapport a l'image, cf build_positions
    -image : L'image
    """
    global pointToWatch
    global garden
    global foutain
    global house
    global upper_left
    global upper_right
    global down_left
    global down_right

    p = image.copy()
    for (mcx, mcy, x, y) in positions:
        p[x-1:x+1, y-1:y+1] = (0, 0, 0)
    p[pointToWatch[0]-2:pointToWatch[0]+2,
      pointToWatch[1]-2:pointToWatch[1]+2] = (0, 255, 255)
    # Les positions des constructions préfaites
    p[garden[0]-2:garden[0]+2, garden[1]-2:garden[1]+2] = (255, 0, 0)
    p[fountain[0]-2:fountain[0]+2, fountain[1]-2:fountain[1]+2] = (0, 255, 0)
    p[house[0]-2:house[0]+2, house[1]-2:house[1]+2] = (0, 0, 255)

    f = frame.copy()
    cv2.line(f, upper_left, upper_right, (0, 0, 255), 5)
    cv2.line(f, upper_right, down_right, (0, 0, 255), 5)
    cv2.line(f, down_right, down_left, (0, 0, 255), 5)
    cv2.line(f, down_left, upper_left, (0, 0, 255), 5)
    d = f.shape[0]
    if d > f.shape[1]:
        d = f.shape[1]
    f = f[0:d, 0:d]
    f = cv2.resize(f,
                   (image.shape[0], image.shape[1]),
                   interpolation=cv2.INTER_AREA)
    return np.hstack([f, p])


# Boucle infinie de la caméra, f est l'image capturée.
for f in camera.capture_continuous(rawCapture,
                                   format="bgr",
                                   use_video_port=True):
    # Prend une photo
    frame = takePicture(f.array, M)

    # Permets d'éviter les 2 premières images captées par la caméra et
    # de laisser à celle-ci le temps de s'adapter a la luminosité de la pièce.
    debug += 1
    if new_pic is None and debug > 2:
        first_pic = frame
>>>>>>> eb4f264dfacb66a19cdfaddbf30a08e50b2f2a5a
        new_pic = frame
        last_pic = frame
        print("Initialisation complete !")
        mc.postToChat("Initialisation complete !")
<<<<<<< HEAD
    pushed = False
    if flag:
        pushed = True
        
    button_fct_pressed()
    
    if not flag:
        if pushed and not alreadyReset:
=======

    # ----------------------------------------
    # Boutons
    # ----------------------------------------
    # Mise à jour de l'état du bouton
    update_button()

    # Tests pour savoir si l'on doit exécuter la fonction onButtonPressed(),
    # la fonction reset() ou ne rien faire
    if flag == ' ':
        if not alreadyReset:
>>>>>>> eb4f264dfacb66a19cdfaddbf30a08e50b2f2a5a
            last_pic = new_pic
            new_pic = frame
            onButtonPressed()
        alreadyReset = False
<<<<<<< HEAD
    
    t = time.time()
    if flag and t - time_flag  >= resetPushTime and not alreadyReset:
        reset()
        alreadyReset=True
        
    
    if new_pic != None :
        cv2.imshow("Diff", showInit(positions, new_pic))
        #cv2.imshow("Diff", np.hstack([new_pic, last_pic]))
    rawCapture.truncate(0)
    
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
=======
    elif flag == 1:
        if(time_flag != 0 and
                time.time() - time_flag > resetPushTime and
                not alreadyReset):
            reset()
            alreadyReset = True

    # Affiche l'image initialisée, permets de vérifier que les valeurs entrées
    # lors de la configuration sont justes.
    if new_pic is not None:
        if debug < 100:
            cv2.imshow("Image", showInit(positions, f.array, new_pic))
        else:
            p = new_pic.copy()
            for (mcx, mcy, x, y) in positions:
                p[x-1:x+1, y-1:y+1] = (0, 0, 0)
            p[pointToWatch[0]-2:pointToWatch[0]+2,
              pointToWatch[1]-2:pointToWatch[1]+2] = (0, 255, 255)
            # Les positions des constructions préfaites.
            p[garden[0]-2:garden[0]+2, garden[1]-2:garden[1]+2] = (255, 0, 0)
            p[fountain[0]-2:fountain[0]+2,
              fountain[1]-2:fountain[1]+2] = (0, 255, 0)
            p[house[0]-2:house[0]+2, house[1]-2:house[1]+2] = (0, 0, 255)

            cv2.imshow("Image", p)

    rawCapture.truncate(0)

    # Si la touche 'q' est pressée, arrête la boucle.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
>>>>>>> eb4f264dfacb66a19cdfaddbf30a08e50b2f2a5a
