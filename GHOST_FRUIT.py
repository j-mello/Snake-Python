import random
from config import ghost_fruit_icon
from FRUIT import FRUIT

class GHOST_FRUIT(FRUIT):
    def __init__(self, party):
        super().__init__(party)
        self.icon = ghost_fruit_icon
        self.special_fruit = True


    def collision(self,snake):
        super().collision(snake)
        snake.ghost_activated = True
        snake.lost_ghost_in = random.randint(2,3)
        # Ragrandi encore le serpent

