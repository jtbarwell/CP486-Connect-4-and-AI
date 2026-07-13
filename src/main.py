import numpy as np
import pygame
import sys
import math
from gameSetting import *
from gameFunctions import *
from player import *
from menu import *

def __main__():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Connect 4")
    run_menu(screen)


if __name__ == "__main__":
    __main__()
