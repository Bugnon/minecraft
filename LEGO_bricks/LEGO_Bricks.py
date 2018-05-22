# Author: Gabriel Fleischer et Furbringer
# Date: 5. 10. 2017
# Affiliation: Gymnase du Bugnon
# OC informatique

# Importation du module pour accéder au GPIO
import RPi.GPIO as gpio
# Importation du module cv2
import cv2
# Importation des modules utilitaires
import time
# Importation du module pour intéragir avec minecraft
from mcpi.minecraft import Minecraft

# Importation du module de la caméra
from picamera.array import PiRGBArray
from picamera import PiCamera

print("Initialising")

# Initialise les variables mc et player
mc = Minecraft.create()
mc.postToChat("Initialising")
p = mc.player


def placeBlock(x, z):
    """Place un bloc de laine noire aux coordonnées (x, height, z)"""
    global height
    global mc

    mc.setBlock(x, height, z, 35, 15)


# =======================================
# Initialisation
# =======================================
def init_frame(angle, center, radius):
    """Initialise les valeurs utiles pour l'interprétation de l'image
        angle : angle de rotation de l'image
        center : (x, y), centre de la plateforme de
construction en pixel sur l'image.
        radius : rayon en pixel du carré utilisé comprenant la platforme.

       Retourne : (angle, min, max, center)
        angle : angle de rotation de l'image
        min : (minX, minY), coordonnées minimales de l'image de la platforme
        max : (maxX, maxY), coordonnées maximales de l'image de la platforme
        center : (x, y), centre de la platforme
    """
    (cx, cy) = center
    minX = int(cx - radius)
    minY = int(cy - radius)
    maxX = int(cx + radius)
    maxY = int(cy + radius)
    return (angle, (minY, minX), (maxY, maxX), (int(cy), int(cx)))


def buildPositions(n, bordure, largeurTotale):
    """Crée la liste des tuples sauvegardant les positions à vérifier sur l'image
    et leur position correspondante dans mineraft.
        n : Nombre de positions par ligne
        bordure : taille de la bordure sur le coté
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
# min : (minX, minY), coordonnées minimales de l'image de la platforme
# max : (maxX, maxY), coordonnées maximales de l'image de la platforme
# center : (x, y), centre de la platforme
frameData = init_frame(-2, (350, 292), 95)

# Point de l'image qui restera inchangé entre chaque manipulation de
# l'utilisateur. Est utilisé pour limiter les problèmes liés à la luminosité
pointToWatch = (3, 30)

# Liste de tuples, sauvegardant les position à vérifier sur l'image et
# leur position correspondante dans mineraft.
# tuple : (mcx, mcy, x, y)
#   x : pixel x
#   y : pixel y
#   mcx : minecraft x
#   mcy : minecraft y
positions = buildPositions(8, 16, 150)

# Temps en secondes durant lequel le bouton doit
# rester pressé avant que le système ne se réinitialise.
resetPushTime = 5

# Flag
# 0  = relaché
# 1  = en train d'être appuyé
# ' ' = appuyé
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
# Téléporation du joueur et génération de l'emplacement des constructions
p.setPos(9, 10, 0)
mc.setBlocks(-2, -1, -2, 10, 100, 10, 155)
mc.setBlocks(-1, 0, -1, 9, 100, 9, 0)
mc.setBlocks(0, -1, 0, 8, -1, 8, 2)
# int : utilisé pour définir la hauteur à laquelle les blocs seront placés
height = 1

# ---------------------------------------
# Initialisation de la caméra
# ---------------------------------------
# initialise la camera et prend les référence pour rawCapture
camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640, 480))

debug = -1


def button_fct_pressed():
    """Test si le bouton est appuyé, relaché ou en train d'être appuyé.
modifie le flag du bouton :
        -0  = relaché
        -1  = en train d'être appuyé
        -' ' = appuyé
"""
# TODO !!! Je comprends pas, c'est pas propre
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

    # Calcule la différence de couleur entre last et new,
    (b1, g1, r1) = last[pointToWatch[0], pointToWatch[1]]
    (b2, g2, r2) = new[pointToWatch[0], pointToWatch[1]]

    r = r1-r2
    g = g1-g2
    b = b1-b2

    (B1, G1, R1) = cv2.split(last)
    (B2, G2, R2) = cv2.split(new)
    # Vérifie pour chaque couleur à chaque position définie
    # par build_positions() si la différence de couleur est
    # plus grande que le seuil de tolérence.
    for (mcx, mcy, x, y) in positions:
        if (checkDif(B1, B2, x, y, b) or
                checkDif(G1, G2, x, y, g) or
                checkDif(R1, R2, x, y, r)):
            # Si la différence dépasse la tolérence pour on moins une couleur,
            # place un bloc dans minecraft aux coordonnées correspondantes.
            placeBlock(mcx, mcy)
    # Augmente la hauteur de 1.
    height += 1


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
    """Regarde si la différence d'intensité de couleur au points (x, y)
entre img1 et img2 dépasse la tolérence.
         -dif2 : La différence d'intensité entre
         last et new au point qui ne devrait pas changer.
         Permet d'être moins dépendant d'une luminosité constante.
"""
    pos1 = int(img1[x, y])
    pos2 = int(img2[x, y])
    dif = pos1 - pos2 - dif2
    if dif < 0:
        dif = -dif
    return dif >= tolerence


def reset():
    """Réinitialise la platforme dans minecraft et remet la hauteur à 1"""
    global mc
    global height
    print("Réinitialisation")
    mc.setBlocks(-2, -1, -2, 9, 100, 9, 155)
    mc.setBlocks(-1, 0, -1, 8, 100, 8, 0)
    mc.setBlocks(0, -1, 0, 7, -1, 7, 2)
    mc.postToChat("Réinitialisation")
    height = 1


def showInit(positions, image):
    """Affiche l'image avec les transformation effectuée par la configuration.
Permet de vérifier que les valeurs fonctionne.
    -positions : Positions des points par rapport à l'image, cf build_positions
    -image : L'image
    """
    global pointToWatch

    p = image.copy()
    for (mcx, mcy, x, y) in positions:
        p[x-1:x+1, y-1:y+1] = (0, 0, 255)
    p[pointToWatch[0], pointToWatch[1]] = (0, 255, 0)
    return p


# Boucle infinie de la caméra, f est l'image capturée.
for f in camera.capture_continuous(rawCapture,
                                   format="bgr",
                                   use_video_port=True):
    # Prend une photo
    frame = takePicture(f.array, frameData)

    # Permet d'éviter les 2 premières images captées par la caméra et de
    # laisser à celle-ci le temps de s'adapter à la luminosité de la pièce.
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
    # Mise à jour de l'êtat du bouton
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

    # Affiche l'image initialisée, permet de vérifier que les valeurs entrée
    # lors de la configuration sont justes.
    if new_pic is not None and debug < 200:
        cv2.imshow("Diff", showInit(positions, new_pic))

    rawCapture.truncate(0)

    # Si la touche 'q' est pressée, arrete la boucle
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
