from pygame.math import Vector2
from init import cell_number, pygame
import random

class ELEMENT:
    def __init__(self):
        self.group_id = 0
        self.length = 1
        self.pos = Vector2(0,0)
        self.body = []
        self.reset()

    def reset(self):
        for block in self.body:
            self.party.tab[int(block.y)][int(block.x)] = 0
        self.body = []
        self.orientation = Vector2(0,0)

    def set_id(self,id):
        if id > 9:
            raise Exception('Id dépassant 9')
        self.id = self.group_id+id

    def set_party(self,party):
            self.party = party

    def place(self,pos,orientation):
        self.orientation = orientation
        self.pos = pos
        self.body = []
        for i in range(self.length):
            block = pos-orientation*i
            self.party.tab[int(block.y)][int(block.x)] = self.id
            self.body.append(block)

    def place_randomly(self):
        while True:
            orientation = [Vector2(0,-1),Vector2(1,0),Vector2(0,1),Vector2(-1,0)][random.randint(0,3)]

            pos_x = random.randint(0,cell_number-1)
            pos_y = random.randint(0,cell_number-1)
            pos = Vector2(pos_x,pos_y)
            if (self.check_random_placement(orientation,pos,self.length) == True):
                break

        self.place(pos,orientation)

    def check_random_placement(self,orientation,pos,length):
        for i in range(length):
            block = pos-orientation*i
            if not 0 <= block.x < cell_number or not 0 <= block.y < cell_number or self.party.tab[int(block.y)][int(block.x)] != 0:
                return False
        return True