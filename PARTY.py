import pygame
from init import screen, game_font, cell_number, cell_size, apple, grass_color, score_color
from SNAKE import SNAKE
from FRUIT import FRUIT

class PARTY:
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
        while any(pos == self.fruit.pos for pos in self.snake.body[1:]):
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
        for row in range(cell_number):
            for col in range(cell_number):
                if row % 2 == col % 2:
                    grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def score(self):
        score_text = str(len(self.snake.body) - 3)
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