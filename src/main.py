import numpy as np
import pygame
import sys
from gameSetting import *
from gameFunctions import *
from player import *
from menu import *

def __main__():
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    player1 = "user"
    player2 = "miniMax"

    pygame.init()


    size = (width, height)


    screen = pygame.display.set_mode(size)
    draw_board(board, screen)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else: 
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                #print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    playerAction(player1, event, board, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True


                # # Ask for Player 2 Input if Player 2 is a user
                else:
                    if player2 == "user":
                        playerAction(player2, event, board, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (40,10))
                            game_over = True

                print_board(board)
                draw_board(board, screen)

                turn += 1
                turn = turn % 2

        # Player 2 Input if Player 2 is an agent (not user)
        if player2 != "user" and turn == 1 and not game_over:
            pygame.time.wait(500)
            playerAction(player2, event, board, 2)

            if winning_move(board, 2):
                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                screen.blit(label, (40,10))
                game_over = True

            print_board(board)
            draw_board(board, screen)

            turn += 1
            turn = turn % 2

        if game_over:
            pygame.time.wait(1500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Connect 4")
    run_menu(screen)


if __name__ == "__main__":
    __main__()
