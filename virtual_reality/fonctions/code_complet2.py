"""
Projet : Virtual reality with Minecraft Pi
Autheur : Benoit Gallois et Jonas Grütter
Date :  29.03.18

Déscription de  l'installation

Ce projet permet de contrôler le personnage dans un jeu Minecraft en bougeant dans la réalité.

Casque qui appuie sur deux boutons à gauche et droite :
- fait bouger un mini-servo qui déplace un une plaque sous la souris
- fait la rotation du personnage dans Minecraft

Un boutons dans chaque main : 
- gauche: fait bouger un mini-servo qui appuie sur le bouton droit de la souris pendant 0.2s
- détruit un bloc
- droit: fait bouger un mini-servo qui appuie sur le bouton gauche de la souris
- crée un bloc

Une plaque sous les pieds avec deux boutons: 
- si les deux boutons sont alterné
- on appuie 'virtuellement' sur la touche 'w' du clavier en utilisant le module 'autogui'
"""

import time
import pyautogui
import RPi.GPIO as gpio
from time import sleep
from mcpi.minecraft import Minecraft


# Définition des boutons sur le GPIO

# Boutons pour avancer (plaque des pieds)
buttonL = 14
buttonR = 15

# Boutons pour créer et casser brique
buttonA = 23   # clique gauche souris, connecter à pwmL
buttonB = 24   # clique droit souris, connecter à pwmR

# Boutons pour la rotation du personnage, connectés à pwm
buttonC = 20
buttonD = 21


mc = Minecraft.create()
x, y ,z = mc.player.getPos()

# Definition de fonctions

def monde_plat():
    """Créer un monde plat pour faciliter déplacement."""    
    mc.setBlocks(x-300 ,y , z-300 ,x+300 ,y,z+300 ,2 )
    mc.setBlocks(x-300, y+1, z-300, x+300, y+300, z+300, 0)
     

def arbre(a, b, c):
    """Créer un arbre basé sur la position actuelle du joueur."""
    mc.setBlocks(x+a, y, z+c ,x+a ,y+b,z+c ,17)
    mc.setBlocks(x+(a-2), y+b , z+(c-2) ,x+(a+2) ,y+b,z+(c+2) ,18)
    mc.setBlocks(x+(a-1) ,y+(b+1) , z+(c-1) ,x+(a+1) ,y+(b+1),z+(c+1) ,18)
    mc.setBlocks(x+a ,y+(b+2) , z+c ,x+a ,y+(b+2),z+c ,18)

def foret():
    """Crée une forêt avec 12 arbres."""
    arbre(6, 4, 4)
    arbre(10, 3, 4)
    arbre(20,4,8)
    arbre(3,8,9)
    arbre(5,9,9)
    arbre(7,7,7)
    arbre(3,9,67)
    arbre(50,10,34)
    arbre(65,3,56)
    arbre(34,13,90)
    arbre(90,7,45)
    arbre(27,8,74)
    arbre(78,4,5)

def init_boutons():
    """Initialisation des 6 boutons en pull-up."""
    gpio.setmode(gpio.BCM) # Mode du GPIO
    gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(buttonR, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(buttonA, gpio.IN, pull_up_down=gpio.PUD_UP)    
    gpio.setup(buttonB, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(buttonC, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(buttonD, gpio.IN, pull_up_down=gpio.PUD_UP)

# Initialisation de l'état précédent des boutons
L0 = False 
R0 = False
A0 = False 
B0 = False 
C0 = False
D0 = False

##Installation Servo

def init_servos():
    """Initialiser les servo-moteurs."""
    #Servo pour rotation du personnage, connecté à boutons C et D
    gpio.setup(2, gpio.OUT)
    pwm = gpio.PWM(2, 50)

    # Servo pour clique gauche, connecté à bouton A
    gpio.setup(18, gpio.OUT)
    pwmL = gpio.PWM(18, 50)

    # Servo pour clique droit, connecté à bouton B
    gpio.setup(13, gpio.OUT)
    pwmR = gpio.PWM(13, 50)

    ##Etat de base des servo
    pwmL.start(4)# Position  de base du servo pwmL
    pwmR.start(8)#  Etat de base du servo pwmR

    x = 7.5
    pwm.start(x)

##  Code avancer buttons

init_boutons()
init_servos()
monde_plat()
foret()

t0 = time.time()

while True:
    sleep(0.05)
##    t = time.time()
##    print(t-t0)
##    t0 = t
    
    L = gpio.input(buttonL)
    R = gpio.input(buttonR)

    if not L and L0:
        pyautogui.keyDown('w')
    if L and not L0:
        pyautogui.keyUp('w')	
    L0 = L
    
    
    if not R and R0:
        pyautogui.keyDown('w')
    if R and not R0:
        pyautogui.keyUp('w')	
    R0 = R


## Code créer et casser brique avec servo pwmL et pwmR button A et button B

    A = gpio.input(buttonA)
    B = gpio.input(buttonB)

# clique gauche de la souris, casser une brique

    if not A and A0:
        pwmL.ChangeDutyCycle(2.5)
        time.sleep(0.5)
        pwmL.ChangeDutyCycle(4)
    if A and not A0:
        pass	    
    A0 = A
    
# clique droite de la souris, créer une brique

    if not B and B0:
        pwmR.ChangeDutyCycle(11)
        time.sleep(0.75)
        pwmR.ChangeDutyCycle(8)
    if B and not B0:
        pass    
    B0 = B
    

## code rotation personnage pwm et buttonC et buttonD

    C = gpio.input(buttonC)
    D = gpio.input(buttonD)

### tire le miservo vers 12.5

    if not C and C0 and x < 12.5:
        pwm.ChangeDutyCycle(x+2.5)
        x = x+2.5
    if C and not C0:
            pass 
    C0 = C

    # tire le mini servo vers 2.5
    
    if not D and D0 and x > 2.5:
        pwm.ChangeDutyCycle(x-2.5)
        x = x-2.5
    if D and not D0:
        pass		
    D0 = D