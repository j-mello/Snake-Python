from ELEMENT import ELEMENT
from pygame.math import Vector2
from init import tonic_group_id, cell_number, pygame, tonic_icon

class TONIC_GRILL(ELEMENT):

    def __init__(self, sens, length = cell_number-1):
        super().__init__()
        self.group_id = tonic_group_id
        self.length = length

        self.icon = tonic_icon

        self.sens = sens # H pour horizontal ou V pour vertical

    def collision(self,snake): #Si un serpent rentre en collision avec une grille tonique, le téléporter de l'autre coté
        head = snake.body[0]
        point_to_teleport = Vector2(head.x, 1 if head.y == cell_number-1 else cell_number-2) if self.sens == 'V' else Vector2(1 if head.x == cell_number-1 else cell_number-2,head.y)
        if self.party.tab[int(point_to_teleport.y)][int(point_to_teleport.x)] != 0:
            element = self.party.get_element_by_id(self.party.tab[int(point_to_teleport.y)][int(point_to_teleport.x)])
            if element.collision(snake) == False:
                return False
        self.party.tab[int(head.y)][int(head.x)] = self.id
        self.party.tab[int(point_to_teleport.y)][int(point_to_teleport.x)] = snake.id
        snake.body[0] = point_to_teleport

