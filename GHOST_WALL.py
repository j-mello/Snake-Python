from ELEMENT import ELEMENT
from init import ghostwall_group_id, ghost_wall_icon
import random

class GHOST_WALL(ELEMENT):

    def __init__(self,length):
        self.group_id = ghostwall_group_id
        self.length = length

        self.remaining_times = random.randint(2,3)

        self.icon = ghost_wall_icon


    def collision(self,snake):
        return True
