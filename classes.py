import pygame
from constants import *
pygame.font.init()

class Square: 
    #Constants
    color = SQUARE_COLOR
    width = SQUARE_SIZE
    height = SQUARE_SIZE

    def __init__(self, x, y, text = ""):
        # x,y position; text equals value
        self.x = x
        self.y = y
        self.text = text
        self.value = None
    
    def draw(self, win):
        #call this method to draw the square on the screen 
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), width = SQUARE_BORDER)

        if self.text != "":
            font = pygame.font.SysFont('comicsans', 35)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos):
        #This function returns true, if the cursor is currently right on the square
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
    def highlight(self):
        self.color = (255,0,0)
    
    def unhighlight(self):
        self.color = SQUARE_COLOR
    
    def write_value(self, val):
        self.value = val
        self.text = str(val)
    



