import pygame, random
from pygame.math import Vector2
from init import screen, cell_number, cell_size, apple

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        #create the rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        #draw the rectangle
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen,(126,166,114), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)