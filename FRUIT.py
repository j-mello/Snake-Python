import pygame, random
from pygame.math import Vector2
from init import screen, cell_number, cell_size, apple, fruit_group_id
from ELEMENT import ELEMENT

class FRUIT(ELEMENT):
    def __init__(self):
        super().__init__()
        self.group_id = fruit_group_id

    def draw(self):
        #create the rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        #draw the rectangle
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen,(126,166,114), fruit_rect)