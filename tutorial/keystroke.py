import pygame, sys
from pygame.locals import *

pygame.init()
WIDTH = 100
HEIGHT = 100

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.guit()
            sys.exit()
        elif event.type == KEYDOWN:
            key = event.key
            print(key)