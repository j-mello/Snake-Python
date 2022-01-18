import random
from init import super_fruit_icon, fruit_group_id
from FRUIT import FRUIT

class SUPER_FRUIT(FRUIT):
    def __init__(self, party):
        super().__init__(party)
        self.icon = super_fruit_icon
        self.super_fruit = True


    def collision(self,snake):
        super().collision(snake)
        # Ragrandi encore le serpent
        snake.add_block(random.randint(1,2))
