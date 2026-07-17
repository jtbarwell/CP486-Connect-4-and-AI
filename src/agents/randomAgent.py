import numpy as np
from gameSetting import *
from gameFunctions import *

def randomAgent(board):
    np.random.seed(SEED)
    valid_locations = [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]
    col = np.random.choice(valid_locations)
    row = get_next_open_row(board, col)
    return row, col

