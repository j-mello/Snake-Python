from init import screen, game_font, cell_number, cell_size, fruit_icon, grass_color, score_color, pygame, default_length_snake, nb_random_walls, nb_wormholes, use_tonic_grills, new_random_walls_at_each_new_fruit, periodically_shrink_grill, use_super_fruit, use_bad_fruit, use_ghost_fruit, use_fire_fruit
from FRUIT import FRUIT
from SUPER_FRUIT import SUPER_FRUIT
from BAD_FRUIT import BAD_FRUIT
from FIRE_FRUIT import FIRE_FRUIT
from GHOST_FRUIT import GHOST_FRUIT
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

        self.cell_number = cell_number
        self.old_cell_number = cell_number

        self.elements = {}

        self.auto_increment_ids_state = 0

        self.place_walls()


        for i in range(nb_random_walls):
            wall = WALL(self,random.randint(3,6))
            wall.randomly = True


        for (i,snake) in enumerate(snakes):
            snake.set_party(self)
            snake.set_player_number(i)
            fruit = FRUIT(self)

        for id in range(nb_wormholes):
            wormhole = WORMHOLE(self)


        self.reset()


    def place_walls(self):
        for  id,(pos,orientation) in enumerate([(Vector2(self.cell_number-1,0),Vector2(1,0)),(Vector2(self.cell_number-1,self.cell_number-1),Vector2(0,1)),(Vector2(0,self.cell_number-1),Vector2(-1,0)),(Vector2(0,0),Vector2(0,-1))]):
            if use_tonic_grills == False:
                wall = WALL(self)
            else:
                wall = TONIC_GRILL(self,'V' if id % 2 == 0 else 'H')
            wall.place(pos,orientation)

    def place_new_fruit(self,fruit):
        fruit.reset()

        c = (1 if fruit.special_fruit == True else 0)*2 + (1 if random.randint(0,4) <= 3 or all(fruit_to_use == False for fruit_to_use in (use_bad_fruit,use_super_fruit,use_ghost_fruit,use_fire_fruit)) else 0)

        if c == 1 or c == 2:
            fruit.place_randomly()
        else:
            fruit.delete()
            if fruit.special_fruit == True:
                new_fruit = FRUIT(self)
            else:
                possibles_fruits = []
                if use_super_fruit == True:
                    possibles_fruits.append(SUPER_FRUIT)
                if use_bad_fruit == True:
                    possibles_fruits.append(BAD_FRUIT)
                if use_ghost_fruit == True:
                    possibles_fruits.append(GHOST_FRUIT)
                if use_fire_fruit == True:
                    possibles_fruits.append(FIRE_FRUIT)

                fruit_class = possibles_fruits[random.randint(0,len(possibles_fruits)-1)]
                new_fruit = fruit_class(self)

            new_fruit.place_randomly()


    def reset(self):
        self.cell_number = cell_number
        self.tab = [[0]*cell_number for i in range(cell_number)]
        to_deletes = []
        for element in self.elements.values():
            if element.type == "snake" or element.type == "fruit" or element.type == "wormhole" or (element.type == "wall" and element.randomly == True):
                element.reset()
                element.place_randomly()
            elif any(element.type == type for type in ("ghost_wall","wall","tonic_grill","fire")):
                to_deletes.append(element)

        for element in to_deletes:
            element.delete()
        self.place_walls()

    def update(self):
        for element in self.elements.values():
            if element.type == "snake":
                element.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.grass()
        for element in self.elements.values():
            element.draw()
        self.scores()

    def display_update(self):
        if self.old_cell_number != self.cell_number:
            self.old_cell_number = self.cell_number
            screen = pygame.display.set_mode((self.cell_number*cell_size,self.cell_number*cell_size))
        pygame.display.update()

    def check_collision(self):
        for snake in list(self.elements.values()):
            if snake.type != "snake":
                continue

            if not 0 <= snake.body[0].x < self.cell_number or not 0 <= snake.body[0].y < self.cell_number:
                self.game_over()
                return

            if snake.collisionned_entity != 0:
                if snake.collisionned_entity.collision(snake) == False:
                    return
                snake.collisionned_entity = 0

    def set_dynamic_wall(self):
        if new_random_walls_at_each_new_fruit == False:
            return

        for element in list(self.elements.values()):
            if element.type == "ghost_wall":
                element.remaining_times -= 1
                if (element.remaining_times == 0):
                    pos = element.pos
                    orientation = element.orientation

                    element.delete()

                    wall = WALL(self, element.length)
                    wall.place(pos,orientation)
                    wall.delete_at_next_game = True
                    wall.delete_in = random.randint(2,3)
            elif element.type == "wall" and element.delete_in != False:
                element.delete_in -= 1
                if element.delete_in == 0:
                    element.delete()

        for i in range(random.randint(1,2)):
            ghost_wall = GHOST_WALL(self,random.randint(3,4))
            ghost_wall.place_randomly()


    def shift_element(self,element,to_shift,to_deletes):
        old_body = [Vector2(block.x,block.y) for block in element.body]
        element.pos -= to_shift
        for block in element.body:
            block -= to_shift
            if block.x < element.limit_spawn or block.y < element.limit_spawn or (self.tab[int(block.y)][int(block.x)] != 0 and self.tab[int(block.y)][int(block.x)].id != element.id):
                if element.type != "snake":
                    to_deletes.append(element)
                    break

                if block.x < 1 or block.y < 1:
                    self.game_over()
                    return False

                other_element = self.tab[int(block.y)][int(block.x)]
                if other_element.place_randomly_when_shrink == True:
                    to_deletes.append(other_element)
                    continue

                if other_element.type == "snake":
                    self.shift_element(other_element,to_shift,to_deletes)
                    continue

                to_deletes.append(other_element)

        if len(to_deletes) == 0 or to_deletes[-1].id != element.id:
            for old_block in old_body:
                self.tab[int(old_block.y)][int(old_block.x)] = 0
            for block in element.body:
                self.tab[int(block.y)][int(block.x)] = element
        return True


    def shrink_grill(self):
        if periodically_shrink_grill <= 0 or self.cell_number <= 10 or random.randint(0,1) == 0:
            return

        self.cell_number -= periodically_shrink_grill
        to_deletes = []
        for element in self.elements.values():
            if (element.type == "wall" and element.randomly == False) or element.type == "tonic_grill":
                to_deletes.append(element)
                continue

            checking_element = True
            while checking_element:
                checking_element = False
                to_shift = Vector2(0,0)
                for block in element.body:
                    if block.x >= self.cell_number-element.limit_spawn and to_shift.x == 0:
                        checking_element = True
                        to_shift.x = 1
                    if block.y >= self.cell_number-element.limit_spawn and to_shift.y == 0:
                        checking_element = True
                        to_shift.y = 1
                    if to_shift.x == 1 and to_shift.y == 1:
                        break
                if to_shift.x > 0 or to_shift.y > 0:
                    if element.place_randomly_when_shrink == True:
                        element.reset()
                        element.place_randomly()
                        break
                    elif self.shift_element(element,to_shift,to_deletes) == False:
                        return

        for element in to_deletes:
            element.delete()

        self.tab = [line[:-periodically_shrink_grill] for line in self.tab[:-periodically_shrink_grill]]

        self.place_walls()


    def game_over(self):
        self.reset()

    def grass(self):
        for row in range(self.cell_number):
            for col in range(self.cell_number):
                if row % 2 == col % 2:
                    grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def scores(self):
        for snake in self.elements.values():
            if snake.type != "snake":
               continue

            num_player = snake.player_number

            score_text = str(len(snake.body) - default_length_snake)
            score_surface = game_font.render(score_text, True, score_color)
            score_x = int(cell_size * self.cell_number - 60) - cell_size*3*num_player
            score_y = int(cell_size * self.cell_number - 40)
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
