import random
import pygame
import time
from classes import *


def init_board():
#Use this function to initialize the soduko board -> returns 9x9 matrix 
    #Sudoku board
    board = [[None for x in range(9)] for x in range(9)]
    for row in range(9):
        for col in range(9):
            x = BOARD_ORIGIN_X + (row * (SQUARE_SIZE)) 
            y = BOARD_ORIGIN_Y + (col * (SQUARE_SIZE)) 
            board[row][col] = Square(x,y,row+1,col+1)
    
    #Buttons
    btn_new_game = Button(650, 125, 'New Game')
    btn_check = Button(650, 225, 'Check')
    btn_solve = Button(650, 325, 'Solve')
    
    return board, btn_check, btn_solve, btn_new_game

def draw_board(board, win):
#Use this function to draw the board-matrix on to the Game-Window
    win.fill(WHITE)
    for i in range(9):
        for j in range(9):
            board[i][j].draw(win)

def draw_buttons(btn_check, btn_solve, btn_new_game, win):
#Use this function to draw the buttons on the game screen
    btn_check.draw(win)
    btn_solve.draw(win)
    btn_new_game.draw(win)


def draw_borders(win): 
#Use this function to draw the borders of the sudoku board
    #Inner borders
    INNER_BORDER_LEFT = pygame.Rect(BOARD_ORIGIN_X + 3*SQUARE_SIZE -2, BOARD_ORIGIN_Y, 4, 9*SQUARE_SIZE)
    INNER_BORDER_RIGHT = pygame.Rect(BOARD_ORIGIN_X + 6*SQUARE_SIZE -2, BOARD_ORIGIN_Y, 4, 9*SQUARE_SIZE)
    INNER_BORDER_TOP = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y + 3*SQUARE_SIZE -2, 9*SQUARE_SIZE, 4)
    INNER_BORDER_BOTTOM = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y + 6*SQUARE_SIZE -2, 9*SQUARE_SIZE, 4)
    pygame.draw.rect(win, BLACK, INNER_BORDER_LEFT)
    pygame.draw.rect(win, BLACK, INNER_BORDER_RIGHT)
    pygame.draw.rect(win, BLACK, INNER_BORDER_TOP)
    pygame.draw.rect(win, BLACK, INNER_BORDER_BOTTOM)

    #Outter borders
    OUTER_BORDER_LEFT = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y, 4, 9*SQUARE_SIZE)
    OUTER_BORDER_RIGHT = pygame.Rect(BOARD_ORIGIN_X + 9*SQUARE_SIZE -2, BOARD_ORIGIN_Y, 4, 9*SQUARE_SIZE)
    OUTER_BORDER_TOP = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y, 9*SQUARE_SIZE, 4)
    OUTER_BORDER_BOTTOM = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y + 9*SQUARE_SIZE, 9*SQUARE_SIZE, 4)
    pygame.draw.rect(win, BLACK, OUTER_BORDER_LEFT)
    pygame.draw.rect(win, BLACK, OUTER_BORDER_RIGHT)
    pygame.draw.rect(win, BLACK, OUTER_BORDER_TOP)
    pygame.draw.rect(win, BLACK, OUTER_BORDER_BOTTOM)


def solve_sudoku(board):
#Use this function to solve the sudoku
    #Find an open square
    current_square = find_empty(board)
    if not current_square:
        return True
    else:
        row, col = current_square
    
    for i in range(1,10):
        if valid(board, row, col, i):
            board[row][col].write_value(i)

            if solve_sudoku(board):
                return True
            
            board[row][col].write_value(-1)
    
    return False
            
def find_empty(board):
#Use this function to find an empty square
    for i in range(9):
        for j in range(9):
            if not board[i][j].set_flag: 
                return (i, j)
    return None

def valid(board, row, col, num):
#Use this function to check if an entry is valid
    super_square = board[row][col].super_square
    existing_entries = []        
    all_entries = set(x for x in range(1,10) if x not in existing_entries)
    for i in range(9):
        if board[row][i].value != None:
            existing_entries.append(board[row][i].value)
        if board[i][col].value != None:
            existing_entries.append(board[i][col].value)
    for i in range(super_square[0], super_square[0]+3):
        for j in range(super_square[1], super_square[1]+3):
            existing_entries.append(board[i][j].value)

    existing_entries = set(existing_entries)
    possible_entries = all_entries - existing_entries  

    if num in possible_entries:
        return True
    return False

def new_game(board):
#Use this function to create a random sudoku game
    #Delete all existing entries
    for row in range(9):
        for col in range(9):
            board[row][col].write_value(-1)
    
    #Insert 1-9 random into first row
    nums = []
    for i in range(1,10):
        nums.append(i)
    
    random.shuffle(nums)
    for i in range(9):
        board[0][i].write_value(nums[i])
    
    solve_sudoku(board)
    for row in range(9):
        for col in range(9):
            if random.randrange(1,10) < 6:
                board[row][col].write_value(-1)
    
def check_solvability(board):
#Use this function to check if a sudoku is solvable in current state
    for row in range(9):
        for col in range(9): 
            if board[row][col].set_flag:
                temp = board[row][col].value
                board[row][col].write_value(-1)
                if not valid(board, row, col, temp):
                    board[row][col].write_value(temp)
                    return False
                board[row][col].write_value(temp)
    return True

def display_message(text, win):
#Use this function to display a message on the game screen
    font = pygame.font.SysFont('comicsans', 30)
    text_surface = font.render(text, False, (250,73,73))
    text_rect = text_surface.get_rect(center = (720,50))
    win.blit(text_surface, text_rect)
    pygame.display.update()
    time.sleep(2)
    



