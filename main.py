import pygame
from constants import *
from helpers import *
from classes import * 

#Game Window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")

#Initialize board -> 9x9 matrix 
board = init_board()


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
            #find the square that got clicked
            for i in range(9):
                for j in range(9):
                    if board[i][j].isOver(pos):
                        #unhighlight former square
                        if current_square != None:
                            board[current_square[0]][current_square[1]].unhighlight()

                        #highlight current square
                        current_square = [i,j]
                        board[i][j].highlight()
                    
        if event.type == pygame.KEYDOWN:
            if current_square != None:
                if event.key == pygame.K_0: board[current_square[0]][current_square[1]].write_value(0)
                elif event.key == pygame.K_1: board[current_square[0]][current_square[1]].write_value(1)
                elif event.key == pygame.K_2: board[current_square[0]][current_square[1]].write_value(2)
                elif event.key == pygame.K_3: board[current_square[0]][current_square[1]].write_value(3)
                elif event.key == pygame.K_4: board[current_square[0]][current_square[1]].write_value(4)
                elif event.key == pygame.K_5: board[current_square[0]][current_square[1]].write_value(5)
                elif event.key == pygame.K_6: board[current_square[0]][current_square[1]].write_value(6)
                elif event.key == pygame.K_7: board[current_square[0]][current_square[1]].write_value(7)
                elif event.key == pygame.K_8: board[current_square[0]][current_square[1]].write_value(8)
                elif event.key == pygame.K_9: board[current_square[0]][current_square[1]].write_value(9)

                        
                    
    draw_board(board, WIN)
    draw_borders(WIN)
    pygame.display.update()

pygame.quit()  

    



