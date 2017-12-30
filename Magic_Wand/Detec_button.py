# Authors:Albert et Ludovic
# Date: 30.12.2017

# Affiliation : Gymnase du Bugnon
# Année 2017-2018
# Classe : OC-Informatique

# ---------------------------------------

from  mcpi.minecraft import Minecraft

import RPi.GPIO as gpio
import time

mc = Minecraft.create()

## initial configurations
antirebond_time = 0.05

## pin numbers
button1 = 14
button2 = 15
button3 = 18
button4 = 23
button5 = 24

## Flags

flags={'button1':0,'button2':0,'button3':0,'button4':0,'button5':0}

## Blocks ID

ID ={'AIR':0,'STONE':1,'GRASS':2,'DIRT':3,'COBBELSTONE':4,'WOOD_PLANKS':5,'SAPLING ':6,'BEDROCK ':7,'WATER_FLOWING':8,'WATER_STATIONARY':9,'LAVA_FLOWING':10,'LAVA_STATIONARY':11,'SAND':12,'GRAVEL':13,'GOLD_ORE':14,'IRON_ORE':15,'COAL_ORE':16,'WOOD':17,'LEAVES':18,'GLASS':20,'LAPIS_LAZULI_ORE':21,'LAPIS_LAZULI_BLOCK':22,'SANDSTONE':24,'BED':26,'COBWEB':30,'GRASS_TALL':31,'WOOL':35,'FLOWER_YELLOW':37,'FLOWER_CYAN':38,'MUSHROOM_BROWN':39,'MUSHROOM_RED':40,'GOLD_BLOCK':41,'IRON_BLOCK':42,'STONE_SLAB_DOUBLE':43,'STONE_SLAB':44,'BRICK_BLOCK':45,'BRICK_BLOCK':46,'BOOKSHELF':47,'MOSS_STONE':48,'OBSIDIAN':49,'TORCH':50,'FIRE':51,'STAIRS_WOOD':53,'CHEST':54,'DIAMOND_ORE':56,'DIAMOND_BLOCK':57,'CRAFTING_TABLE':58,'FARMLAND':60,'FURNACE_INACTIVE':61,'FURNACE_ACTIVE':62,'DOOR_WOOD':64,'LADDER ':65,'STAIRS_COBBLESTONE':67,'DOOR_IRON':71,'REDSTONE_ORE':73,'SNOW':78,'ICE':79,'SNOW_BLOCK':80,'CACTUS':81,'CLAY':82,'SUGAR_CANE':83,'FENCE':85,'GLOWSTONE_BLOCK':89,'BEDROCK_INVISIBLE':95,'STONE_BRICK':98,'GLASS_PANE':102,'MELON':103,'FENCE_GATE':107,'GLOWING_OBSIDIAN':246,'NETHER_REACTOR_COR':247}


gpio.setmode(gpio.BCM)

def button_setup(nb):
    gpio.setup(eval(nb), gpio.IN, pull_up_down=gpio.PUD_UP)

def button_fct_pressed(nb):
    if  not gpio.input(eval(nb)) and flags[nb]==0:
        flags[nb]=1
        time.sleep(antirebond_time)
        return
    if (flags[nb]== 1 or flags[nb]==' ') and not gpio.input(eval(nb)):
        flags[nb] = ' '
        return
    
    if (flags[nb]==' ' or flags[nb]==1 )and gpio.input(eval(nb)):          
        flags[nb]=0
        return

def check_buttons_fct():
    button_fct_pressed('button1')
    button_fct_pressed('button2')
    button_fct_pressed('button3')
    button_fct_pressed('button4')
    button_fct_pressed('button5')

button_setup('button1')
button_setup('button2')
button_setup('button3')
button_setup('button4')
button_setup('button5')

while True:
    check_buttons_fct()
    if flags['button1']==True:
        mc.postToChat("You've pressed button1")
    if flags['button2']==True:
        mc.postToChat("You've pressed button2")
    if flags['button3']==True:
        mc.postToChat("You've pressed button3")
    if flags['button4']==True:
        mc.postToChat("You've pressed button4")
    if flags['button5']==True:
        mc.postToChat("You've pressed button5")

    #print(flags['button1'],flags['button2'],flags['button3'],flags['button4'],flags['button5'])

