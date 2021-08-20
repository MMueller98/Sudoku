import pygame
from classes import *


def init_board():
#Use this function to initialize the soduko board -> returns 9x9 matrix 
    board = [[None for x in range(9)] for x in range(9)]
    for i in range(9):
        for j in range(9):
            x = BOARD_ORIGIN_X + (i * (SQUARE_SIZE)) 
            y = BOARD_ORIGIN_Y + (j * (SQUARE_SIZE)) 
            board[i][j] = Square(x,y)
    return board

def draw_board(board, win):
#Use this function to draw the board-matrix on to the Game-Window
    win.fill(WHITE)
    for i in range(9):
        for j in range(9):
            board[i][j].draw(win)

def draw_borders(win): 
    #Innen
    INNER_BORDER_LEFT = pygame.Rect(BOARD_ORIGIN_X + 3*SQUARE_SIZE -2, BOARD_ORIGIN_Y, 4, 9*SQUARE_SIZE)
    INNER_BORDER_RIGHT = pygame.Rect(BOARD_ORIGIN_X + 6*SQUARE_SIZE -2, BOARD_ORIGIN_Y, 4, 9*SQUARE_SIZE)
    INNER_BORDER_TOP = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y + 3*SQUARE_SIZE -2, 9*SQUARE_SIZE, 4)
    INNER_BORDER_BOTTOM = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y + 6*SQUARE_SIZE -2, 9*SQUARE_SIZE, 4)
    pygame.draw.rect(win, BLACK, INNER_BORDER_LEFT)
    pygame.draw.rect(win, BLACK, INNER_BORDER_RIGHT)
    pygame.draw.rect(win, BLACK, INNER_BORDER_TOP)
    pygame.draw.rect(win, BLACK, INNER_BORDER_BOTTOM)

    #Außen
    OUTER_BORDER_LEFT = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y, 4, 9*SQUARE_SIZE)
    OUTER_BORDER_RIGHT = pygame.Rect(BOARD_ORIGIN_X + 9*SQUARE_SIZE -2, BOARD_ORIGIN_Y, 4, 9*SQUARE_SIZE)
    OUTER_BORDER_TOP = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y, 9*SQUARE_SIZE, 4)
    OUTER_BORDER_BOTTOM = pygame.Rect(BOARD_ORIGIN_X, BOARD_ORIGIN_Y + 9*SQUARE_SIZE, 9*SQUARE_SIZE, 4)
    pygame.draw.rect(win, BLACK, OUTER_BORDER_LEFT)
    pygame.draw.rect(win, BLACK, OUTER_BORDER_RIGHT)
    pygame.draw.rect(win, BLACK, OUTER_BORDER_TOP)
    pygame.draw.rect(win, BLACK, OUTER_BORDER_BOTTOM)
