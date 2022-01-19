from ELEMENT import ELEMENT
from pygame.math import Vector2
from init import pygame, tonic_icon

class TONIC_GRILL(ELEMENT):

    def __init__(self, party, sens, length = None):
        super().__init__(party)
        if length == None:
            length = self.party.cell_number-1
        self.length = length

        self.icon = tonic_icon

        self.type = "tonic_grill"

        self.sens = sens # H pour horizontal ou V pour vertical

    def collision(self,snake): #Si un serpent rentre en collision avec une grille tonique, le téléporter de l'autre coté
        head = snake.body[0]
        point_to_teleport = Vector2(head.x, 1 if head.y == self.party.cell_number-1 else self.party.cell_number-2) if self.sens == 'V' else Vector2(1 if head.x == self.party.cell_number-1 else self.party.cell_number-2,head.y)
        if self.party.tab[int(point_to_teleport.y)][int(point_to_teleport.x)] != 0:
            element = self.party.tab[int(point_to_teleport.y)][int(point_to_teleport.x)]
            if element.collision(snake) == False:
                return False
        self.party.tab[int(head.y)][int(head.x)] = self
        self.party.tab[int(point_to_teleport.y)][int(point_to_teleport.x)] = snake
        snake.body[0] = point_to_teleport

