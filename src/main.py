from gameSetting import *
from gameFunctions import *
from player import *
from gameLoop import gameLoop


def __main__():
    current_screen = START_SCREEN
    if current_screen == "menu":
        # mainMenu()
        current_screen = "game"  # Change to "game" to proceed to the game loop

    if current_screen == "game":
        gameLoop()

if __name__ == "__main__":
    __main__()
