import numpy as np
import math
from gameSetting import *
from gameFunctions import *

from agents.randomAgent import randomAgent
from agents.miniMaxAgent import miniMaxAgent
from agents.ruleBasedAgent import ruleBasedAgent

def playerAction(playerType, board, pnum, event=None):
    
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
    elif playerType == "miniMax":
        best_col, best_score = miniMaxAgent(board, pnum, 4)  # Assuming depth of 4 for the minimax agent
        drop_piece(board, get_next_open_row(board, best_col), best_col, pnum)
    else:
        print("Invalid player type. Please choose 'user', 'random', 'ruleBased', or 'miniMax'.")
