from init import pygame, screen, SCREEN_UPDATE
from config import menu_dimensions
from score_table.show_scores import show_scores
from score_table.listen_back_button import listen_back_button
import json

def score_table():
    screen = pygame.display.set_mode(menu_dimensions)

    file_name = "scores.json"
    try:
        with open(file_name, 'r') as file:
            obj = json.loads(file.read())
    except FileNotFoundError:
        obj = {}

    a = 0
    b = 10

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == SCREEN_UPDATE:
                show_scores(obj,a,b)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    listen_back_button(mouse)

            mouse = pygame.mouse.get_pos()

