import sys
from PARTY import PARTY
from elements.SNAKE import SNAKE
from init import screen, pygame, SCREEN_UPDATE
from config import cell_number, cell_size, config_game
from pygame.math import Vector2

def start_game():
    screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))

    snakes = []

    snakes.append(SNAKE(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT))
    if config_game["nb_players"] >= 2:
        snakes.append(SNAKE(pygame.K_z,pygame.K_s,pygame.K_d,pygame.K_q))
    if config_game["nb_players"] >= 3:
        snakes.append(SNAKE(pygame.K_y,pygame.K_h,pygame.K_j,pygame.K_g))

    party = PARTY(*snakes)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                screen.fill((175,215,70))
                party.update()
                party.draw_elements()
                party.display_update()
            if event.type == pygame.KEYDOWN:
                if party.playing:
                    for snake in party.elements.values():
                        if snake.type != "snake":
                            continue
                        for (key,new_direction) in snake.KEYS.items():
                            if event.key == key and snake.orientation != new_direction*(-1):
                                snake.direction = new_direction
                                snake.orientation = new_direction
                elif event.key == pygame.K_RETURN:
                    party.reset()
