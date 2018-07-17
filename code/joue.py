""" This module start and stop the game
It describes the routine call each time a key is pressed"""

import pygame
from pygame.locals import *
from initialise import *
from team import *

continuer = 1

def routine(i):
    """reset the window : The technique is to put the window picture
    overhead others images, in the precedent position"""
    fenetre.blit(fond, (0, 0))
    #display the labyrinth
    LabOne.display_labi(fenetre)
    #move MacGyver managing collosion
    MacGyver.move(i, LabOne, Max)
    # display all MacGyver, elements and the gardian
    MacGyver.display(fenetre)
    Element.display_all_elts(fenetre)
    Max.display(fenetre)
    MacGyver.display_res(fenetre)
    pygame.display.flip()  #Necessary to refresh the game window

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
