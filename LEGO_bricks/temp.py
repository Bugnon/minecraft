
# Importation du module pour acceder au GPIO
import RPi.GPIO as gpio
import time

# Flag
# 0  = relache
# 1  = en train d'etre appuye
# ' ' = appuye
alreadySaidReset = False
flag = 0
# Time flag : Sauvegarde le temps de pression
time_flag = 0

antirebond_time = 0.20
# Pin sur le GPIO
button = 14

# ---------------------------------------
# Gpio initalisation
# ---------------------------------------
gpio.setmode(gpio.BCM)
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_UP)

def button_fct_pressed():
    """Test si le bouton est appuye, relache ou en train d'etre appuye.
modifie le flag du bouton :
        -0  = relache
        -1  = appuye
        -' ' = juste relâché
"""
    global flag
    global time_flag
    global button
    global antirebond_time

    pressed = not gpio.input(button)
    last_pressed = flag == 1
    
    if pressed:
        if time_flag == 0:
            flag = 1
            time_flag = time.time()
    elif time.time() - time_flag > antirebond_time:
        if last_pressed:
            flag = ' '
        else :
            flag = 0
            time_flag = 0

while True :
    button_fct_pressed()
    if flag == ' ':
        print("PRESSED ! : " + str(time.time() - time_flag))
        alreadySaidReset = False
    elif flag == 1 :
        if(time_flag != 0 and time.time() - time_flag > 4 and not alreadySaidReset):
            print("Reset")
            alreadySaidReset = True