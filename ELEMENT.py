from pygame.math import Vector2
from init import cell_size, screen, pygame, fruit_group_id
import random

class ELEMENT:
    def __init__(self,party = None):
        if party != None:
            self.set_party(party)
        self.group_id = 0
        self.length = 1
        self.pos = Vector2(0,0)
        self.body = []
        self.limit_spawn = 1
        self.place_randomly_when_shrink = False
        self.reset()

    def reset(self):
        for block in self.body:
            if self.party.tab[int(block.y)][int(block.x)] == self.id:
                self.party.tab[int(block.y)][int(block.x)] = 0
        self.body = []
        self.orientation = Vector2(0,0)

    def set_id(self,id):
        if id > 99:
            raise Exception('Id dépassant 99')
        self.id = self.group_id+id

    def auto_set_id(self):
        id = self.group_id
        for element in self.party.elements:
            if element.id == id:
                id += 1
        self.id = id

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

            pos_x = random.randint(0,self.party.cell_number-1)
            pos_y = random.randint(0,self.party.cell_number-1)
            pos = Vector2(pos_x,pos_y)
            if (self.check_random_placement(orientation,pos,self.length) == True):
                break
        self.place(pos,orientation)

    def check_random_placement(self,orientation,pos,length):
        for i in range(length):
            block = pos-orientation*i
            if not self.limit_spawn <= block.x < self.party.cell_number-self.limit_spawn or not self.limit_spawn <= block.y < self.party.cell_number-self.limit_spawn or self.party.tab[int(block.y)][int(block.x)] != 0:
                return False
        return True

    def draw(self):
        for block in self.body:
            # On crée les rect pour les positions
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size,cell_size)

            screen.blit(self.icon,block_rect)

    def collision(self,snake):
        self.party.game_over()
        return False
