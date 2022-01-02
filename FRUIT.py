import pygame, random
from init import screen, cell_number, cell_size, fruit_icon, fruit_group_id, new_random_walls_at_each_new_fruit
from ELEMENT import ELEMENT

class FRUIT(ELEMENT):
    def __init__(self):
        super().__init__()
        self.group_id = fruit_group_id

        self.icon = fruit_icon


    def collision(self,snake):
         # bruitage
         snake.play_eating_sound()
         # replacer un fruit ailleurs
         self.reset()
         self.place_randomly()
         # rendre le serpent plus grand
         snake.add_block()
         snake.collisionned_block = 0

         self.party.set_dynamic_wall()
