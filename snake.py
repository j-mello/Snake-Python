import pygame, sys

from pygame import surface

pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
test_surface = pygame.Surface((400,100))
test_surface.fill(pygame.Color('blue'))
test_rectangle = test_surface.get_rect(center = (400,400))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # screen.fill(pygame.Color('gold'))
    screen.fill((175,215,70))
    test_rectangle.right += 1
    screen.blit(test_surface, test_rectangle)
    pygame.display.update()
    clock.tick(60)