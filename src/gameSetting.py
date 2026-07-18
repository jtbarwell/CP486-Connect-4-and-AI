import numpy as np
import pygame
import sys
import math

SEED = 468  # instantiate variable

START_SCREEN = "menu"

TIME_BETWEEN_MOVES = 75  # milliseconds
TIME_BETWEEN_FRAMES = 10  # milliseconds

BLUE = (48,98,124)
BOARD_BLUE = (0, 0, 255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
YELLOW_BOX = (249,248,113) # for menu items which are selected
WHITE = (255,255,255)
LIGHT_BLUE = (173, 216, 230) # for menu boxes to select agent
NAVY_BG = (31, 33, 51)
GREEN = (0, 200, 149)

ROW_COUNT = 6
COLUMN_COUNT = 7

SQUARESIZE = 100

MINIMAX_DEPTH = 4

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
RADIUS = int(SQUARESIZE/2 - 5)