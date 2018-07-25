fenetre = pygame.display.set_mode((580, 480)) #480 = 15 * 32 , the size image should be 32

def display(self, window):
#display the visitor picture
    window.blit(self.picture, (self.pos_X , self.pos_Y))
    return None
		
def display(self, window):
#display result pictiure
    if self.data == 1:
        window.blit(self.ok, self.position)
    elif self.data == 0:
        window.blit(self.Nok, self.position)
    return None
		
def display_labi(self, window):
#display labyrinth from the list of not available position
    for elt in self.list:
        window.blit(self.picture, elt) 
    return None