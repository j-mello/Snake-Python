import pygame
from pygame.math import Vector2
from init import screen, cell_size, default_length_snake, snake_group_id
from ELEMENT import ELEMENT

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
        self.group_id = snake_group_id

        self.reset()

        # Graphismes pour la tête du serpent
        self.head_up = pygame.image.load('graphisms/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphisms/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('graphisms/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphisms/head_left.png').convert_alpha()

        # Graphismes pour la queue du serpent
        self.tail_up = pygame.image.load('graphisms/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphisms/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphisms/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphisms/tail_left.png').convert_alpha()

        # Graphismes pour le corps du serpent
        self.body_vertical = pygame.image.load('graphisms/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('graphisms/body_horizontal.png').convert_alpha()

        # Graphismes pour le corps du serpent en train de tourner
        self.body_tr = pygame.image.load('graphisms/body_topright.png').convert_alpha()
        self.body_tl = pygame.image.load('graphisms/body_topleft.png').convert_alpha()
        self.body_br = pygame.image.load('graphisms/body_bottomright.png').convert_alpha()
        self.body_bl = pygame.image.load('graphisms/body_bottomleft.png').convert_alpha()

        # Son quand le serpent mange une pomme
        self.eating_sound = pygame.mixer.Sound('sounds/crack.wav')

    def reset(self):
        super().reset()
        self.direction = Vector2(0,0)
        self.new_block = 0
        self.collisionned_block = 0

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
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y :
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1 :
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1 :
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1 :
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1 :
                        screen.blit(self.body_br, block_rect)

    def update_head_graphisms(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphisms(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.direction == Vector2(0,0):
            return

        body_copy = self.body[:]
        if self.new_block > 0:
            self.new_block -= 1
        else:
            to_loop = 1+min(-1*self.new_block, len(self.body)-default_length_snake)
            for i in range(to_loop):
                self.party.tab[int(self.body[-1].y)][int(self.body[-1].x)] = 0
                body_copy = body_copy[:-1]
            if self.new_block < 0:
                self.new_block = 0

        body_copy.insert(0,body_copy[0] + self.direction)
        self.collisionned_block = self.party.tab[int(body_copy[0].y)][int(body_copy[0].x)]
        self.party.tab[int(body_copy[0].y)][int(body_copy[0].x)] = self.id

        self.body = body_copy[:]

    def add_block(self, n = 1):
        self.new_block += n

    def remove_block(self, n = 1):
        self.new_block -= n

    def play_eating_sound(self):
        self.eating_sound.play()
