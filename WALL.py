from init import wall_icon, pygame
from ELEMENT import ELEMENT

class WALL(ELEMENT):

    def __init__(self, party, length = None):
        super().__init__(party)
        if length == None:
            length = self.party.cell_number-1
        self.length = length
        self.randomly = False
        self.delete_at_next_game = False
        self.delete_in = False

        self.type = "wall"

        self.icon = wall_icon


