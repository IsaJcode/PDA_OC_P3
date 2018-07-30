""" This module create all objets used in the code and provides display functions"""
from team import Labi
from team import Element
from team import Player
from team import result
from team import Garde
from level import *

#Creation of objets
LabOne = Labi(LEVEL, MUR)

Elt1 = Element(LabOne, AIGUILLE)
Elt2 = Element(LabOne, ETHER)
Elt3 = Element(LabOne, TUBE)
Elt4 = Element(LabOne, SERINGUE)

Max = Garde(GARDIEN, LabOne)
res = result(TOP, DOWN)
MacGyver = Player(PERSONNAGE, LabOne, res)
continuer = 1



def initialisation():
    """Display elements in initial position"""
    FENETRE.blit(TABLEAU, (0, 0))
    FENETRE.blit(FOND, (0, 0))
    LabOne.display_labi(FENETRE)
    MacGyver.display(FENETRE)
    Element.display_all_elts(FENETRE)
    Max.display(FENETRE)
    pygame.display.flip() #Necessary to refresh the game window

def display_all():
    """Display elements in update position"""
    FENETRE.blit(FOND, (0, 0))
    #display the labyrinth
    LabOne.display_labi(FENETRE)
    # display all MacGyver, elements and the gardian
    MacGyver.display(FENETRE)
    Element.display_all_elts(FENETRE)
    Max.display(FENETRE)
    MacGyver.display_res(FENETRE)
    pygame.display.flip()  #Necessary to refresh the game window
