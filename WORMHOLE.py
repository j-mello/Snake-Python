from ELEMENT import ELEMENT
from init import wormhole_group_id, cell_number, wormhole_icon
import random
from pygame.math import Vector2

class WORMHOLE(ELEMENT):

    def __init__(self):
        super().__init__()
        self.group_id = wormhole_group_id

        self.icon = wormhole_icon

    def place_randomly(self):

        self.body = []
        for i in range(2):
            while True:
                pos = Vector2(random.randint(0,cell_number-1), random.randint(0,cell_number-1))
                if (self.party.tab[int(pos.y)][int(pos.x)] != 0):
                    continue
                for xs in (-1,0,1):
                    for ys in (-1,0,1):
                       if pos.x + xs < 0 or pos.x + xs >= cell_number or pos.y + ys < 0 or pos.y + ys >= cell_number or self.party.tab[int(pos.y + ys)][int(pos.x + xs)] != 0:
                        continue
                break
            self.body.append(pos)
            self.party.tab[int(pos.y)][int(pos.x)] = self.id



    def collision(self,snake):
        srcPos = snake.body[0]
        dstPos = self.body[1][:] if srcPos == self.body[0] else self.body[0][:]
        dstPos += snake.direction

        self.party.tab[int(srcPos.y)][int(srcPos.x)] = self.id
        self.party.tab[int(dstPos.y)][int(dstPos.x)] = snake.id

        snake.body[0] = dstPos



