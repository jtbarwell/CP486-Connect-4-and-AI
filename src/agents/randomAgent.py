import numpy as np
from gameSetting import *
from gameFunctions import *

def randomAgent(board, pnum):
    valid_locations = [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]
    col = np.random.choice(valid_locations)
    row = get_next_open_row(board, col)
    drop_piece(board, row, col, pnum)

