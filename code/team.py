""" This module provides all classes used in the code"""
import random
import pygame
from pygame.locals import *

class Visitor:
    def __init__ (self, pic, pos) :
        self.pos_X = pos[0]
        self.pos_Y = pos[1]
        self.picture = pic

    def display(self, window):
    #Display the visitor picture
        window.blit(self.picture, (self.pos_X , self.pos_Y))
        return None
        
		
class Garde(Visitor):
    def __init__ (self, pic, lab) :
    # A Gard is a Visitor initially at the labyrinth exit
        Visitor.__init__(self, pic, lab.exit)
        
    def collision_garde (self, pos):    
    #McGyver meet the gardian or not? 
        return pos == (self.pos_X, self.pos_Y)

        
class Player(Visitor) :
    def __init__ (self, pic, lab, result) :
    # A player is a Visitor initially at the labyrinth entry
    # He should pick objects and display a result at the end of the game
        Visitor.__init__(self, pic, lab.entry)
        self.NbElemtPick = 0
        self.res = result
        
    def new_position (self, direction):
    #Compute a new position according to keyboard entry
        if(direction == 1):# K_LEFT
            NewX = self.pos_X -32
            NewY = self.pos_Y
        
        elif(direction == 2):# K_RIGHT
            NewX = self.pos_X +32
            NewY = self.pos_Y            
                    
        elif(direction == 3):# K_UP
            NewX = self.pos_X 
            NewY = self.pos_Y -32
        
        elif(direction == 4):# K_DOWN    
            NewX = self.pos_X 
            NewY = self.pos_Y +32
            
        return ((NewX,NewY))
    
    def move (self, direction, lab, gard):
        #manage player position in the labyrinth and collisions
        newPos = self.new_position (direction) # McGyver want take a new position
        Go = lab.collision_lab(newPos) # McGyver try to take a new position in the lab
        
        if Go == True: # McGyver has moved
        
            #Update position
            self.pos_X = newPos[0]
            self.pos_Y = newPos[1]
            
            if gard.collision_garde(newPos) == True:    #McGyver meet the gardian
                self.res.data = self.NbElemtPick == 4  #McGyver fight the gardian
                
            elif Element.collision_elt(newPos, self.NbElemtPick) == True: #McGyver reach an object
                self.NbElemtPick += 1                                    #McGyver take an object
        return None
        
    def display_res(self, window):
    # display the player result
        self.res.display(window)
        return None

		
class result:
    def __init__(self, imOk, imNok):
        self.ok = imOk
        self.Nok = imNok
        self.position = (100, 100)
        self.data = 2 #Not yet defined
        return None
        
    def display(self, window):
    #
        if self.data == 1:
            window.blit(self.ok, self.position)
        elif self.data == 0:
            window.blit(self.Nok, self.position)
        return None
    
class Labi :

    def __init__(self, lev, im):
        self.level = lev         #game level
        self.entry = (0,0)        #labyrinth entry position
        self.exit = (448, 448)    #labyrinth exit position
        self.list = list()         #For the list of not available positions (wall)
        self.lib = list ()         #For the list of available positions
        self.picture = im       #image for the wall  
        
        #To initialise the list of available and not available positions
        n = 0
        p = 0
        for elt in self.level:
            #In the level, m represent the wall
            if elt == "m": 
                self.list.append((n,p))
                n+=32
                
            #In the level, 0 represent the place for moving
            elif  elt == "0":
                self.lib.append((n,p))
                n+=32
                
            #In the level, " " represent the edge
            elif elt == " ":
                n=0
                p+=32
        
        #Entry and exit are not available positions for elements        
        self.lib.remove(self.entry)
        self.lib.remove(self.exit)
        return None
    
    def display_labi(self, window):
    #display labyrinth from the list of not available position
        for elt in self.list:
            window.blit(self.picture, elt) 
        return None
        
    def new_pos_elt(self):
    #provide a new random position for element from the list of available positions
        position = random.choice(self.lib)
        self.lib.remove(position)
        return position
    
    def collision_lab (self, pos):
    #The movement is possible if the new position is not an edge or a wall position
        movement = True
        #Collision with the edge
        if (pos[0] < 0) or (pos[0] > 448) or (pos[1] < 0) or (pos[1] > 448):
            movement = False
        
        #Collision with labyrinth wall
        if  movement == True:
            for elt in self.list:
                if pos == elt:
                    movement = False
        return movement
    

class Element(Visitor): 
#Class for all elements to pick necessarily to win
    listOutLab = list() #For the list of elements out of the labyrinth
    listInLab = list()  #For the list of elements inside the labyrinth
    nbElts = 0 # Number of created elements
    
    def __init__(self, lab ,picture):
    #An element is a Visitor, when it is created, the number of created elements and the list of elements
    #inside the labyrinth is increased
        if Element.nbElts < 4:  #Number of elements is limited to 4
            Visitor.__init__(self, picture, lab.new_pos_elt())    
            Element.listInLab.append(self)
            Element.nbElts += 1
        return None
    
    @classmethod
    def collision_elt (cls, pos, i):
    #method of the class to put element out of the labyrinth if MacGyver reachs it
        find = False
        for elt in cls.listInLab:
            if (pos== (elt.pos_X , elt.pos_Y)): #MacGyver reachs an object    
                find = True
                
                elt.pos_X = 512 #position out of the labyrinth
                elt.pos_Y = i*32
                Element.listOutLab.append(elt) #The element is put in the list of elements out of the labyrinth
                Element.listInLab.remove(elt)  #The element is removed from the list of elements inside the labyrinth
        return find
    
    @classmethod
    #method of the class to display all elements
    def display_all_elts(cls, window):
        for elt in cls.listInLab: # To display all elements located inside the labyrinth
            elt.display(window)

        for elt in cls.listOutLab: #To display all elements located outside the labyrinth
            elt.display(window)            
        return None