""" This module start and stop the game
It describes the routine call each time a key is pressed"""

import pygame
from pygame.locals import *

from initialise import initialisation
from initialise import LabOne
from initialise import Max
from initialise import MacGyver
from initialise import continuer
from initialise import display_all


def routine(i):
    """reset the window : The technique is to put the window picture
    overhead others images, in the precedent position"""
    #move MacGyver managing collosion
    MacGyver.move(i, LabOne, Max)
    #Display
    display_all()

initialisation()

while continuer:
    for event in pygame.event.get():      #To analyze all received events
        if event.type == QUIT:            #End the loop if QUIT (QUIT = manually close the window)
            continuer = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            routine(1)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            routine(2)
        elif event.type == KEYDOWN and event.key == K_UP:
            routine(3)
        elif event.type == KEYDOWN and event.key == K_DOWN:
            routine(4)
