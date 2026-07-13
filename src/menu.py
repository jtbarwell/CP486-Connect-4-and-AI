import pygame
from gameSetting import *

AGENT_TYPES = ["user", "random", "rule-based", "minimax"]
AGENT_LABELS = {
    "user": "Human",
    "random": "Random",
    "rule-based": "Rule",
    "minimax": "MiniMax"
}


def draw_menu(screen, font, player1_type, player2_type):
    screen.fill(BLACK)
    title = font.render("CONNECT 4", True, WHITE)
    screen.blit(title, (width // 2 - title.get_width() // 2, 40))

    subtitle = pygame.font.SysFont("Segoe UI", 28).render("Choose each player before starting", True, WHITE)
    screen.blit(subtitle, (width // 2 - subtitle.get_width() // 2, 120))

    draw_player_selector(screen, 80, 180, "Player 1", player1_type)
    draw_player_selector(screen, width // 2 + 40, 180, "Player 2", player2_type)

    start_rect = pygame.Rect(width // 2 - 250, 420, 500, 120)
    pygame.draw.rect(screen, GREEN, start_rect)
    start_label = font.render("START GAME", True, BLACK)
    screen.blit(start_label, (width // 2 - start_label.get_width() // 2, 435))
    return start_rect


def draw_player_selector(screen, x, y, title, selected_type):
    panel = pygame.Rect(x, y, 240, 180)
    pygame.draw.rect(screen, BLUE, panel)
    title_text = pygame.font.SysFont("Segoe UI", 24).render(title, True, WHITE)
    screen.blit(title_text, (x + 20, y + 20))

    button_y = y + 60
    for index, agent_type in enumerate(AGENT_TYPES):
        button_rect = pygame.Rect(x + 20 + (index % 2) * 100, button_y + (index // 2) * 50, 80, 35)
        color = YELLOW if agent_type == selected_type else LIGHT_BLUE
        pygame.draw.rect(screen, color, button_rect)
        label = pygame.font.SysFont("monospace", 14).render(AGENT_LABELS[agent_type], True, BLACK)
        screen.blit(label, (button_rect.x + 10, button_rect.y + 8))


def draw_game_over(screen, message, font):
    screen.fill(BLACK)
    label = font.render(message, True, YELLOW)
    screen.blit(label, (width // 2 - label.get_width() // 2, 140))
    button_rect = pygame.Rect(width // 2 - 120, 280, 240, 60)
    pygame.draw.rect(screen, GREEN, button_rect)
    button_text = pygame.font.SysFont("monospace", 26).render("BACK TO MENU", True, BLACK)
    screen.blit(button_text, (width // 2 - button_text.get_width() // 2, 295))
    return button_rect


def handle_menu_click(pos, player1_type, player2_type):
    start_rect = pygame.Rect(width // 2 - 250, 420, 500, 120)
    if start_rect.collidepoint(pos):
        return player1_type, player2_type, True

    if 80 <= pos[0] <= 320 and 180 <= pos[1] <= 360:
        panel_left = pygame.Rect(80, 180, 240, 180)
        if panel_left.collidepoint(pos):
            button_rects = [
                pygame.Rect(100, 240, 80, 35),
                pygame.Rect(200, 240, 80, 35),
                pygame.Rect(100, 290, 80, 35),
                pygame.Rect(200, 290, 80, 35),
            ]
            for index, rect in enumerate(button_rects):
                if rect.collidepoint(pos):
                    return AGENT_TYPES[index], player2_type, False

    if width // 2 + 40 <= pos[0] <= width // 2 + 280 and 180 <= pos[1] <= 360:
        panel_right = pygame.Rect(width // 2 + 40, 180, 240, 180)
        if panel_right.collidepoint(pos):
            button_rects = [
                pygame.Rect(width // 2 + 60, 240, 80, 35),
                pygame.Rect(width // 2 + 160, 240, 80, 35),
                pygame.Rect(width // 2 + 60, 290, 80, 35),
                pygame.Rect(width // 2 + 160, 290, 80, 35),
            ]
            for index, rect in enumerate(button_rects):
                if rect.collidepoint(pos):
                    return player1_type, AGENT_TYPES[index], False

    return player1_type, player2_type, False


def run_menu(screen):
    pygame.font.init()
    font = pygame.font.SysFont("Segoe UI", 36)
    title_font = pygame.font.SysFont("Segoe UI", 70)

    player1_type = "user"
    player2_type = "user"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                player1_type, player2_type, should_start = handle_menu_click(event.pos, player1_type, player2_type)
                if should_start:
                    return player1_type, player2_type

        draw_menu(screen, title_font, player1_type, player2_type)
        pygame.display.update()

