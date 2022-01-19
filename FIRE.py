from init import fire_icon
from pygame.math import Vector2
import json
from ELEMENT import ELEMENT

class FIRE(ELEMENT):

    def __init__(self,party,snake):
        super().__init__(party)
        self.snake = snake
        self.icon = fire_icon
        self.type = "fire"


    def place(self):
        self.reset()
        for snake_block in self.snake.body:
            x = int(snake_block.x)
            y = int(snake_block.y)
            for xs in (-1,0,1):
                for ys in (-1,0,1):
                    if (
                        (xs == 0 and ys == 0) or
                        not 0 < x+xs < self.party.cell_number or
                        not 0 < y+ys < self.party.cell_number or
                        (self.party.tab[y+ys][x+xs] != 0 and self.party.tab[y+ys][x+xs].type != "ghost_wall")):
                        continue

                    self.body.append(Vector2(x+xs,y+ys))
                    self.party.tab[y+ys][x+xs] = self


    def collision(self,snake):
        if snake.id != self.snake.id:
            self.party.game_over(snake)
            return False
        return True

