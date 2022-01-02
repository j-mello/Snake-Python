from init import cell_number, wall_group_id, wall_icon, pygame
from ELEMENT import ELEMENT

class WALL(ELEMENT):

    def __init__(self, length = cell_number-1):
        super().__init__()
        self.length = length
        self.group_id = wall_group_id
        self.randomly = False
        self.delete_at_next_game = False
        self.delete_in = False

        self.icon = wall_icon


