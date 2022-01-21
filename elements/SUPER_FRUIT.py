import random
from config import super_fruit_icon
from elements.FRUIT import FRUIT

class SUPER_FRUIT(FRUIT):
    def __init__(self, party):
        super().__init__(party)
        self.icon = super_fruit_icon
        self.special_fruit = True


    def collision(self,snake):
        super().collision(snake)
        # Ragrandi encore le serpent
        snake.add_block(random.randint(2,3))
