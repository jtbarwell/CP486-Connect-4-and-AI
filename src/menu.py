import pygame
import random
from gameSetting import *

AGENT_TYPES = ["user", "random", "ruleBased", "miniMax"]
AGENT_LABELS = {
    "user": "Human",
    "random": "Random",
    "ruleBased": "RuleBased",
    "miniMax": "MiniMax"
}

seedInput = None


def draw_menu(screen, font, player1_type, player2_type, seed_text, seed_active):
    screen.fill(NAVY_BG)
    title = font.render("CONNECT 4", True, WHITE)
    screen.blit(title, (width // 2 - title.get_width() // 2, 40))

    subtitle = pygame.font.SysFont("Segoe UI", 28).render("Choose each player before starting", True, WHITE)
    screen.blit(subtitle, (width // 2 - subtitle.get_width() // 2, 120))

    draw_player_selector(screen, 80, 180, "Player 1", player1_type)
    draw_player_selector(screen, width // 2 + 40, 180, "Player 2", player2_type)

    start_rect = pygame.Rect(width // 2 - 250, 420, 500, 120)
    pygame.draw.rect(screen, GREEN, start_rect)
    start_label = font.render("START GAME", True, BLACK)
    screen.blit(start_label, (width // 2 - start_label.get_width() // 2, 430))

    seed_rect = draw_seed_box(screen, seed_text, seed_active)

    return start_rect, seed_rect


def draw_seed_box(screen, seed_text, seed_active):
    seed_font = pygame.font.SysFont("Segoe UI", 24)

    caption_label = seed_font.render("Seed:", True, WHITE)
    caption_x = width // 2 - 220
    caption_y = height - 60
    screen.blit(caption_label, (caption_x, caption_y + 8))

    box_x = caption_x + caption_label.get_width() + 15
    box_y = caption_y
    box_width = 300
    box_height = 40
    seed_rect = pygame.Rect(box_x, box_y, box_width, box_height)

    box_color = YELLOW_BOX if seed_active else LIGHT_BLUE
    pygame.draw.rect(screen, box_color, seed_rect)
    pygame.draw.rect(screen, WHITE, seed_rect, 2)

    text_surface = seed_font.render(seed_text, True, BLACK)
    screen.blit(text_surface, (seed_rect.x + 8, seed_rect.y + 8))

    return seed_rect


def draw_player_selector(screen, x, y, title, selected_type):
    panel = pygame.Rect(x, y, 240, 180)
    pygame.draw.rect(screen, BLUE, panel)
    title_text = pygame.font.SysFont("Segoe UI", 24).render(title, True, WHITE)
    screen.blit(title_text, (x + 20, y + 20))

    button_y = y + 60
    for index, agent_type in enumerate(AGENT_TYPES):
        button_rect = pygame.Rect(x + 20 + (index % 2) * 110, button_y + (index // 2) * 50, 90, 35)
        color = YELLOW_BOX if agent_type == selected_type else LIGHT_BLUE
        pygame.draw.rect(screen, color, button_rect)
        label = pygame.font.SysFont("monospace", 14).render(AGENT_LABELS[agent_type], True, BLACK)
        screen.blit(label, (button_rect.x + 10, button_rect.y + 8))


def draw_game_over(screen, message, subtitle, font):
    # screen.fill(BLACK)
    winning_color = YELLOW if "Player 1" in subtitle else RED
    # add rectangle behind subtitle THAT IS LENGTH OF SUBTITLE 
    subtitle_rect = pygame.Rect(0, 190, 1300, 80)
    pygame.draw.rect(screen, NAVY_BG, subtitle_rect)

    label = font.render(message, True, winning_color)
    screen.blit(label, (width // 2 - label.get_width() // 2, 10))
    

    subtitle_label = pygame.font.SysFont("monospace", round(len(subtitle)*1.5)).render(subtitle, True, WHITE)
    screen.blit(subtitle_label, (width // 2 - subtitle_label.get_width() // 2, 200))

    button_rect = pygame.Rect(width // 2 - 120, 280, 240, 60)
    pygame.draw.rect(screen, GREEN, button_rect)

    button_text = pygame.font.SysFont("monospace", 26).render("BACK TO MENU", True, BLACK)
    screen.blit(button_text, (width // 2 - button_text.get_width() // 2, 295))

    pygame.display.flip()
    
    return button_rect


def handle_menu_click(pos, player1_type, player2_type, seed_rect):
    global seedInput

    start_rect = pygame.Rect(width // 2 - 250, 420, 500, 120)
    if start_rect.collidepoint(pos):
        return player1_type, player2_type, True, False

    if seed_rect.collidepoint(pos):
        return player1_type, player2_type, False, True

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
                    return AGENT_TYPES[index], player2_type, False, False

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
                    return player1_type, AGENT_TYPES[index], False, False

    # Clicked elsewhere on the screen - deactivate the seed box
    return player1_type, player2_type, False, False


def run_menu(screen, p1, p2):
    global seedInput

    pygame.font.init()
    font = pygame.font.SysFont("Segoe UI", 36)
    title_font = pygame.font.SysFont("Segoe UI", 70)

    player1_type = p1
    player2_type = p2

    seed_text = ""
    seed_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # We need the seed_rect from the last draw call to hit-test correctly;
                # draw once first if this is the very first loop iteration.
                _, seed_rect = draw_menu(screen, title_font, player1_type, player2_type, seed_text, seed_active)

                player1_type, player2_type, should_start, seed_active = handle_menu_click(
                    event.pos, player1_type, player2_type, seed_rect
                )

                if should_start:
                    if seed_text.strip() == "":
                        seedInput = random.randint(100000000, 999999999)
                        print(seedInput)
                        SEED = seedInput
                    else:
                        seedInput = seed_text
                        print(seedInput)
                        SEED = seedInput
                    return player1_type, player2_type

            if event.type == pygame.KEYDOWN and seed_active:
                if event.key == pygame.K_BACKSPACE:
                    seed_text = seed_text[:-1]
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    seed_active = False
                elif event.unicode.isdigit():
                    seed_text += event.unicode

        draw_menu(screen, title_font, player1_type, player2_type, seed_text, seed_active)
        pygame.display.update()