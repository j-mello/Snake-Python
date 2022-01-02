import pygame


pygame.mixer.pre_init(44100,-16,2,512) # Précharge le son pour éviter un potentiel délai
pygame.init()

cell_size = 40
cell_number = 22
default_length_snake = 3
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
game_font = pygame.font.Font('fonts/Marcha.ttf', 25)
background_color = (175,215,70)
grass_color = (167,209,61)
score_color = (56,74,12)

fruit_icon = pygame.image.load('graphisms/apple.png').convert_alpha()
tonic_icon = pygame.image.load('graphisms/tonic.png').convert_alpha()

#Afficher aléatoirement des murs dans le niveau
nb_random_walls = 10

#Remplacer les murs des coté, par des grilles qui téléportent de l'autre coté
use_tonic_grills = True




# Les id des serpents iront de 100 à 199
snake_group_id = 100

# Les id des murs iront de 200 à 299
wall_group_id = 200

# les ids des fruits irons de 400 à 499
fruit_group_id = 400

# Les ids des grilles tonique irons de 500 à 599
tonic_group_id = 500