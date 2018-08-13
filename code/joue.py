""" This module start and stop the game
It describes the routine call each time a key is pressed"""

from initdisplay import initialisation
from initdisplay import LabOne
from initdisplay import Max
from initdisplay import MacGyver
from initdisplay import continuer
from initdisplay import display_all

import pygame
from pygame.locals import *
pygame.init()


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
        if (event.type == QUIT) or (MacGyver.res.data != 2):            #End the loop if QUIT (QUIT = manually close the window)
            continuer = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            routine(1)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            routine(2)
        elif event.type == KEYDOWN and event.key == K_UP:
            routine(3)
        elif event.type == KEYDOWN and event.key == K_DOWN:
            routine(4)
