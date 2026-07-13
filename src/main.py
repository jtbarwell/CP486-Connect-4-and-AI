from gameSetting import *
from gameFunctions import *
from player import *
from gameLoop import gameLoop
from menu import *

def __main__():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Connect 4")

    current_screen = START_SCREEN
    if current_screen == "menu":
        p1, p2 = run_menu(screen)
        current_screen = "game"  # Change to "game" to proceed to the game loop

    if current_screen == "game":
        gameLoop(screen, p1, p2)

if __name__ == "__main__":
    __main__()

