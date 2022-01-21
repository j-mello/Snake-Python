from init import pygame

cell_size = 40
cell_number = 20
default_length_snake = 3
game_font = pygame.font.Font('fonts/Marcha.ttf', 25)
background_color = (175,215,70)
grass_color = (167,209,61)
score_color = (56,74,12)

menu_dimensions = (854,480)
menu_validate_button_y = 20
menu_y_margin = 50
menu_x_margin = 30
menu_text_bottom_margin = 20
menu_body_height = 100
menu_font = pygame.font.SysFont("comicsansms", 15)
settable_values_menu_font = pygame.font.SysFont("comicsansms", 20)

fruit_icon = pygame.image.load('graphisms/apple.png').convert_alpha()
skull_icon = pygame.image.load('graphisms/skull.png').convert_alpha()
ghost_fruit_icon = pygame.image.load('graphisms/ghost_apple.png').convert_alpha()
super_fruit_icon = pygame.image.load('graphisms/super_apple.png').convert_alpha()
bad_fruit_icon = pygame.image.load('graphisms/bad_apple.png').convert_alpha()
fire_fruit_icon = pygame.image.load('graphisms/fire_apple.png').convert_alpha()
fire_icon = pygame.image.load('graphisms/fire.png').convert_alpha()
tonic_icon = pygame.image.load('graphisms/tonic.png').convert_alpha()
wormhole_icon = pygame.image.load('graphisms/wormhole.png').convert_alpha()
wall_icon = pygame.image.load('graphisms/wall.png').convert_alpha()
ghost_wall_icon = pygame.image.load('graphisms/wall.png').convert_alpha()
ghost_wall_icon.set_alpha(100)



config_game = {

    #Afficher aléatoirement des murs dans le niveau
    "nb_random_walls": 0,

    #Afficher aléatoirement de nouveaux murs supplémentaire à chaque fruit mangé
    "new_random_walls_at_each_new_fruit": False,

    #Le nombre de trous de ver
    "nb_wormholes": 0,

    #Remplacer les murs des coté, par des grilles qui téléportent de l'autre coté
    "use_tonic_grills": False,

    #Depuis diminuer la tailler du niveau régulièrement
    "periodically_shrink_grill": 0,

    #Activer les super fruits
    "use_super_fruit": False,

    #Activer les mauvais fruits
    "use_bad_fruit": False,

    #Activer les fruits fantômes
    "use_ghost_fruit": False,

    #Activer les fruits de feu
    "use_fire_fruit": False
}
