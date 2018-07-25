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
		
		
	def collision_garde (self, pos):    
    #McGyver meet the gardian or not? 
        return pos == (self.pos_X, self.pos_Y)
		
		
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