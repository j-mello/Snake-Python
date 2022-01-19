import random
from init import fruit_icon
from ELEMENT import ELEMENT

class FRUIT(ELEMENT):
    def __init__(self, party):
        super().__init__(party)
        self.place_randomly_when_shrink = True
        self.special_fruit = False

        self.icon = fruit_icon

        self.type = "fruit"


    def collision(self,snake):
        # bruitage
        snake.play_eating_sound()

        # replacer un fruit ailleurs
        self.party.place_new_fruit(self)

        self.party.set_dynamic_wall()
        self.party.shrink_grill()

        if snake.lost_ghost_in > 0:
            snake.lost_ghost_in -= 1
        elif snake.ghost_activated == True:
            snake.ghost_activated = False

        if snake.lost_fire_in > 0:
            snake.lost_fire_in -= 1
        elif snake.fire != None:
            snake.remove_fire()

        if self.special_fruit == False:
            # rendre le serpent plus grand
            snake.add_block()
