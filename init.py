import pygame


pygame.mixer.pre_init(44100,-16,2,512) # Précharge le son pour éviter un potentiel délai
pygame.init()

#screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
screen = pygame.display.set_mode((854,480))

clock = pygame.time.Clock()

clock.tick(60) #La boucle s'exécute 60 fois par seconde, correspondant aux 60 FPS

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #L'event sera trigger toutes les 150 millisecondes
