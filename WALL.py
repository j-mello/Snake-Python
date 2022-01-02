from init import cell_number, wall_group_id, pygame
from ELEMENT import ELEMENT

class WALL(ELEMENT):

    def __init__(self, randomly = False, length = cell_number-1):
        super().__init__()
        self.length = length
        self.group_id = wall_group_id
        self.randomly = randomly

        self.icon = pygame.image.load('graphisms/wall.png').convert_alpha()

