from init import pygame, screen, SCREEN_UPDATE
from config import (menu_dimensions,
                   menu_y_margin,
                   menu_x_margin,
                   menu_validate_button_y,
                   menu_body_height,
                   menu_font,
                   settable_values_menu_font,
                   menu_text_bottom_margin)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                listen_buttons(mouse)


            if event.type == SCREEN_UPDATE:
                display_buttons()

            mouse = pygame.mouse.get_pos()
