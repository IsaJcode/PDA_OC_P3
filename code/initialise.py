from team import *
from level import *

import pygame
from pygame.locals import *
pygame.init()

#Load image

fenetre = pygame.display.set_mode((580, 480)) #480 = 15 * 32 , the size image should be 32
tableau = pygame.image.load("ressource/Sable.jpg").convert()
fond = pygame.image.load("ressource/Sea.jpg").convert() 

personnage = pygame.image.load("ressource/MacGyver.png").convert_alpha()
mur = pygame.image.load("ressource/mur.jpg").convert_alpha()
aiguille = pygame.image.load("ressource/aiguille.png").convert_alpha()
seringue = pygame.image.load("ressource/seringue.png").convert_alpha()
tube = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
ether = pygame.image.load("ressource/ether.png").convert_alpha()
gardien = pygame.image.load("ressource/Gardien.png").convert_alpha()
top = pygame.image.load("ressource/Top.jpg").convert_alpha()
down = pygame.image.load("ressource/Down.jpg").convert_alpha()

#Creation of objets
LabOne = labi(level, mur)

Elt1 = Element(LabOne, aiguille)
Elt2 = Element(LabOne, ether)
Elt3 = Element(LabOne, tube)
Elt4 = Element(LabOne, seringue)

Max = Garde(gardien, LabOne)
res = result (top, down)
MacGyver = Player(personnage, LabOne, res)


#Display elements in initial position
fenetre.blit(tableau, (0,0))
fenetre.blit(fond, (0,0))
LabOne.display_labi(fenetre)
MacGyver.display(fenetre)
Element.display_all_elts(fenetre)
Max.display(fenetre)
pygame.display.flip() #Necessary to refresh the game window