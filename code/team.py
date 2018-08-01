""" This module provides all classes used in the code"""
import random
#import pygame is not needed because theses class are used by
#module which import pygame

class Visitor:
    """
        Describes any element in the lab
    """
    def __init__(self, pic, pos): #Pylint : put a docstring method reach to an error
        #Set visitor position and picture
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.picture = pic

    def display(self, window):
        #Display the visitor picture
        window.blit(self.picture, (self.pos_x, self.pos_y))

class Garde(Visitor):
    """
        Gardian class descriptor
    """
    def __init__(self, pic, lab):
        # A Gard is a Visitor initially at the labyrinth exit
        Visitor.__init__(self, pic, lab.exit)

    def collision_garde(self, pos):
        #McGyver meet the gardian or not?
        return pos == (self.pos_x, self.pos_y)


class Player(Visitor):
    """
        McGyver class descriptor
    """
    def __init__(self, pic, lab, result):
        # A player is a Visitor initially at the labyrinth entry
        # He should pick objects and display a result at the end of the game
        Visitor.__init__(self, pic, lab.entry)
        self.nb_elemt_pick = 0
        self.res = result

    def new_position(self, direction):
        #Compute a new position according to keyboard entry
        if direction == 1:# K_LEFT
            new_x = self.pos_x - 32
            new_y = self.pos_y

        elif direction == 2:# K_RIGHT
            new_x = self.pos_x + 32
            new_y = self.pos_y

        elif direction == 3:# K_UP
            new_x = self.pos_x
            new_y = self.pos_y - 32

        elif direction == 4:# K_DOWN
            new_x = self.pos_x
            new_y = self.pos_y + 32
        return (new_x, new_y)

    def move(self, direction, lab, gard):
        #manage player position in the labyrinth and collisions
        new_pos = self.new_position(direction) # McGyver want take a new position
        go = lab.collision_lab(new_pos) # McGyver try to take a new position in the lab

        if go: # McGyver has moved
            #Update position
            self.pos_x = new_pos[0]
            self.pos_y = new_pos[1]

            if gard.collision_garde(new_pos):   #McGyver meet the gardian
                self.res.data = self.nb_elemt_pick == 4  #McGyver fight the gardian

            elif Element.collision_elt(new_pos, self.nb_elemt_pick): #McGyver reach an object
                self.nb_elemt_pick += 1                                     #McGyver take an object

    def display_res(self, window):
        # display the player result
        self.res.display(window)

class Result:
    """
        result class descriptor
    """
    def __init__(self, im_ok, im_nok):
        #set different result picture, position to display
        #and initilise a n
        self.ok = im_ok
        self.nok = im_nok
        self.position = (100, 100)
        self.data = 2 #Not yet defined

    def display(self, window):
        #display the result
        if self.data == 1:
            window.blit(self.ok, self.position)
        elif self.data == 0:
            window.blit(self.nok, self.position)

class Labi:
    """
        class representing the labyrinth object
    """
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

    def display_labi(self, window):
        #display labyrinth from the list of not available position
        for elt in self.list:
            window.blit(self.picture, elt)

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
    """
        Class for all elements to pick necessarily to win
    """
    list_out_lab = list() #For the list of elements out of the labyrinth
    list_in_lab = list()  #For the list of elements inside the labyrinth
    nb_elts = 0 # Number of created elements

    def __init__(self, lab, picture):
        #An element is a Visitor, when it is created, the number of created
		#elements and the list of elements inside the labyrinth is increased
        if Element.nb_elts < 4:  #Number of elements is limited to 4
            Visitor.__init__(self, picture, lab.new_pos_elt())
            Element.list_in_lab.append(self)
            Element.nb_elts += 1

    @classmethod
    def collision_elt(cls, pos, i):
        #method of the class to put element out of the labyrinth if MacGyver reachs it
        find = False
        for elt in cls.list_in_lab:
            if pos == (elt.pos_x, elt.pos_y): #MacGyver reachs an object
                find = True
                elt.pos_x = 512 #position out of the labyrinth
                elt.pos_y = i*32
				#The element is put in the list of elements out of the labyrinth
                Element.list_out_lab.append(elt)
				#The element is removed from the list of elements inside the labyrinth
                Element.list_in_lab.remove(elt)
        return find

    @classmethod
    def display_all_elts(cls, window):
	    #method of the class to display all elements
        for elt in cls.list_in_lab: # To display all elements located inside the labyrinth
            elt.display(window)

        for elt in cls.list_out_lab: #To display all elements located outside the labyrinth
            elt.display(window)

