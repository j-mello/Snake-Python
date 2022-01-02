from init import screen, game_font, cell_number, cell_size, apple, grass_color, score_color, pygame, default_length_snake
from FRUIT import FRUIT
import random
from pygame.math import Vector2

class PARTY:
    def __init__(self,snakes):
        self.snakes = snakes
        for snake in self.snakes:
            snake.set_party(self)
        self.tab = [[0]*cell_number for i in range(cell_number)]
        self.reset()


    def reset(self):
        for snake in self.snakes:
            snake.reset()
            self.place_randomly(snake)

        self.fruit = FRUIT()

    def place_randomly(self,element):
        while True:
            orientation = [Vector2(0,-1),Vector2(1,0),Vector2(0,1),Vector2(-1,0)][random.randint(0,3)]

            pos_x = random.randint(0,cell_number-1)
            pos_y = random.randint(0,cell_number-1)
            pos = Vector2(pos_x,pos_y)
            if (self.check_random_placement(orientation,pos,element.length) == True):
                break

        element.orientation = orientation
        element.body = []
        for i in range(element.length):
            block = pos-orientation*i
            self.tab[int(block.y)][int(block.x)] = 1
            element.body.append(block)

    def check_random_placement(self,orientation,pos,length):
        for i in range(length):
            block = pos-orientation*i
            if not 0 <= block.x < cell_number or not 0 <= block.y < cell_number or self.tab[int(block.y)][int(block.x)] != 0:
                return False
        return True

    def update(self):
        for (index,snake) in enumerate(self.snakes):
            snake.move_snake(index)
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.grass()
        self.score()
        for snake in self.snakes:
            snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        for snake in self.snakes:
            if self.fruit.pos == snake.body[0]: #Si le fruit et la tête du serpent sont à la même position
                # bruitage
                snake.play_eating_sound()
                # replacer un fruit ailleurs
                self.fruit.randomize()
                # rendre le serpent plus grand
                snake.add_block()

        # empêcher le fruit d'apparaitre sur le serpent
        while any(any(pos == self.fruit.pos for pos in snake.body[1:]) for snake in self.snakes):
            self.fruit.randomize()


    def check_fail(self):
        #Si snake est en dehors de l'écran
        for snake in self.snakes:
            if not 0 <= snake.body[0].x < cell_number or not 0 <= snake.body[0].y < cell_number:
                self.game_over()

            if (snake.collisionned_block != 0):
                self.game_over()

    def game_over(self):
        self.reset()

    def grass(self):
        for row in range(cell_number):
            for col in range(cell_number):
                if row % 2 == col % 2:
                    grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def score(self):
        snake = self.snakes[0]
        score_text = str(len(snake.body) - default_length_snake)
        score_surface = game_font.render(score_text, True, score_color)
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 8 ,apple_rect.height + 4)

        pygame.draw.rect(screen,grass_color,bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen,score_color,bg_rect,2)