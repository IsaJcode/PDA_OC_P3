""" This module provides all constants used in the code"""
import pygame
import os

#LEVEL provides a string whih describes the labyrinth
#0 represent free place
#m reprensent the wall

LEVEL = open("level.txt", "r").read() #the game level can be easily configured in level.txt
STARTPOINT = (0, 0)
STOPPOINT = (448, 448)

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
