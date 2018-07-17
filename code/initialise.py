from team import *
from level import *

import pygame
from pygame.locals import *
pygame.init()

#Load image

fenetre = pygame.display.set_mode((580, 480)) #480 = 15 * 32 , the size image should be 32
tableau = pygame.image.load("Sable.jpg").convert()
fond = pygame.image.load("Sea.jpg").convert() 

personnage = pygame.image.load("MacGyver.png").convert_alpha()
mur = pygame.image.load("mur.jpg").convert_alpha()
aiguille = pygame.image.load("aiguille.png").convert_alpha()
seringue = pygame.image.load("seringue.png").convert_alpha()
tube = pygame.image.load("tube_plastique.png").convert_alpha()
ether = pygame.image.load("ether.png").convert_alpha()
gardien = pygame.image.load("Gardien.png").convert_alpha()
top = pygame.image.load("Top.jpg").convert_alpha()
down = pygame.image.load("Down.jpg").convert_alpha()

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