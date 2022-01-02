import sys
from PARTY import PARTY
from init import screen, pygame
from pygame.math import Vector2

clock = pygame.time.Clock()

party = PARTY()

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
            if event.key == pygame.K_UP and party.snake.direction.y != 1:
                party.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN and party.snake.direction.y != -1:
                party.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT and party.snake.direction.x != -1:
                party.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT and party.snake.direction.x != 1:
                party.snake.direction = Vector2(-1,0)
    screen.fill((175,215,70))