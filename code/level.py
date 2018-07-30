""" This module provides all constants used in the code"""
import pygame
from pygame.locals import *
pygame.init()

#LEVEL provides a string whih describes the labyrinth
#0 represent free place
#m reprensent the wall

LEVEL = "000mmmmm0m00mmm \
0m00000m0mm0m0m \
00mm0m000m0000m \
m000mmmm000mm0m \
000m00000mmm00m \
mm0mmmm0mm000mm \
000mmm0000mmmmm \
0m000mm0m0mm00m \
0mm0m000m0000mm \
mmm00mmmm0mmmmm \
mmm0mm0m00mm00m \
m000m00m0mm00mm \
00mm00000000mmm \
mmmmm0mm0mm0mmm \
m00000mm00m0000 "

#Window creation
FENETRE = pygame.display.set_mode((580, 480)) #480 = 15 * 32 , the size image should be 32

#Load image
TABLEAU = pygame.image.load("ressource/Sable.jpg").convert()
FOND = pygame.image.load("ressource/Sea.jpg").convert()
PERSONNAGE = pygame.image.load("ressource/MacGyver.png").convert_alpha()
MUR = pygame.image.load("ressource/mur.jpg").convert_alpha()
AIGUILLE = pygame.image.load("ressource/aiguille.png").convert_alpha()
SERINGUE = pygame.image.load("ressource/seringue.png").convert_alpha()
TUBE = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
ETHER = pygame.image.load("ressource/ether.png").convert_alpha()
GARDIEN = pygame.image.load("ressource/Gardien.png").convert_alpha()
TOP = pygame.image.load("ressource/Top.jpg").convert_alpha()
DOWN = pygame.image.load("ressource/Down.jpg").convert_alpha()
