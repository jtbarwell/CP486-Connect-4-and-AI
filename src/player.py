import numpy as np
import pygame
import sys
import math
from gameSetting import *
from gameFunctions import *

from agents.randomAgent import randomAgent
# from agents.miniMaxAgent import miniMaxAgent
from agents.ruleBasedAgent import ruleBasedAgent

def playerAction(playerType, event, board, pnum):
    
    if playerType == "user":
        posx = event.pos[0]
        col = int(math.floor(posx/SQUARESIZE))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, pnum)

    elif playerType == "random":
        randomAgent(board, pnum)
    elif playerType == "ruleBased":
        ruleBasedAgent(board, pnum)
    # elif playerType == "miniMax":
    #     miniMaxAgent(board, pnum)
    else:
        print("Invalid player type. Please choose 'user', 'random', 'ruleBased', or 'miniMax'.")
