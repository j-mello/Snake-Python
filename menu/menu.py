from init import pygame, screen, SCREEN_UPDATE
from config import menu_dimensions
from menu.buttons import buttons, validate_button
from menu.define_coordinates import define_coordinates
from menu.listen_buttons import listen_buttons
from menu.display_buttons import display_buttons

def menu():
    screen = pygame.display.set_mode(menu_dimensions)

    define_coordinates()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                listen_buttons(mouse)

            if event.type == SCREEN_UPDATE:
                display_buttons()

            mouse = pygame.mouse.get_pos()
