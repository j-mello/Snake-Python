from ELEMENT import ELEMENT
from config import ghost_wall_icon
import random

class GHOST_WALL(ELEMENT):

    def __init__(self,party,length):
        super().__init__(party)
        self.length = length

        self.type = "ghost_wall"

        self.remaining_times = random.randint(2,3)

        self.icon = ghost_wall_icon


    def collision(self,snake):
        return True
