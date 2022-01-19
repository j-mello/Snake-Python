import pygame, random
from pygame.math import Vector2
from init import screen, cell_size, default_length_snake
from ELEMENT import ELEMENT
from FIRE import FIRE

class SNAKE(ELEMENT):
    def __init__(self,UP_KEY,DOWN_KEY,RIGHT_KEY,LEFT_KEY):
        super().__init__()

        self.KEYS = {
            UP_KEY: Vector2(0,-1),
            DOWN_KEY: Vector2(0,1),
            RIGHT_KEY: Vector2(1,0),
            LEFT_KEY: Vector2(-1,0)
        }

        self.length = default_length_snake
        self.player_number = 0
        self.score = 0

        self.type = "snake"

        self.reset()

        # Son quand le serpent mange une pomme
        self.eating_sound = pygame.mixer.Sound('sounds/crack.wav')

    def set_player_number(self,player_number):
        self.player_number = player_number

    def get_image(self,name):
        key = name+'_ghosted' if self.ghost_activated == True else name
        if not key in dir(self):
            image = pygame.image.load('graphisms/'+name+'.png').convert_alpha()
            if self.ghost_activated == True:
                image.set_alpha(150)
            setattr(self, key, image)

        return getattr(self, key)

    def reset(self):
        super().reset()
        self.alive = True
        self.lost_ghost_in = 0
        self.ghost_activated = False
        self.lost_fire_in = 0
        self.fire = None
        self.direction = Vector2(0,0)
        self.collisionned_entity = 0

    def draw(self):
        self.update_head_graphisms()
        self.update_tail_graphisms()

        for index, block in enumerate(self.body):
            # On crée les rect pour les positions
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size,cell_size)

            # Tête du serpent
            if index == 0:
                screen.blit(self.head,block_rect)
            # Queue du serpent
            elif index == len(self.body) - 1 :
                screen.blit(self.tail,block_rect)
            # Corps du serpent
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x :
                    screen.blit(self.get_image('body_vertical'),block_rect)
                elif previous_block.y == next_block.y :
                    screen.blit(self.get_image('body_horizontal'),block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1 :
                        screen.blit(self.get_image('body_tl'), block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1 :
                        screen.blit(self.get_image('body_bl'), block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1 :
                        screen.blit(self.get_image('body_tr'), block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1 :
                        screen.blit(self.get_image('body_br'), block_rect)

    def update_head_graphisms(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.get_image('head_left')
        elif head_relation == Vector2(-1,0): self.head = self.get_image('head_right')
        elif head_relation == Vector2(0,1): self.head = self.get_image('head_up')
        elif head_relation == Vector2(0,-1): self.head = self.get_image('head_down')

    def update_tail_graphisms(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.get_image('tail_left')
        elif tail_relation == Vector2(-1,0): self.tail = self.get_image('tail_right')
        elif tail_relation == Vector2(0,1): self.tail = self.get_image('tail_up')
        elif tail_relation == Vector2(0,-1): self.tail = self.get_image('tail_down')


    def set_party(self,party):
        self.party = party
        self.auto_set_id()
        self.party.players[self.player_number] = self

    def move_snake(self):
        if self.direction == Vector2(0,0):
            return

        body_copy = self.body[:]
        blocks_to_add = self.score-(len(self.body)-default_length_snake)
        if blocks_to_add <= 0:
            to_loop = 1+min(-1*blocks_to_add, len(self.body)-default_length_snake)
            for i in range(to_loop):
                if self.party.tab[int(self.body[-1].y)][int(self.body[-1].x)] != 0 and self.party.tab[int(self.body[-1].y)][int(self.body[-1].x)].id == self.id:
                    self.party.tab[int(self.body[-1].y)][int(self.body[-1].x)] = 0
                body_copy = body_copy[:-1]

        body_copy.insert(0,body_copy[0] + self.direction)
        self.collisionned_entity = self.party.tab[int(body_copy[0].y)][int(body_copy[0].x)]
        self.party.tab[int(body_copy[0].y)][int(body_copy[0].x)] = self

        self.body = body_copy[:]

        if self.fire != None:
            self.fire.place()

    def add_block(self, n = 1):
        self.score += n

    def remove_block(self, n = 1):
        self.score = max(0,self.score-1)

    def play_eating_sound(self):
        self.eating_sound.play()

    def create_fire(self):
        if self.fire == None:
            fire = FIRE(self.party,self)
            fire.place()
            self.fire = fire
        self.lost_fire_in = random.randint(1,2)

    def remove_fire(self):
        if self.fire != None:
            self.fire.reset()
            self.fire.delete()
            self.fire = None

    def kill(self):
        self.delete()
        self.alive = False

    def delete(self):
        self.remove_fire()
        super().delete()

    def collision(self,snake):
        if self.id != snake.id or self.ghost_activated == False:
            self.party.game_over(snake)
            return False
        return True
