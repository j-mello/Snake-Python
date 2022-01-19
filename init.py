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
super_fruit_icon = pygame.image.load('graphisms/super_apple.png').convert_alpha()
bad_fruit_icon = pygame.image.load('graphisms/bad_apple.png').convert_alpha()
tonic_icon = pygame.image.load('graphisms/tonic.png').convert_alpha()
wormhole_icon = pygame.image.load('graphisms/wormhole.png').convert_alpha()
wall_icon = pygame.image.load('graphisms/wall.png').convert_alpha()
ghost_wall_icon = pygame.image.load('graphisms/wall.png').convert_alpha()
ghost_wall_icon.set_alpha(100)

#Afficher aléatoirement des murs dans le niveau
nb_random_walls = 3

#Afficher aléatoirement de nouveaux murs supplémentaire à chaque fruit mangé
new_random_walls_at_each_new_fruit = True

#Le nombre de trous de ver
nb_wormholes = 1

#Remplacer les murs des coté, par des grilles qui téléportent de l'autre coté
use_tonic_grills = True

#Depuis diminuer la tailler du niveau régulièrement
periodically_shrink_grill = 2

use_bad_fruit = True




# Les id des serpents iront de 100 à 199
snake_group_id = 100

# Les id des murs iront de 200 à 299
wall_group_id = 200

# Les ids des grilles tonique irons de 300 à 399
tonic_group_id = 300

# les ids des fruits irons de 400 à 499
fruit_group_id = 400

# Les ids des trous de ver irons de 500 à 599
wormhole_group_id = 500

# Les ids des murs fantomes irons de 600 à 699
ghostwall_group_id = 600
