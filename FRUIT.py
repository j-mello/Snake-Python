import random
from init import fruit_icon, fruit_group_id
from ELEMENT import ELEMENT

class FRUIT(ELEMENT):
    def __init__(self, party):
        super().__init__(party)
        self.group_id = fruit_group_id
        self.place_randomly_when_shrink = True
        self.special_fruit = False

        self.icon = fruit_icon


    def collision(self,snake):
        # bruitage
        snake.play_eating_sound()

        # replacer un fruit ailleurs
        self.party.place_new_fruit(self)

        self.party.set_dynamic_wall()
        self.party.shrink_grill()

        snake.collisionned_block = 0
        if self.special_fruit == False:
            # rendre le serpent plus grand
            snake.add_block()
