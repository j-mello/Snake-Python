import random
from config import fire_fruit_icon
from elements.FRUIT import FRUIT

class FIRE_FRUIT(FRUIT):
    def __init__(self, party):
        super().__init__(party)
        self.icon = fire_fruit_icon
        self.special_fruit = True


    def collision(self,snake):
        super().collision(snake)
        # Emflamme le joueur
        snake.create_fire()

