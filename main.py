import pygame
import time
from constants import *
from helpers import *
from classes import * 

#Game Window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")

#Initialize board -> 9x9 matrix 
board, btn_check, btn_solve, btn_new_game = init_board()

#Game variables
run = True
current_square = None

#Game Circle 
while run:
    for event in pygame.event.get():
        #Mouse position
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
        #find button that got clicked
            #Button "solve" got clicked
            if btn_solve.isOver(pos):
                if not check_solvability(board):
                    display_message('Sudoku is not solvable', WIN)
                else: 
                    solve_sudoku(board)
            #Button "new game" got clicked
            elif btn_new_game.isOver(pos):
                new_game(board)

            #Button "check" got clicked
            elif btn_check.isOver(pos):
                if not check_solvability(board):
                    display_message('There is an error in your solution', WIN)
                else:
                    display_message('So far, so good', WIN)
                
            #Find the square that got clicked
            for i in range(9):
                for j in range(9):
                    if board[i][j].isOver(pos):
                        #Unhighlight former square
                        if current_square != None:
                            board[current_square[0]][current_square[1]].unhighlight()

                        #Highlight current square
                        current_square = [i,j]
                        board[i][j].highlight(BLUE)

        #Write value in selected square    
        if event.type == pygame.KEYDOWN:
            if current_square != None:
                if event.key == pygame.K_1: board[current_square[0]][current_square[1]].write_value(1)
                elif event.key == pygame.K_2: board[current_square[0]][current_square[1]].write_value(2)
                elif event.key == pygame.K_3: board[current_square[0]][current_square[1]].write_value(3)
                elif event.key == pygame.K_4: board[current_square[0]][current_square[1]].write_value(4)
                elif event.key == pygame.K_5: board[current_square[0]][current_square[1]].write_value(5)
                elif event.key == pygame.K_6: board[current_square[0]][current_square[1]].write_value(6)
                elif event.key == pygame.K_7: board[current_square[0]][current_square[1]].write_value(7)
                elif event.key == pygame.K_8: board[current_square[0]][current_square[1]].write_value(8)
                elif event.key == pygame.K_9: board[current_square[0]][current_square[1]].write_value(9)
                elif event.key == pygame.K_BACKSPACE: board[current_square[0]][current_square[1]].write_value(-1)

    #Update display
    draw_board(board, WIN)
    draw_borders(WIN)
    draw_buttons(btn_check, btn_solve, btn_new_game, WIN)
    pygame.display.update()

pygame.quit()  

    



