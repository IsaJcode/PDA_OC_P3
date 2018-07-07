import random
import pygame
from pygame.locals import * # Q1: pourquoi on importe un bout de code alors qu on a deja tout importe?

import niveau
from niveau import *

pygame.init()

fenetre = pygame.display.set_mode((580, 480)) #480 = 15 * 32 mon image doit donc faire 32
tableau = pygame.image.load("Sable.jpg").convert()
fond = pygame.image.load("Sea.jpg").convert() 
#fenetre.blit(fond, (0,0))

personnage = pygame.image.load("MacGyver.png").convert_alpha()
mur = pygame.image.load("mur.jpg").convert_alpha()
aiguille = pygame.image.load("aiguille.png").convert_alpha()
seringue = pygame.image.load("seringue.png").convert_alpha()
tube = pygame.image.load("tube_plastique.png").convert_alpha()
ether = pygame.image.load("ether.png").convert_alpha()
gardien = pygame.image.load("Gardien.png").convert_alpha()
top = pygame.image.load("Top.jpg").convert_alpha()
down = pygame.image.load("Down.jpg").convert_alpha()

class Personnage :
	def __init__ (self, tof, lab, resultat) :
		self.pos_X = lab.entree[0]
		self.pos_Y = lab.entree[1]
		self.image = tof
		self.NbElemtPris = 0
		self.res = resultat
		
	#Collision labyrinthe:	
	def CollLab (self, direction, lab):
		if(direction == 1):# K_LEFT
			deplacement = True
			Old_x = self.pos_X
			self.pos_X -= 32
			if self.pos_X < 0:
				self.pos_X = 0
				deplacement = False
				
			else:	
				for elt in lab.list:
					if (self.pos_X, self.pos_Y) == elt:
						deplacement = False
						self.pos_X = Old_x
		
		elif(direction == 2):# K_RIGHT
			deplacement = True
			
			Old_x = self.pos_X
			self.pos_X += 32 
			
			if self.pos_X > 448:
				self.pos_X = 448
				deplacement = False
				
			else:	
				for elt in lab.list:
					if (self.pos_X, self.pos_Y) == elt:
						deplacement = False
						self.pos_X = Old_x
				
		elif(direction == 3):# K_UP
			deplacement = True
			
			Old_y = self.pos_Y
			self.pos_Y -= 32
			if self.pos_Y < 0:
				self.pos_Y = 0
				deplacement = False
				
			else:	
				for elt in lab.list:
					if (self.pos_X, self.pos_Y) == elt:
						deplacement = False
						self.pos_Y = Old_y
		
		elif(direction == 4):# K_DOWN
			deplacement = True		
			Old_y = self.pos_Y
			self.pos_Y+= 32
			
			if self.pos_Y > 448:
				self.pos_Y = 448
				deplacement = False
				
			else:	
				for elt in lab.list:
					if (self.pos_X, self.pos_Y) == elt:
						deplacement = False
						self.pos_Y = Old_y
		
		return deplacement
		
	
	def seDeplacer (self, direction, lab, elts):
		Go = self.CollLab(direction, lab)
		if Go == True: #affiche m indique si McGyver s est deplace
			if ((self.pos_X, self.pos_Y) == lab.sortie): #McGyver est a la sortie
				if self.NbElemtPris == 4:
					self.res.data = 1 #McGyver sort vivant
				else:
					self.res.data = 0  #Desolee pour McGyver
			else: #McGyver n est pas encore a la sortie
				for i in range(0,4):
					if ((self.pos_X , self.pos_Y) == elts.listePosition[i]): #si j ai atteint un objet, je change la position de cet objet en le mettant dans mon tableau
						elts.pris(i)
						self.NbElemtPris += 1
		return None
	
	def affiche(self):
		fenetre.blit(self.image, (self.pos_X , self.pos_Y))
		return None
		
	def afficheRes(self):
		self.res.affiche()
		return None

class result:
	def __init__(self, imOk, imNok):
		self.ok = imOk
		self.Nok = imNok
		self.position = (100, 100)
		self.data = 2 #Not yet defined
		return None
		
	def affiche(self):
		if self.data == 1:
			fenetre.blit(self.ok, self.position)
		elif self.data == 0:
			fenetre.blit(self.Nok, self.position)
		return None
	
class labi :

	def __init__(self, niv, im):
		self.niveau = niv
		self.entree = (0,0)
		self.sortie = (448, 448)
		self.list = list()
		self.lib = list ()
		self.image = im
		
		n = 0
		p=0
		for elt in self.niveau:
			if elt == "m": 
				self.list.append((n,p))
				n+=32
			
			elif  elt == "0":
				self.lib.append((n,p))
				n+=32
			
			elif elt == " ":
				n=0
				p+=32
		return None
	
	def afficheLabi(self):
		for elt in self.list:
			fenetre.blit(self.image, elt) 
		return None

	
class Elements:

	def __init__(self, lab, aig, et, tub, serg):
	
		self.Imaiguille = aig
		self.Imether = et
		self.Imtube = tub
		self.Imseringue = serg
	
		self.listePosition = list()
		liste = lab.lib
		liste.remove(lab.entree)
		liste.remove(lab.sortie)
	
		position1 = random.choice(liste)
		self.listePosition.append(position1)
		liste.remove(position1)

		position2 = random.choice(liste)
		self.listePosition.append(position2)
		liste.remove(position2)

		position3 = random.choice(liste)
		self.listePosition.append(position3) 
		liste.remove(position3)

		position4 = random.choice(liste)
		self.listePosition.append(position4)
	
		return None

	def affiche(self):
		fenetre.blit(self.Imaiguille, self.listePosition[0]) 
		fenetre.blit(self.Imether, self.listePosition[1]) 
		fenetre.blit(self.Imtube, self.listePosition[2]) 
		fenetre.blit(self.Imseringue, self.listePosition[3]) 
		return None
	
	def pris(self,i):
		self.listePosition [i] = (512, i*32)
		return None
		
class Garde:
	def __init__ (self, tof, lab) :
		self.position = lab.sortie
		self.image = tof

	def affiche(self):
		fenetre.blit(self.image, self.position)
		return None
		