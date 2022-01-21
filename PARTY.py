from config import game_font, cell_number, cell_size, fruit_icon, skull_icon, grass_color, score_color, pygame, default_length_snake, config_game
from init import screen
from elements.FRUIT import FRUIT
from elements.SUPER_FRUIT import SUPER_FRUIT
from elements.BAD_FRUIT import BAD_FRUIT
from elements.FIRE_FRUIT import FIRE_FRUIT
from elements.GHOST_FRUIT import GHOST_FRUIT
from elements.WALL import WALL
from elements.TONIC_GRILL import TONIC_GRILL
from elements.WORMHOLE import WORMHOLE
from elements.GHOST_WALL import GHOST_WALL
import random
import json

from pygame.math import Vector2
import random

class PARTY:
    def __init__(self,*snakes):

        self.tab = [[0]*cell_number for i in range(cell_number)]

        self.cell_number = cell_number
        self.old_cell_number = cell_number

        self.elements = {}
        self.players = {}

        self.auto_increment_ids_state = 0

        self.place_walls()


        for i in range(config_game["nb_random_walls"]):
            wall = WALL(self,random.randint(3,6))
            wall.randomly = True


        for (i,snake) in enumerate(snakes):
            snake.set_player_number(i)
            snake.set_party(self)
            fruit = FRUIT(self)

        for id in range(config_game["nb_wormholes"]):
            wormhole = WORMHOLE(self)

        self.reset()


    def reset(self):
        self.cell_number = cell_number
        self.playing = True
        self.tab = [[0]*cell_number for i in range(cell_number)]
        to_deletes = []
        for element in self.elements.values():
            if element.type == "fruit" or element.type == "wormhole" or (element.type == "wall" and element.randomly == True):
                element.reset()
                element.place_randomly()
            elif any(element.type == type for type in ("ghost_wall","wall","tonic_grill","fire")):
                to_deletes.append(element)

        for element in to_deletes:
            element.delete()

        for player in self.players.values():
            self.elements[player.id] = player
            player.alive = True
            player.score = 0
            player.reset()
            player.place_randomly()

        self.place_walls()


    def place_walls(self):
        for  id,(pos,orientation) in enumerate([(Vector2(self.cell_number-1,0),Vector2(1,0)),(Vector2(self.cell_number-1,self.cell_number-1),Vector2(0,1)),(Vector2(0,self.cell_number-1),Vector2(-1,0)),(Vector2(0,0),Vector2(0,-1))]):
            if config_game["use_tonic_grills"] == False:
                wall = WALL(self)
            else:
                wall = TONIC_GRILL(self,'V' if id % 2 == 0 else 'H')
            wall.place(pos,orientation)

    def place_new_fruit(self,fruit):
        fruit.reset()

        c = (1 if fruit.special_fruit == True else 0)*2 + (1 if random.randint(0,4) <= 3 or all(fruit_to_use == False for fruit_to_use in (config_game["use_bad_fruit"],config_game["use_super_fruit"],config_game["use_ghost_fruit"],config_game["use_fire_fruit"])) else 0)

        if c == 1 or c == 2:
            fruit.place_randomly()
        else:
            fruit.delete()
            if fruit.special_fruit == True:
                new_fruit = FRUIT(self)
            else:
                possibles_fruits = []
                if config_game["use_super_fruit"] == True:
                    possibles_fruits.append(SUPER_FRUIT)
                if config_game["use_bad_fruit"] == True:
                    possibles_fruits.append(BAD_FRUIT)
                if config_game["use_ghost_fruit"] == True:
                    possibles_fruits.append(GHOST_FRUIT)
                if config_game["use_fire_fruit"] == True:
                    possibles_fruits.append(FIRE_FRUIT)

                fruit_class = possibles_fruits[random.randint(0,len(possibles_fruits)-1)]
                new_fruit = fruit_class(self)

            new_fruit.place_randomly()

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

            if len(snake.body) == 0 or not 0 <= snake.body[0].x < self.cell_number or not 0 <= snake.body[0].y < self.cell_number:
                self.game_over(snake)
                return

            if snake.collisionned_entity != 0:
                if snake.collisionned_entity.collision(snake) == False:
                    return
                snake.collisionned_entity = 0

    def set_dynamic_wall(self):
        if config_game["new_random_walls_at_each_new_fruit"] == False:
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


    def shift_element(self,element,to_shift):
        old_body = [Vector2(block.x,block.y) for block in element.body]
        element.pos -= to_shift
        for block in element.body:
            block -= to_shift
            if block.x < element.limit_spawn or block.y < element.limit_spawn or (self.tab[int(block.y)][int(block.x)] != 0 and self.tab[int(block.y)][int(block.x)].id != element.id):
                if element.type != "snake":
                    element.delete()
                    return False

                if block.x < 1 or block.y < 1:
                    self.game_over(element)
                    return False

                other_element = self.tab[int(block.y)][int(block.x)]
                if other_element.place_randomly_when_shrink == True:
                    other_element.delete()
                    continue

                if other_element.type == "snake":
                    self.shift_element(other_element,to_shift)
                    continue

                other_element.delete()


        for old_block in old_body:
            if self.tab[int(old_block.y)][int(old_block.x)].id == element.id:
                self.tab[int(old_block.y)][int(old_block.x)] = 0
        for block in element.body:
            self.tab[int(block.y)][int(block.x)] = element
        return True


    def shrink_grill(self):
        if config_game["periodically_shrink_grill"] <= 0 or self.cell_number <= 10 or random.randint(0,1) == 0:
            return

        self.cell_number -= config_game["periodically_shrink_grill"]
        for element in list(self.elements.values()):
            if (element.type == "wall" and element.randomly == False) or element.type == "tonic_grill":
                element.delete()
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
                    elif self.shift_element(element,to_shift) == False:
                        return

        self.tab = [line[:-config_game["periodically_shrink_grill"]] for line in self.tab[:-config_game["periodically_shrink_grill"]]]

        self.place_walls()


    def game_over(self,snake):
        snake.kill()
        alive_players = sum([1 for player in self.players.values() if player.alive])
        if alive_players <= 1:
            for snake in self.players.values():
                snake.direction = Vector2(0,0)
            self.save_scores()
            self.playing = False


    def save_scores(self):
        file_name = "scores.json"
        try:
            with open(file_name, 'r') as file:
                obj = json.loads(file.read())
        except FileNotFoundError:
            obj = {}

        for num,player in self.players.items():
            if not str(num+1) in obj:
                obj[str(num+1)] = []
            obj[str(num+1)].append(player.score)

        with open(file_name, 'w') as file:
            file.write(json.dumps(obj))

    def grass(self):
        for row in range(self.cell_number):
            for col in range(self.cell_number):
                if row % 2 == col % 2:
                    grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def scores(self):
        font = game_font if self.playing else pygame.font.Font('fonts/Marcha.ttf', int(50*self.cell_number/20))

        if self.playing == False:
            sentence_font = pygame.font.SysFont("comicsansms", int(35*self.cell_number/20))

            sentence_text = "Appuyez sur entrer pour recommencer"
            sentence_height = font.size(sentence_text)[1]

            sentence_surface = sentence_font.render(sentence_text, True, score_color)
            sentence_x = cell_size * self.cell_number / 2
            sentence_y = cell_size * self.cell_number / 2 + sentence_height

            sentence_rect = sentence_surface.get_rect(center = (sentence_x, sentence_y))

            screen.blit(sentence_surface,sentence_rect)


        for (player_number,snake) in self.players.items():

            score_text = str(snake.score)
            score_surface = font.render(score_text, True, score_color)
            score_x = int(cell_size * self.cell_number - 60) - cell_size * 3 * player_number if self.playing else int(cell_size * self.cell_number - 120*self.cell_number/20) - cell_size * 6*self.cell_number/20 * player_number
            score_y = int(cell_size * self.cell_number - 40) if self.playing else int(cell_size * self.cell_number/2)
            score_rect = score_surface.get_rect(center = (score_x, score_y))

            icon = fruit_icon if snake.alive or self.playing == False else skull_icon
            icon_rect = icon.get_rect(midright = (score_rect.left, score_rect.centery))

            bg_rect = pygame.Rect(icon_rect.left, icon_rect.top - (0 if self.playing else 8), icon_rect.width + score_rect.width + 8 ,icon_rect.height + (4 if self.playing else 12))

            who_surface = font.render(f"Joueur {player_number+1} : ", True, score_color)
            who_rect = who_surface.get_rect(center = (score_x-cell_size/2, score_y-( cell_size if self.playing else 1.5*cell_size ) ))

            pygame.draw.rect(screen,grass_color,bg_rect)
            screen.blit(who_surface,who_rect)
            screen.blit(score_surface, score_rect)
            screen.blit(icon, icon_rect)
            pygame.draw.rect(screen,score_color,bg_rect,2)
