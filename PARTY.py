from init import screen, game_font, cell_number, cell_size, fruit_icon, grass_color, score_color, pygame, default_length_snake, fruit_group_id, snake_group_id, wall_group_id, wormhole_group_id, ghostwall_group_id, tonic_group_id, fire_group_id, nb_random_walls, nb_wormholes, use_tonic_grills, new_random_walls_at_each_new_fruit, periodically_shrink_grill, use_super_fruit, use_bad_fruit, use_ghost_fruit, use_fire_fruit
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

        self.elements = []


        self.place_walls()


        for i in range(nb_random_walls):
            wall = WALL(self,random.randint(3,6))
            wall.randomly = True
            wall.set_id(4+i)
            self.elements.append(wall)


        for (id,snake) in enumerate(snakes):
            snake.set_party(self)
            snake.set_id(id)
            self.elements.append(snake)

            fruit = FRUIT(self)
            fruit.set_id(id)
            self.elements.append(fruit)

        for id in range(nb_wormholes):
            wormhole = WORMHOLE(self)
            wormhole.set_id(id)
            self.elements.append(wormhole)


        self.reset()


    def place_walls(self):
        for  id,(pos,orientation) in enumerate([(Vector2(self.cell_number-1,0),Vector2(1,0)),(Vector2(self.cell_number-1,self.cell_number-1),Vector2(0,1)),(Vector2(0,self.cell_number-1),Vector2(-1,0)),(Vector2(0,0),Vector2(0,-1))]):
            if use_tonic_grills == False:
                wall = WALL(self)
            else:
                wall = TONIC_GRILL(self,'V' if id % 2 == 0 else 'H')
            wall.set_id(id)
            wall.place(pos,orientation)
            self.elements.append(wall)

    def place_new_fruit(self,fruit):
        fruit.reset()

        c = (1 if fruit.special_fruit == True else 0)*2 + (1 if random.randint(0,4) <= 3 or all(fruit_to_use == False for fruit_to_use in (use_bad_fruit,use_super_fruit,use_ghost_fruit,use_fire_fruit)) else 0)

        if c == 1 or c == 2:
            fruit.place_randomly()
        else:
            self.delete_element_by_id(fruit.id)
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

            new_fruit.set_id(fruit.id%100)
            new_fruit.place_randomly()
            self.elements.append(new_fruit)


    def reset(self):
        self.cell_number = cell_number
        self.tab = [[0]*cell_number for i in range(cell_number)]
        to_deletes = []
        for i,element in enumerate(self.elements):
            type = element.id//100*100
            if type == snake_group_id or type == fruit_group_id or type == wormhole_group_id or (type == wall_group_id and element.randomly == True):
                element.reset()
                element.place_randomly()
            elif any(type == group_id for group_id in (ghostwall_group_id,wall_group_id,tonic_group_id,fire_group_id)):
                element.reset()
                to_deletes.append(i)

        self.place_walls()

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

    def display_update(self):
        if self.old_cell_number != self.cell_number:
            self.old_cell_number = self.cell_number
            screen = pygame.display.set_mode((self.cell_number*cell_size,self.cell_number*cell_size))
        pygame.display.update()

    def check_collision(self):
        for snake in self.elements:
            if snake.id//100*100 != snake_group_id:
                continue

            if not 0 <= snake.body[0].x < self.cell_number or not 0 <= snake.body[0].y < self.cell_number:
                self.game_over()
                return

            if snake.collisionned_block != 0:
                t = self.get_element_by_id(snake.collisionned_block)
                element = None if t == None else t[0]
                if element != None and element.collision(snake) == False:
                    return

    def get_element_by_id(self,id):
        for (i,element) in enumerate(self.elements):
            if element.id == id:
                return element,i
        return None

    def delete_element_by_id(self,id):
       for (i,element) in enumerate(self.elements):
            if element.id == id:
                del self.elements[i]
                return True
       return False

    def set_dynamic_wall(self):
        if new_random_walls_at_each_new_fruit == False:
            return

        to_deletes = []
        for (i,element) in enumerate(self.elements):
            element = self.elements[i]
            if element.id//100*100 == ghostwall_group_id:
                element.remaining_times -= 1
                if (element.remaining_times == 0):
                    pos = element.pos
                    orientation = element.orientation

                    element.reset()
                    to_deletes.append(i)

                    wall = WALL(self, element.length)
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
            ghost_wall = GHOST_WALL(self,random.randint(3,4))
            ghost_wall.auto_set_id()
            ghost_wall.place_randomly()
            self.elements.append(ghost_wall)


    def shift_element(self,element,index,to_shift,to_deletes):
        old_body = [Vector2(block.x,block.y) for block in element.body]
        element.pos -= to_shift
        for block in element.body:
            block -= to_shift
            if block.x < element.limit_spawn or block.y < element.limit_spawn or (self.tab[int(block.y)][int(block.x)] != 0 and self.tab[int(block.y)][int(block.x)] != element.id):
                if element.id//100*100 != snake_group_id:
                    element.reset()
                    to_deletes.append(index)
                    break

                if block.x < 1 or block.y < 1:
                    self.game_over()
                    return False

                other_element,other_index_element = self.get_element_by_id(self.tab[int(block.y)][int(block.x)])
                if other_element.place_randomly_when_shrink == True:
                    other_element.reset()
                    other_element.place_randomly()
                    continue

                if self.tab[int(block.y)][int(block.x)]//100*100 == snake_group_id:
                    self.shift_element(other_element,other_index_element,to_shift,to_deletes)
                    continue

                other_element.reset()
                to_deletes.append(other_index_element)

        if len(to_deletes) == 0 or to_deletes[-1] != index:
            for old_block in old_body:
                self.tab[int(old_block.y)][int(old_block.x)] = 0
            for block in element.body:
                self.tab[int(block.y)][int(block.x)] = element.id
        return True


    def shrink_grill(self):
        if periodically_shrink_grill <= 0 or self.cell_number <= 10 or random.randint(0,1) == 0:
            return

        to_deletes = []
        self.cell_number -= periodically_shrink_grill
        for (i,element) in enumerate(self.elements):
            if (element.id//100*100 == wall_group_id and element.randomly == False) or element.id//100*100 == tonic_group_id:
                element.reset()
                to_deletes.append(i)
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
                    elif self.shift_element(element,i,to_shift,to_deletes) == False:
                        return


        self.tab = [line[:-periodically_shrink_grill] for line in self.tab[:-periodically_shrink_grill]]

        for i in sorted(to_deletes, reverse=True):
            del self.elements[i]

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
        for (i,snake) in enumerate(self.elements):
            if snake.id//100*100 != snake_group_id:
               continue

            num_player = snake.id%100

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
