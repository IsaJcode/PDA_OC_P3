class Garde(Visitor):
    def __init__ (self, pic, lab) :
    # A Gard is a Visitor initially at the labyrinth exit
        Visitor.__init__(self, pic, lab.exit)
		
#......		

class Player(Visitor) :
    def __init__ (self, pic, lab, result) :
    # A player is a Visitor initially at the labyrinth entry
    # He should pick objects and display a result at the end of the game
        Visitor.__init__(self, pic, lab.entry)
        self.NbElemtPick = 0
        self.res = result
		
#......

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

#......		
#Method from labi class		
    def new_pos_elt(self):
    #provide a new random position for element from the list of available positions
        position = random.choice(self.lib)
        self.lib.remove(position)
        return position