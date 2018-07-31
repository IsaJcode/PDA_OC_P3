""" This module provides all classes used in the code"""
import random
import pygame
from pygame.locals import *

class Visitor:
    """
        Describes any element in the lab
    """	
    def __init__(self, pic, pos):
        #Set visitor position and picture
        self.posX = pos[0]
        self.posY = pos[1]
        self.picture = pic

    def display(self, window):
        #Display the visitor picture
        window.blit(self.picture, (self.posX, self.posY))
        return None

class Garde(Visitor):
#Gardian class descriptor
    def __init__(self, pic, lab):
    # A Gard is a Visitor initially at the labyrinth exit
        Visitor.__init__(self, pic, lab.exit)

    def collision_garde(self, pos):
    #McGyver meet the gardian or not?
        return pos == (self.posX, self.posY)


class Player(Visitor):
    #McGyver class descriptor
    def __init__(self, pic, lab, result):
        # A player is a Visitor initially at the labyrinth entry
        # He should pick objects and display a result at the end of the game
        Visitor.__init__(self, pic, lab.entry)
        self.nbElemtPick = 0
        self.res = result

    def new_position(self, direction):
        #Compute a new position according to keyboard entry
        if direction == 1:# K_LEFT
            newX = self.posX - 32
            newY = self.posY

        elif direction == 2:# K_RIGHT
            newX = self.posX + 32
            newY = self.posY

        elif direction == 3:# K_UP
            newX = self.posX
            newY = self.posY - 32

        elif direction == 4:# K_DOWN
            newX = self.posX
            newY = self.posY + 32
        return (newX, newY)

    def move(self, direction, lab, gard):
        #manage player position in the labyrinth and collisions
        newPos = self.new_position(direction) # McGyver want take a new position
        go = lab.collision_lab(newPos) # McGyver try to take a new position in the lab

        if go: # McGyver has moved
            #Update position
            self.posX = newPos[0]
            self.posY = newPos[1]

            if gard.collision_garde(newPos):   #McGyver meet the gardian
                self.res.data = self.nbElemtPick == 4  #McGyver fight the gardian

            elif Element.collision_elt(newPos, self.nbElemtPick): #McGyver reach an object
                self.nbElemtPick += 1                                     #McGyver take an object
        return None

    def display_res(self, window):
        # display the player result
        self.res.display(window)
        return None

class result:
    #result class descriptor
    def __init__(self, imOk, imNok):
        #set different result picture, position to display
        #and initilise a n		
        self.ok = imOk
        self.nok = imNok
        self.position = (100, 100)
        self.data = 2 #Not yet defined
        return None

    def display(self, window):
    #display the result
        if self.data == 1:
            window.blit(self.ok, self.position)
        elif self.data == 0:
            window.blit(self.nok, self.position)
        return None

class Labi:
    #class representing the labyrinth object
    def __init__(self, lev, im):
	    #set the entry, the exit, free and unfree position list,
        #wall labyrinth picture and the level of the game which is the labyrinth configuration
        self.level = lev         #game level
        self.entry = (0, 0)        #labyrinth entry position
        self.exit = (448, 448)    #labyrinth exit position
        self.list = list()         #For the list of not available positions (wall)
        self.lib = list()         #For the list of available positions
        self.picture = im       #image for the wall

        #To initialise the list of available and not available positions
        abs = 0
        ord = 0
        for elt in self.level:
            #In the level, m represent the wall
            if elt == "m":
                self.list.append((abs, ord))
                abs += 32

            #In the level, 0 represent the place for moving
            elif  elt == "0":
                self.lib.append((abs, ord))
                abs += 32

            #In the level, " " represent the edge
            elif elt == " ":
                abs = 0
                ord += 32

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

    def collision_lab(self, pos):
    #The movement is possible if the new position is not an edge or a wall position
        movement = True
        #Collision with the edge
        if (pos[0] < 0) or (pos[0] > 448) or (pos[1] < 0) or (pos[1] > 448):
            movement = False

        #Collision with labyrinth wall
        if movement:
            for elt in self.list:
                if pos == elt:
                    movement = False
        return movement


class Element(Visitor):
    #Class for all elements to pick necessarily to win
    listOutLab = list() #For the list of elements out of the labyrinth
    listInLab = list()  #For the list of elements inside the labyrinth
    nbElts = 0 # Number of created elements

    def __init__(self, lab, picture):
        #An element is a Visitor, when it is created, the number of created elements and the list of elements
        #inside the labyrinth is increased
        if Element.nbElts < 4:  #Number of elements is limited to 4
            Visitor.__init__(self, picture, lab.new_pos_elt())
            Element.listInLab.append(self)
            Element.nbElts += 1
        return None

    @classmethod
    def collision_elt(cls, pos, i):
    #method of the class to put element out of the labyrinth if MacGyver reachs it
        find = False
        for elt in cls.listInLab:
            if pos == (elt.posX, elt.posY): #MacGyver reachs an object
                find = True
                elt.posX = 512 #position out of the labyrinth
                elt.posY = i*32
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
