import numpy as np
import math, time
from gameSetting import *
from gameFunctions import *

from agents.randomAgent import randomAgent
from agents.miniMaxAgent import miniMaxAgent
from agents.ruleBasedAgent import ruleBasedAgent

def playerAction(playerType, board, pnum, screen=None, event=None):
    
    if playerType == "user":
        posx = event.pos[0]
        col = int(math.floor(posx/SQUARESIZE))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, pnum, screen)
        else:
            return False

    elif playerType == "random":
        start_time = time.perf_counter()
        row, col = randomAgent(board)
        end_time = time.perf_counter()
        processing_time = end_time-start_time
        print(f"Processing time: {processing_time:.6f}")
        drop_piece(board, row, col, pnum, screen)
        
    elif playerType == "ruleBased":
        start_time = time.perf_counter()
        row, col = ruleBasedAgent(board, pnum)
        end_time = time.perf_counter()
        processing_time = end_time-start_time
        print(f"Processing time: {processing_time:.6f}")
        drop_piece(board, row, col, pnum, screen)

    elif playerType == "miniMax":
        start_time = time.perf_counter()
        best_col, best_score = miniMaxAgent(board, pnum, MINIMAX_DEPTH, -math.inf, math.inf, True)
        end_time = time.perf_counter()
        processing_time = end_time-start_time
        print(f"Processing time: {processing_time:.6f}")
        drop_piece(board, get_next_open_row(board, best_col), best_col, pnum, screen)
    else:
        print("Invalid player type. Please choose 'user', 'random', 'ruleBased', or 'miniMax'.")
        
    return True
