import numpy as np
import pygame
import sys
from gameSetting import *
from gameFunctions import *
from menu import draw_game_over
from player import *

def gameLoop(screen, p1, p2):
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    player1 = p1
    player2 = p2
    screen.fill(BLACK)
    draw_board(board, screen)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while not game_over:

        # Player 1 Input if Player 1 is an agent (not user)
        if player1 != "user" and turn == 0 and not game_over:
            pygame.time.wait(500)
            playerAction(player1, board, 1)

            if winning_move(board, 1):
                label = "Player 1 (" + player1 + ") wins!!"
                game_over = True

            print_board(board)
            draw_board(board, screen)

            turn += 1
            turn = turn % 2
        
        if player1 == "user" or player2 == "user" and not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, NAVY_BG, (0,0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    else: 
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, NAVY_BG, (0,0, width, SQUARESIZE))
                    #print(event.pos)
                    # Ask for Player 1 Input
                    if turn == 0:
                        playerAction(player1, board, 1, event)

                        if winning_move(board, 1):
                            label = "Player 1 (" + player1 + ") wins!!"
                            game_over = True


                    # # Ask for Player 2 Input if Player 2 is a user
                    else:
                        if player2 == "user":
                            playerAction(player2, board, 2, event)

                            if winning_move(board, 2):
                                label = "Player 2 (" + player2 + ") wins!!"
                                game_over = True

                    print_board(board)
                    draw_board(board, screen)

                    turn += 1
                    turn = turn % 2

        # Player 2 Input if Player 2 is an agent (not user)
        if player2 != "user" and turn == 1 and not game_over:
            pygame.time.wait(500)
            playerAction(player2, board, 2)

            if winning_move(board, 2):
                label = "Player 2 (" + player2 + ") wins!!"
                game_over = True

            print_board(board)
            draw_board(board, screen)

            turn += 1
            turn = turn % 2

        # Check for draw
        if not game_over and len(get_valid_locations(board)) == 0:
            label = "Draw!"
            game_over = True


        if game_over:
            print(label)
            while True:
                button_rect = draw_game_over(screen, "Game Over", label, myfont)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                        return

                pygame.time.wait(10)
