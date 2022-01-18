from init import wall_group_id, wall_icon, pygame
from ELEMENT import ELEMENT

class WALL(ELEMENT):

    def __init__(self, party, length = None):
        super().__init__(party)
        if length == None:
            length = self.party.cell_number-1
        self.length = length
        self.group_id = wall_group_id
        self.randomly = False
        self.delete_at_next_game = False
        self.delete_in = False

        self.icon = wall_icon


