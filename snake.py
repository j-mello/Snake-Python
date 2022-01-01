import pygame, sys, random
from pygame.math import Vector2

pygame.mixer.pre_init(44100,-16,2,512) # Précharge le son pour éviter un potentiel délai
pygame.init()

clock = pygame.time.Clock()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
apple = pygame.image.load('graphisms/apple.png').convert_alpha()
game_font = pygame.font.Font('fonts/Marcha.ttf', 25)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

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

    def draw_snake(self):
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
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False

        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_eating_sound(self):
        self.eating_sound.play()

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        #create the rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        #draw the rectangle
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen,(126,166,114), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.grass()
        self.score()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: #Si le fruit et la tête du serpent sont à la même position
            # bruitage
            self.snake.play_eating_sound()
            # replacer un fruit ailleurs
            self.fruit.randomize()
            # rendre le serpent plus grand
            self.snake.add_block()
        
        # empêcher le fruit d'apparaitre sur le serpent
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    
    def check_fail(self):
        #Si snake est en dehors de l'écran
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        #Si snake se touche lui-même
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
    
    def grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
    
    def score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 8 ,apple_rect.height + 4)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT #creation d'un event
pygame.time.set_timer(SCREEN_UPDATE, 150) #L'event sera trigger toutes les 150 millisecondes

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) #La boucle s'exécute 60 fois par seconde, correspondant aux 60 FPS