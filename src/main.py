from gameSetting import *
from gameFunctions import *
from player import *
from gameLoop import gameLoop
from menu import run_menu

def __main__():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Connect 4")

    current_screen = START_SCREEN
    p1 = "user"
    p2 = "user"

    while True:

        if current_screen == "menu":
            p1, p2 = run_menu(screen, p1, p2)
            current_screen = "game"  # Change to "game" to proceed to the game loop

        if current_screen == "game":
            gameLoop(screen, p1, p2)
            current_screen = "menu"  # Change back to "menu" after the game loop ends


if __name__ == "__main__":
    __main__()

