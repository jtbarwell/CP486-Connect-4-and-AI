"""
An agent driven by manually defined, prioritized rules. A reasonable rule set, in priority order: 
1. If a move wins immediately, play it. 
2. Else, if the opponent has an immediate winning move, block it. 
3. Else, prefer central columns. 
4. Else, extend your own longest line / create threats. 
State your exact rules and their priority order in the report. Apply the tie-breaking rule above when several 
moves satisfy the same rule. 
"""
import numpy as np
from gameSetting import *
from gameFunctions import *

def ruleBasedAgent(board, pnum):
    np.random.seed(SEED)
    # Check for winning move
    winning_moves = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, pnum)
            if winning_move(temp_board, pnum):
                winning_moves.append(col)
    if len(winning_moves) >= 1:
        col = np.random.choice(winning_moves)
        row = get_next_open_row(board, col)
        return row, col

    # Check for opponent's winning move and block it
    opponent_pnum = 1 if pnum == 2 else 2
    opp_winning_moves = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, opponent_pnum)
            if winning_move(temp_board, opponent_pnum):
                opp_winning_moves.append(col)
    if len(opp_winning_moves) >= 1:
        col = np.random.choice(opp_winning_moves)
        row = get_next_open_row(board, col)
        return row, col

    # Prefer central columns
    center_col = COLUMN_COUNT // 2
    if is_valid_location(board, center_col):
        row = get_next_open_row(board, center_col)
        return row, center_col

    # Extend own longest line / create threats
    valid_moves = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_moves.append(col)
    col = np.random.choice(valid_moves)
    row = get_next_open_row(board, col)
    return row, col