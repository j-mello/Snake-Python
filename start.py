import sys
from PARTY import PARTY
from SNAKE import SNAKE
from init import screen, pygame, snake_group_id
from pygame.math import Vector2

clock = pygame.time.Clock()

snake = SNAKE(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)
snake2 = SNAKE(pygame.K_z,pygame.K_s,pygame.K_d,pygame.K_q)

party = PARTY([snake,snake2])

SCREEN_UPDATE = pygame.USEREVENT #creation d'un event
pygame.time.set_timer(SCREEN_UPDATE, 150) #L'event sera trigger toutes les 150 millisecondes

clock.tick(60) #La boucle s'exécute 60 fois par seconde, correspondant aux 60 FPS


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            screen.fill((175,215,70))
            party.update()
            party.draw_elements()
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            for (index,snake) in enumerate(party.elements):
                if snake.id//100*100 != snake_group_id:
                    continue
                for (key,new_direction) in snake.KEYS.items():
                    if event.key == key and snake.orientation != new_direction*(-1):
                        snake.direction = new_direction
                        snake.orientation = new_direction