from ELEMENT import ELEMENT
from config import wormhole_icon
import random
from pygame.math import Vector2

class WORMHOLE(ELEMENT):

    def __init__(self,party):
        super().__init__(party)
        self.limit_spawn = 2
        self.place_randomly_when_shrink = True

        self.type = "wormhole"

        self.icon = wormhole_icon

    def place_randomly(self):
        self.body = []
        for i in range(2):
            limit_try_wormhole_spawn = 500
            i = 0
            while i<limit_try_wormhole_spawn:
                pos = Vector2(random.randint(0,self.party.cell_number-1), random.randint(0,self.party.cell_number-1))
                if (self.party.tab[int(pos.y)][int(pos.x)] != 0):
                    continue

                ok = True
                for xs in (-1,0,1):
                    for ys in (-1,0,1):
                        if (self.party.tab[int(pos.y + ys)][int(pos.x + xs)] != 0 or
                           pos.y + ys >= self.party.cell_number-self.limit_spawn or
                           pos.x + xs >= self.party.cell_number-self.limit_spawn or
                           pos.y + ys < self.limit_spawn or
                           pos.x + xs < self.limit_spawn):
                            ok = False
                            break
                    if ok == False: break

                if ok == True: break
                i += 1
            if i == limit_try_wormhole_spawn:
                self.delete()
                return
            self.body.append(pos)
            self.party.tab[int(pos.y)][int(pos.x)] = self



    def collision(self,snake):
        srcPos = snake.body[0]
        dstPos = self.body[1][:] if srcPos == self.body[0] else self.body[0][:]
        dstPos += snake.direction

        self.party.tab[int(srcPos.y)][int(srcPos.x)] = self
        if self.party.tab[int(dstPos.y)][int(dstPos.x)] != 0:
            element = self.party.tab[int(dstPos.y)][int(dstPos.x)]
            if element.collision(snake) == False:
                return False
        self.party.tab[int(dstPos.y)][int(dstPos.x)] = snake

        snake.body[0] = dstPos



