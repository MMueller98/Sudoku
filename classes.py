import pygame
from constants import *
pygame.font.init()

class Square: 
    #Constants
    color = SQUARE_COLOR
    width = SQUARE_SIZE
    height = SQUARE_SIZE

    def __init__(self, x, y, row, col, text = ""):
        # x,y position; text equals value
        self.x = x
        self.y = y
        self.row = row
        self.col = col
        self.text = text
        self.value = None
        self.super_square = None
        self.set_flag = False

        #Assign number of super-square -> 3x3 square, where every num has to be in
        if(row == 1 or row == 2 or row == 3):
            if(col == 1 or col == 2 or col == 3):
                self.super_square = [0,0]
            if(col == 4 or col == 5 or col == 6):
                self.super_square = [0,3]
            if(col == 7 or col == 8 or col == 9):
                self.super_square = [0,6]
        if(row == 4 or row == 5 or row == 6):
            if(col == 1 or col == 2 or col == 3):
                self.super_square = [3,0]
            if(col == 4 or col == 5 or col == 6):
                self.super_square = [3,3]
            if(col == 7 or col == 8 or col == 9):
                self.super_square = [3,6]
        if(row == 7 or row == 8 or row == 9):
            if(col == 1 or col == 2 or col == 3):
                self.super_square = [6,0]
            if(col == 4 or col == 5 or col == 6):
                self.super_square = [6,3]
            if(col == 7 or col == 8 or col == 9):
                self.super_square = [6,6]
    
    def draw(self, win):
        #Call this method to draw the square on the screen 
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
    
    def highlight(self, color):
    #Highlight a square of Sudoku board
        self.color = color
    
    def unhighlight(self):
    #Highlight a square of Sudoku board
        self.color = SQUARE_COLOR
    
    def write_value(self, val):
    #Write a value in a square of the sudoku board
        self.value = val
        if val == -1:
            self.text = ''
            self.set_flag = False
            self.value = None
        else:
            self.text = str(val)
            self.set_flag = True
    
class Button:
    #Constants 
    color = BLACK
    width = BUTTON_WIDTH
    height = BUTTON_HEIGHT

    #Constructor 
    def __init__(self, x,y, text=''):
        self.x = x
        self.y = y
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4), 3)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),3)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

        
    



