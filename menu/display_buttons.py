from init import pygame, screen
from config import (menu_dimensions,
                   menu_y_margin,
                   menu_x_margin,
                   menu_validate_button_y,
                   menu_body_height,
                   menu_font,
                   settable_values_menu_font,
                   menu_text_bottom_margin)
from menu.buttons import buttons, validate_button

def display_buttons(): # update screen only if a value has changed
    if all("old_value" in button and button["get"]() == button["old_value"] for button in buttons):
        return



    screen.fill((200,200,200))
    for button in buttons:
        text = button["name"]
        text_width,text_height,x,y = [button[k] for k in ("text_width", "text_height", "x", "y")]

        surface = menu_font.render(text, True, (0,0,0))
        rect = surface.get_rect(center = (x+text_width/2, y+text_height/2))

        settable_value_text = button["get"]()
        button["old_value"] = settable_value_text

        settable_value_width, settable_value_height = [button[k] for k in ("settable_value_width", "settable_value_height")]
        settable_value_surface = settable_values_menu_font.render(settable_value_text, True, (0,0,0))
        settable_value_rect_center = button["settable_value_rect_center"]
        settable_value_rect = settable_value_surface.get_rect(center = settable_value_rect_center)

        settable_value_bg_rect_params, global_bg_rect_params, text_bg_rect_params = [button[k] for k in ("settable_value_bg_rect_params", "global_bg_rect_params", "text_bg_rect_params")]
        settable_value_bg_rect = pygame.Rect(*settable_value_bg_rect_params)
        global_bg_rect = pygame.Rect(*global_bg_rect_params)
        text_bg_rect = pygame.Rect(*text_bg_rect_params)

        if button['type'] == "integer":

            (buttons_increment_and_decrement_x, buttons_increment_and_decrement_height, buttons_increment_and_decrement_width,
            button_increment_y, button_decrement_y, button_increment_rect_center, button_decrement_rect_center
            ) = [button[k] for k in ("buttons_increment_and_decrement_x",
                                     "buttons_increment_and_decrement_height",
                                     "buttons_increment_and_decrement_width",
                                     "button_increment_y",
                                     "button_decrement_y",
                                     "button_increment_rect_center",
                                     "button_decrement_rect_center")]

            button_increment_surface = menu_font.render(" V ", True, (0,0,0))
            button_increment_surface = pygame.transform.flip(button_increment_surface, True, True)
            button_increment_rect = button_increment_surface.get_rect(center = button_increment_rect_center)

            button_decrement_surface = menu_font.render(" V ", True, (0,0,0))
            button_decrement_rect = button_increment_surface.get_rect(center = button_decrement_rect_center)

            screen.blit(button_increment_surface,button_increment_rect)
            pygame.draw.rect(screen, (0,0,0), button_increment_rect, 1)

            screen.blit(button_decrement_surface,button_decrement_rect)
            pygame.draw.rect(screen, (0,0,0), button_decrement_rect, 1)



        pygame.draw.rect(screen,(0,0,0),global_bg_rect, 2)
        pygame.draw.rect(screen,(0,0,0),text_bg_rect, 2)
        pygame.draw.rect(screen,(255,255,255),settable_value_bg_rect)
        pygame.draw.rect(screen,(0,0,0),settable_value_bg_rect, 1)
        screen.blit(surface,rect)
        screen.blit(settable_value_surface,settable_value_rect)

    (
        name,
        validate_button_text_width,
        validate_button_text_height,
        y_validate_button,
        x_validate_button,
        validate_button_bg_rect_params
    ) = [validate_button[k] for k in (
                                        "name",
                                        "validate_button_text_width",
                                        "validate_button_text_height",
                                        "y_validate_button",
                                        "x_validate_button",
                                        "validate_button_bg_rect_params"
                                     )]

    validate_button_surface = settable_values_menu_font.render(name,True,(255,255,255))
    validate_button_rect = validate_button_surface.get_rect(center = (x_validate_button+validate_button_text_width/2, y_validate_button+validate_button_text_height/2))

    validate_button_bg_rect = pygame.Rect(*validate_button_bg_rect_params)

    pygame.draw.rect(screen,(0,0,0),validate_button_bg_rect)
    pygame.draw.rect(screen,(255,255,255),validate_button_bg_rect, 1)
    screen.blit(validate_button_surface,validate_button_rect)

    pygame.display.update()
