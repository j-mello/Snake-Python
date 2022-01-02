import pygame


pygame.mixer.pre_init(44100,-16,2,512) # Précharge le son pour éviter un potentiel délai
pygame.init()

cell_size = 40
cell_number = 22
default_length_snake = 3
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
apple = pygame.image.load('graphisms/apple.png').convert_alpha()
game_font = pygame.font.Font('fonts/Marcha.ttf', 25)
background_color = (175,215,70)
grass_color = (167,209,61)
score_color = (56,74,12)

# Les id des serpents iront de 10 à 19
snake_group_id = 10

# Les id des murs iront de 20 à 29
wall_group_id = 20

# les ids des fruits irons de 40 à 49
fruit_group_id = 40