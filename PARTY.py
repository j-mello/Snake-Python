from init import screen, game_font, cell_number, cell_size, fruit_icon, grass_color, score_color, pygame, default_length_snake, fruit_group_id, snake_group_id, wall_group_id, wormhole_group_id, ghostwall_group_id, nb_random_walls, nb_wormholes, use_tonic_grills, new_random_walls_at_each_new_fruit
from FRUIT import FRUIT
from WALL import WALL
from TONIC_GRILL import TONIC_GRILL
from WORMHOLE import WORMHOLE
from GHOST_WALL import GHOST_WALL
import random

from pygame.math import Vector2
import random

class PARTY:
    def __init__(self,snakes):

        self.tab = [[0]*cell_number for i in range(cell_number)]

        self.elements = []

        nb_static_walls = 0
        for  id,(pos,orientation) in enumerate([(Vector2(cell_number-1,0),Vector2(1,0)),(Vector2(cell_number-1,cell_number-1),Vector2(0,1)),(Vector2(0,cell_number-1),Vector2(-1,0)),(Vector2(0,0),Vector2(0,-1))]):
            if use_tonic_grills == False:
                wall = WALL()
                nb_static_walls += 1
            else:
                wall = TONIC_GRILL('V' if id % 2 == 0 else 'H')
            wall.set_id(id)
            wall.set_party(self)
            wall.place(pos,orientation)
            self.elements.append(wall)



        for i in range(nb_random_walls):
            wall = WALL(random.randint(3,6))
            wall.randomly = True
            wall.set_id(i+nb_static_walls)
            wall.set_party(self)
            self.elements.append(wall)


        for (id,snake) in enumerate(snakes):
            snake.set_party(self)
            snake.set_id(id)
            self.elements.append(snake)

            fruit = FRUIT()
            fruit.set_id(id)
            fruit.set_party(self)
            self.elements.append(fruit)

        for id in range(nb_wormholes):
            wormhole = WORMHOLE()
            wormhole.set_id(id)
            wormhole.set_party(self)
            self.elements.append(wormhole)


        self.reset()


    def reset(self):
        to_deletes = []
        for i,element in enumerate(self.elements):
            type = element.id//100*100
            if type == snake_group_id or type == fruit_group_id or type == wormhole_group_id or (type == wall_group_id and element.randomly == True):
                element.reset()
                element.place_randomly()
            elif type == ghostwall_group_id or (type == wall_group_id and element.delete_at_next_game == True):
                element.reset()
                to_deletes.append(i)

        for i in sorted(to_deletes, reverse=True):
            del self.elements[i]

    def update(self):
        for element in self.elements:
            if element.id//100*100 == snake_group_id:
                element.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.grass()
        for element in self.elements:
            element.draw()
        self.scores()

    def check_collision(self):
        for snake in self.elements:
            if snake.id//100*100 != snake_group_id:
                continue

            if not 0 <= snake.body[0].x < cell_number or not 0 <= snake.body[0].y < cell_number:
                self.game_over()
                return

            if snake.collisionned_block != 0:
                element = self.get_element_by_id(snake.collisionned_block)
                if element.collision(snake) == False:
                    return

    def get_element_by_id(self,id):
        for element in self.elements:
            if element.id == id:
                return element
        return None

    def set_dynamic_wall(self):
        if new_random_walls_at_each_new_fruit == False:
            return

        to_deletes = []
        nb_elements = len(self.elements)
        for i in range(nb_elements):
            element = self.elements[i]
            if element.id//100*100 == ghostwall_group_id:
                element.remaining_times -= 1
                if (element.remaining_times == 0):
                    pos = element.pos
                    orientation = element.orientation

                    element.reset()
                    to_deletes.append(i)

                    wall = WALL(element.length)
                    wall.set_party(self)
                    wall.auto_set_id()
                    wall.place(pos,orientation)
                    wall.delete_at_next_game = True
                    wall.delete_in = random.randint(2,3)
                    self.elements.append(wall)
            elif element.id//100*100 == wall_group_id and element.delete_in != False:
                element.delete_in -= 1
                if element.delete_in == 0:
                    to_deletes.append(i)
                    element.reset()


        for i in sorted(to_deletes, reverse=True):
            del self.elements[i]

        for i in range(random.randint(1,2)):
            ghost_wall = GHOST_WALL(random.randint(3,4))
            ghost_wall.set_party(self)
            ghost_wall.auto_set_id()
            ghost_wall.place_randomly()
            self.elements.append(ghost_wall)

    def game_over(self):
        self.reset()

    def grass(self):
        for row in range(cell_number):
            for col in range(cell_number):
                if row % 2 == col % 2:
                    grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def scores(self):
        for (i,snake) in enumerate(self.elements):
            if snake.id//100*100 != snake_group_id:
               continue

            num_player = snake.id%100

            score_text = str(len(snake.body) - default_length_snake)
            score_surface = game_font.render(score_text, True, score_color)
            score_x = int(cell_size * cell_number - 60) - cell_size*3*num_player
            score_y = int(cell_size * cell_number - 40)
            score_rect = score_surface.get_rect(center = (score_x, score_y))
            apple_rect = fruit_icon.get_rect(midright = (score_rect.left, score_rect.centery))
            bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 8 ,apple_rect.height + 4)

            who_surface = game_font.render(f"Joueur {num_player+1} : ", True, score_color)
            who_rect = who_surface.get_rect(center = (score_x-cell_size/2, score_y-cell_size))

            pygame.draw.rect(screen,grass_color,bg_rect)
            screen.blit(who_surface,who_rect)
            screen.blit(score_surface, score_rect)
            screen.blit(fruit_icon, apple_rect)
            pygame.draw.rect(screen,score_color,bg_rect,2)