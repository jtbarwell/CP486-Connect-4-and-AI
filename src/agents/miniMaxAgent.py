"""
Implement the Minimax algorithm with: 
● Configurable search depth (a parameter). 
● Terminal evaluation: win = large positive, loss = large negative, draw = 0 (from the perspective of the agent to move). 
● Heuristic evaluation for non-terminal states at the depth limit (see Heuristic guidance below). 
● For all reported experiments, use a fixed depth of 4 (you may additionally report an optional depth-6 run for discussion). 
Heuristic guidance (Agent 3). A common, defensible evaluation is windowed scoring: slide a length-4 window over every row, column, and diagonal, 
and score each window by how many of your discs vs. the opponent’s it contains (reward 3-in-a-window heavily, 2 modestly; penalise the opponent’s the same way), 
plus a small weight for centre-column control. You may design your own — just describe it precisely in the report. 
"""
import numpy as np
import random
import math
from gameSetting import *
from gameFunctions import *

WINDOW_LENGTH = 4

def evaluate_window(window, pnum):
    score = 0
    opponent_pnum = 1 if pnum == 2 else 2
    empty_count = window.count(0)

    if window.count(pnum) == 4:
        score += 100
    elif window.count(pnum) == 3 and empty_count == 1:
        score += 5
    elif window.count(pnum) == 2 and empty_count == 2:
        score += 2

    if window.count(opponent_pnum) == 3 and empty_count == 1:
        score -= 4

    return score

def score_position(board, pnum):
    score = 0
    opponent_pnum = 1 if pnum == 2 else 2

    # Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(pnum)
    score += center_count * 3

    # Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, pnum)

    # Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, pnum)

    # Score positive sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, pnum)

    # Score negative sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, pnum)

    return score

def is_terminal_node(board):
	return winning_move(board, 1) or winning_move(board, 2) or len(get_valid_locations(board)) == 0

def miniMaxAgent(board, pnum, depth, alpha, beta, maximizingPlayer):

    opponent = 1 if pnum == 2 else 2

    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)

    if is_terminal:
        if winning_move(board, pnum):
            return (None, 100000000000000)
        elif winning_move(board, 1 if pnum == 2 else 2):
            return (None, -10000000000000)
        elif len(get_valid_locations(board)) == 0:
            return (None, 0)

    if depth == 0:
        return (None, score_position(board, pnum)) # always scored for the root agent

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, pnum)  # root agent drops here
            new_score = miniMaxAgent(b_copy, pnum, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value, column = new_score, col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, opponent)  # opponent drops here
            new_score = miniMaxAgent(b_copy, pnum, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value, column = new_score, col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
