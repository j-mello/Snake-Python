import random
from config import bad_fruit_icon
from FRUIT import FRUIT

class BAD_FRUIT(FRUIT):
    def __init__(self, party):
        super().__init__(party)
        self.icon = bad_fruit_icon
        self.special_fruit = True


    def collision(self,snake):
        super().collision(snake)
        # Rétrecir le serpent
        snake.remove_block(random.randint(2,3))
