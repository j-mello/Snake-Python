import sys
from PARTY import PARTY
from SNAKE import SNAKE
from init import screen, pygame
from pygame.math import Vector2

clock = pygame.time.Clock()

snake = SNAKE(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)

party = PARTY(snake)

SCREEN_UPDATE = pygame.USEREVENT #creation d'un event
pygame.time.set_timer(SCREEN_UPDATE, 150) #L'event sera trigger toutes les 150 millisecondes

clock.tick(60) #La boucle s'exécute 60 fois par seconde, correspondant aux 60 FPS


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            party.update()
            party.draw_elements()
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            for (key,new_direction) in party.snake.KEYS.items():
                if event.key == key and party.snake.direction != new_direction*(-1):
                    party.snake.direction = new_direction
    screen.fill((175,215,70))