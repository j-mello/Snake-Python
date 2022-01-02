from init import screen, game_font, cell_number, cell_size, apple, grass_color, score_color, pygame, default_length_snake, fruit_group_id
from FRUIT import FRUIT
from WALL import WALL
from pygame.math import Vector2

class PARTY:
    def __init__(self,snakes):

        self.tab = [[0]*cell_number for i in range(cell_number)]

        self.fruits = []
        self.snakes = snakes
        for (id,snake) in enumerate(self.snakes):
            snake.set_party(self)
            snake.set_id(id)

            fruit = FRUIT()
            fruit.set_id(id)
            fruit.set_party(self)
            fruit.place_randomly()
            self.fruits.append(fruit)


        self.walls = []

        for  id,(pos,orientation) in enumerate([(Vector2(cell_number-1,0),Vector2(1,0)),(Vector2(cell_number-1,cell_number-1),Vector2(0,1)),(Vector2(0,cell_number-1),Vector2(-1,0)),(Vector2(0,0),Vector2(0,-1))]):
            wall = WALL()
            wall.set_id(id)
            wall.set_party(self)
            wall.place(pos,orientation)
            self.walls.append(wall)

        self.reset()


    def reset(self):
        for snake in self.snakes:
            snake.reset()
            snake.place_randomly()

        for fruit in self.fruits:
            fruit.reset()
            fruit.place_randomly()

    def update(self):
        for (index,snake) in enumerate(self.snakes):
            snake.move_snake(index)
        self.check_collision()

    def draw_elements(self):
        self.grass()
        for snake in self.snakes:
            snake.draw()
        for wall in self.walls:
            wall.draw()
        for fruit in self.fruits:
            fruit.draw()
        self.scores()

    def check_collision(self):
        for snake in self.snakes:
            if not 0 <= snake.body[0].x < cell_number or not 0 <= snake.body[0].y < cell_number:
                self.game_over()
                return
            if snake.collisionned_block != 0:
                type = snake.collisionned_block//10*10
                if (type == fruit_group_id):
                    # bruitage
                    snake.play_eating_sound()
                    # replacer un fruit ailleurs
                    fruit = self.get_fruit_by_id(snake.collisionned_block)
                    fruit.place_randomly()
                    # rendre le serpent plus grand
                    snake.add_block()
                    snake.collisionned_block = 0
                else:
                    self.game_over()

    def get_fruit_by_id(self,id):
        for fruit in self.fruits:
            if fruit.id == id:
                return fruit
        return None

    def game_over(self):
        self.reset()

    def grass(self):
        for row in range(cell_number):
            for col in range(cell_number):
                if row % 2 == col % 2:
                    grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def scores(self):
        for (i,snake) in enumerate(self.snakes):
            score_text = str(len(snake.body) - default_length_snake)
            score_surface = game_font.render(score_text, True, score_color)
            score_x = int(cell_size * cell_number - 60) - cell_size*3*i
            score_y = int(cell_size * cell_number - 40)
            score_rect = score_surface.get_rect(center = (score_x, score_y))
            apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
            bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 8 ,apple_rect.height + 4)

            who_surface = game_font.render(f"Joueur {i+1} : ", True, score_color)
            who_rect = who_surface.get_rect(center = (score_x-cell_size/2, score_y-cell_size))

            pygame.draw.rect(screen,grass_color,bg_rect)
            screen.blit(who_surface,who_rect)
            screen.blit(score_surface, score_rect)
            screen.blit(apple, apple_rect)
            pygame.draw.rect(screen,score_color,bg_rect,2)