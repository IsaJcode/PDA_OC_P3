import pygame
from pygame.locals import * # Q1: pourquoi on importe un bout de code alors qu on a deja tout importe?

from viewLab import *

import niveau
from niveau import *

pygame.init()


#Choix des positions
LabOne = labi(niveau, mur)
Elts = Elements(LabOne, aiguille, ether, tube, seringue)
Max = Garde(gardien, LabOne)
res = result (top, down)
MacGyver = Personnage(personnage, LabOne, res)


#Affichage des elements en position initiale
fenetre.blit(tableau, (0,0))
fenetre.blit(fond, (0,0))
LabOne.afficheLabi()
MacGyver.affiche()
Elts.affiche()
Max.affiche()
pygame.display.flip() #permet de rafraichir , sinon l affichage de la fenetre ne met pas a jour

continuer = 1


while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les evenements recus
		if event.type == QUIT:     #Si un de ces evenements est de type QUIT
			continuer = int(input())      #On arrete la boucle Q7: int(input()) ?
			
		elif event.type == KEYDOWN and event.key == K_LEFT:
			fenetre.blit(fond, (0,0)) #on recolle la fenetre au dessus du personnage dans la position precedente
			LabOne.afficheLabi()
			MacGyver.seDeplacer(1, LabOne, Elts)
			
			MacGyver.affiche()
			Elts.affiche()
			Max.affiche()
			MacGyver.afficheRes()
			pygame.display.flip()  # on rafraichit la fenetre
			
		elif event.type == KEYDOWN and event.key == K_RIGHT:
			fenetre.blit(fond, (0,0))
			LabOne.afficheLabi()
			MacGyver.seDeplacer(2, LabOne, Elts)
			
			MacGyver.affiche()
			Elts.affiche()
			Max.affiche()
			MacGyver.afficheRes()		
			pygame.display.flip() 
			
		elif event.type == KEYDOWN and event.key == K_UP:
			fenetre.blit(fond, (0,0))
			LabOne.afficheLabi()
			MacGyver.seDeplacer(3, LabOne, Elts)
			
			MacGyver.affiche()
			Elts.affiche()
			Max.affiche()
			MacGyver.afficheRes()
			pygame.display.flip() 
			
		elif event.type == KEYDOWN and event.key == K_DOWN:
			fenetre.blit(fond, (0,0))
			LabOne.afficheLabi()			
			MacGyver.seDeplacer(4, LabOne, Elts)

			MacGyver.affiche()
			Elts.affiche()
			Max.affiche()
			MacGyver.afficheRes()			
			pygame.display.flip() 