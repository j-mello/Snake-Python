from init import pygame, screen
from config import menu_dimensions, menu_font
from score_table.config import (
                    player_col_width,
                    player_col_height,
                    header_col_height,
                    title_bottom_margin,
                    title_top_margin,


                    back_button_x,
                    back_button_y,
                    back_button_width,
                    back_button_height,
                    back_button_text,
                    back_button_text_color,
                    back_button_bg_color,
                    back_button_border_color,

                    delete_scores_button_x,
                    delete_scores_button_y,
                    delete_scores_button_width,
                    delete_scores_button_height,
                    delete_scores_button_text,
                    delete_scores_button_text_color,
                    delete_scores_button_bg_color,
                    delete_scores_button_border_color,

                    title_text
                    )

old_a = None
old_b = None
old_obj = {}

def show_delete_scores_button():
    surface = menu_font.render(delete_scores_button_text, True, delete_scores_button_text_color)
    rect = surface.get_rect(center = (delete_scores_button_x+delete_scores_button_width/2,delete_scores_button_y+delete_scores_button_height/2))

    bg_rect = pygame.Rect((delete_scores_button_x,delete_scores_button_y,delete_scores_button_width,delete_scores_button_height))

    pygame.draw.rect(screen,delete_scores_button_bg_color,bg_rect)
    pygame.draw.rect(screen,delete_scores_button_border_color,bg_rect, 2)
    screen.blit(surface,rect)

def show_back_button():
    surface = menu_font.render(back_button_text, True, back_button_text_color)
    rect = surface.get_rect(center = (back_button_x+back_button_width/2,back_button_y+back_button_height/2))

    bg_rect = pygame.Rect((back_button_x,back_button_y,back_button_width,back_button_height))

    pygame.draw.rect(screen,back_button_bg_color,bg_rect)
    pygame.draw.rect(screen,back_button_border_color,bg_rect, 2)
    screen.blit(surface,rect)


def show_scores(obj,a,b):
    global old_a, old_b, old_obj
    if a == old_a and b == old_b and len(obj.keys()) == len(old_obj.keys()):
        return

    screen.fill((200,200,200))

    old_a = a
    old_b = b
    old_obj = obj

    show_back_button()
    show_delete_scores_button()

    nb_players = len(obj.keys())

    initial_x = menu_dimensions[0]/2-player_col_width*(nb_players/2)

    y = 0
    title_width,title_height = menu_font.size(title_text)
    title_surface = menu_font.render(title_text, True, (0,0,0))
    title_rect = title_surface.get_rect(center = (menu_dimensions[0]/2,title_height/2+title_top_margin))
    screen.blit(title_surface,title_rect)

    y += title_height+title_top_margin+title_bottom_margin
    x = initial_x
    for player_num in obj.keys():
        player_surface = menu_font.render(f"Joueur N°{player_num}", True, (0,0,0))
        player_rect = player_surface.get_rect(center = (x+player_col_width/2,y+header_col_height/2))

        player_bg_rect = pygame.Rect((x,y,player_col_width,header_col_height))

        pygame.draw.rect(screen,(200,200,200),player_bg_rect)
        pygame.draw.rect(screen,(0,0,0),player_bg_rect, 2)
        screen.blit(player_surface,player_rect)

        x += player_col_width

    y += header_col_height

    for i in range(a,b):
        x = initial_x
        num_text = str(i+1)
        num_width,num_height = menu_font.size(num_text)
        num_surface = menu_font.render(num_text, True, (0,0,0))
        num_rect = num_surface.get_rect(center = (x-10,y+player_col_height/2))
        screen.blit(num_surface,num_rect)
        for scores in obj.values():
            if i < len(scores):
                score_surface = menu_font.render(str(scores[i]), True, (0,0,0))
                score_rect = score_surface.get_rect(center = (x+player_col_width/2,y+player_col_height/2))

                score_bg_rect = pygame.Rect((x,y,player_col_width,player_col_height))

                pygame.draw.rect(screen,(200,200,200),score_bg_rect)
                pygame.draw.rect(screen,(0,0,0),score_bg_rect, 2)
                screen.blit(score_surface,score_rect)
            x += player_col_width
        y += player_col_height
    pygame.draw.line(screen, (0,0,0), (0,y),(menu_dimensions[0],y))

    pygame.display.update()

