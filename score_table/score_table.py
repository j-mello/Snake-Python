from init import pygame, screen, SCREEN_UPDATE
from config import menu_dimensions
from score_table.show_scores import show_scores
from score_table.listen_buttons import listen_back_button, listen_delete_scores_button
from score_table.config import scroll_scale
import json

get_longer_col_len = lambda obj: max( [*list(map(len,list(obj.values()) ) ),0] )

def scroll(a,b,obj,factor):

    scale = min(scroll_scale,get_longer_col_len(obj)-b) if factor == 1 else min(scroll_scale,a)
    a += scale*factor
    b += scale*factor
    return a,b

def score_table():
    screen = pygame.display.set_mode(menu_dimensions)

    file_name = "scores.json"
    try:
        with open(file_name, 'r') as file:
            obj = json.loads(file.read())
    except FileNotFoundError:
        obj = {}
    a = 0
    b = min(5,get_longer_col_len(obj))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == SCREEN_UPDATE:
                show_scores(obj,a,b)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    listen_back_button(mouse)
                    if listen_delete_scores_button(mouse):
                        obj = {}
                        a = 0
                        b = 0
                elif event.button == 4:
                    a,b = scroll(a,b,obj,-1)
                elif event.button == 5:
                    a,b = scroll(a,b,obj,1)

            mouse = pygame.mouse.get_pos()

