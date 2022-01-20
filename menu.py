from init import pygame, screen, SCREEN_UPDATE
from config import (menu_dimensions,
                   menu_y_margin,
                   menu_x_margin,
                   menu_body_height,
                   menu_font,
                   settable_values_menu_font,
                   menu_text_bottom_margin,

                   nb_random_walls,
                   new_random_walls_at_each_new_fruit,
                   nb_wormholes,
                   use_tonic_grills,
                   periodically_shrink_grill,
                   use_super_fruit,
                   use_bad_fruit,
                   use_ghost_fruit,
                   use_fire_fruit)

buttons = [
    {
        "name": "Murs aléatoires",
        "type": "integer",
        "action": lambda: print("coucou"),
        "get": lambda: str(nb_random_walls)
    },
    {
        "name": "Murs aléatoire à chaque nouveau fruit",
        "type": "boolean",
        "action": lambda: print("coucou"),
        "get": lambda: "Oui" if new_random_walls_at_each_new_fruit else "Non"
    },
    {
        "name": "Nombre de trous de ver",
        "type": "integer",
        "action": lambda: print("coucou"),
        "get": lambda: str(nb_wormholes)
    },
    {
        "name": "Grilles toriques",
        "type": "boolean",
        "action": lambda: print("coucou"),
        "get": lambda: "Oui" if use_tonic_grills else "Non"
    },
    {
        "name": "Régulièrement rétrecir la grille de :  ",
        "type": "integer",
        "action": lambda: print("coucou"),
        "get": lambda: str(periodically_shrink_grill)
    },
    {
        "name": "Super fruits",
        "type": "boolean",
        "action": lambda: print("coucou"),
        "get": lambda: "Oui" if use_super_fruit else "Non"
    },
    {
        "name": "Mauvais fruits",
        "type": "boolean",
        "action": lambda: print("coucou"),
        "get": lambda: "Oui" if  use_bad_fruit else "Non"
    },
    {
        "name": "Fruits fantômes",
        "type": "boolean",
        "action": lambda: print("coucou"),
        "get": lambda: "Oui" if  use_ghost_fruit else "Non"
    },
    {
        "name": "Fruits de feu",
        "type": "boolean",
        "action": lambda: print("coucou"),
        "get": lambda: "Oui" if  use_fire_fruit else "Non"
    }
]

def menu():
    screen = pygame.display.set_mode(menu_dimensions)
    width = menu_dimensions[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print(mouse)
                x = 40
                y = 40
                for button in buttons:
                    text_width,text_height = menu_font.size(button["name"])

                    if x > width-40-text_width:
                        x = 40
                        y += menu_body_height+menu_y_margin

                    settable_value_width,settable_value_height = settable_values_menu_font.size(button["get"]())
                    x_area = x+text_width/2-min(settable_value_width,text_width/2-settable_value_width/2-3)-settable_value_width/2
                    y_area = y+text_height+6+menu_text_bottom_margin-3
                    width_area = settable_value_width+6
                    height_area = settable_value_height+6
                    #if x_area <= mouse[0] <= x_area+width_area:
                    #    print("x_area clicked '"+button['name']+"'")
                    #if y_area <= mouse[1] <= y_area+height_area:
                    #    print("y_area clicked '"+button['name']+"'")
                    #if button["name"] == "Murs aléatoires":
                    #if button["name"] == "Murs aléatoire à chaque nouveau fruit":
                    #    print(f"x: {x_area}, x2: {x_area+width_area}")
                    #    print(mouse)
                    if x_area <= mouse[0] <= x_area+width_area and y_area <= mouse[1] <= y_area+height_area:
                        print("button '"+button["name"]+"' clicked")

                    x += text_width+menu_x_margin
            if event.type == SCREEN_UPDATE:
                screen.fill((200,200,200))
                x = 40
                y = 40
                for button in buttons:
                    text = button["name"]
                    text_width,text_height = menu_font.size(text)

                    if x > width-40-text_width:
                        x = 40
                        y += menu_body_height+menu_y_margin

                    surface = menu_font.render(text, True, (0,0,0))
                    rect = surface.get_rect(center = (x+text_width/2, y+text_height/2))

                    settable_value_text = button["get"]()
                    settable_value_width,settable_value_height = settable_values_menu_font.size(settable_value_text)
                    settable_value_surface = settable_values_menu_font.render(settable_value_text, True, (0,0,0))
                    settable_value_rect_center = (x+text_width/2-min(settable_value_width,text_width/2-settable_value_width/2-3), y+text_height+6+menu_text_bottom_margin+settable_value_height/2)
                    settable_value_rect = settable_value_surface.get_rect(center = settable_value_rect_center)

                    settable_value_bg_rect = pygame.Rect(settable_value_rect_center[0]-settable_value_width/2-3, settable_value_rect_center[1]-settable_value_height/2-3, settable_value_width+6, settable_value_height+6)
                    global_bg_rect = pygame.Rect(x-3, y-3 , max(text_width,settable_value_width)+6 , text_height+3+menu_body_height)
                    text_bg_rect = pygame.Rect(x-3, y-3 , max(text_width,settable_value_width)+6 , text_height+6)

                    pygame.draw.rect(screen,(0,0,0),global_bg_rect, 2)
                    pygame.draw.rect(screen,(0,0,0),text_bg_rect, 2)
                    pygame.draw.rect(screen,(255,255,255),settable_value_bg_rect)
                    pygame.draw.rect(screen,(0,0,0),settable_value_bg_rect, 1)
                    screen.blit(surface,rect)
                    screen.blit(settable_value_surface,settable_value_rect)

                    x += text_width+menu_x_margin

                pygame.display.update()

            mouse = pygame.mouse.get_pos()
