from config import (menu_dimensions,
                   menu_y_margin,
                   menu_x_margin,
                   menu_validate_button_margin,
                   menu_body_height,
                   menu_font,
                   menu_text_bottom_margin
                   )

from menu.buttons import buttons, validate_button, scores_button


def define_coordinates():
    global validate_button
    width = menu_dimensions[0]
    x = 40
    y = 40
    for (i,button) in enumerate(buttons): # calcul one time all coordinates, to re use them after
        text_width,text_height = menu_font.size(button["name"])

        if x > width-40-text_width:
            x = 40
            y += menu_body_height+menu_y_margin

        settable_value_width,settable_value_height = menu_font.size(max(button["get"](),"99"))
        settable_value_rect_center = (x+text_width/2, y+text_height+6+menu_text_bottom_margin+settable_value_height/2)
        settable_value_bg_rect_params = (settable_value_rect_center[0]-settable_value_width/2-3, settable_value_rect_center[1]-settable_value_height/2-3, settable_value_width+6, settable_value_height+6)
        global_bg_rect_params = (x-3, y-3 , max(text_width,settable_value_width)+6 , text_height+3+menu_body_height)
        text_bg_rect_params = (x-3, y-3 , max(text_width,settable_value_width)+6 , text_height+6)

        locals_ = locals()
        buttons[i] = {**button, **{k: locals_[k] for k in (
                                            "x",
                                            "y",
                                            "text_width",
                                            "text_height",
                                            "settable_value_width",
                                            "settable_value_height",
                                            "settable_value_rect_center",
                                            "settable_value_bg_rect_params",
                                            "global_bg_rect_params",
                                            "text_bg_rect_params"
                                            )
                              }
                  }

        if button["type"] == "integer":
            buttons_increment_and_decrement_x = settable_value_bg_rect_params[0]+settable_value_bg_rect_params[2]+10
            buttons_increment_and_decrement_height = settable_value_bg_rect_params[3]/2-5
            buttons_increment_and_decrement_width = menu_font.size(" v ")[0]

            button_increment_y = settable_value_bg_rect_params[1]
            button_decrement_y = settable_value_bg_rect_params[1]+settable_value_bg_rect_params[3]/2+5

            button_increment_rect_center = (buttons_increment_and_decrement_x+buttons_increment_and_decrement_width/2, button_increment_y+buttons_increment_and_decrement_height/2)
            button_decrement_rect_center = (buttons_increment_and_decrement_x+buttons_increment_and_decrement_width/2, button_decrement_y+buttons_increment_and_decrement_height/2)

            locals_ = locals()
            buttons[i] = {**buttons[i], **{k: locals_[k] for k in (
                                                "buttons_increment_and_decrement_x",
                                                "buttons_increment_and_decrement_height",
                                                "buttons_increment_and_decrement_width",
                                                "button_increment_y",
                                                "button_decrement_y",
                                                "button_increment_rect_center",
                                                "button_decrement_rect_center"
                                                )
                                   }
                     }
        x += text_width+menu_x_margin


    # Defines validate button coordinates
    validate_button_text_width, validate_button_text_height = menu_font.size(validate_button["name"])


    for button in buttons[::-1]:
        y_validate_button = button["y"]+button["global_bg_rect_params"][1]+menu_validate_button_margin
        if y_validate_button < menu_dimensions[1]:
            break

    x_validate_button = menu_dimensions[0]/2-validate_button_text_width/2

    validate_button_bg_rect_params = (x_validate_button-60,y_validate_button-20,validate_button_text_width+120, validate_button_text_height+40)

    for k in (
               "validate_button_text_width",
               "validate_button_text_height",
               "y_validate_button",
               "x_validate_button",
               "validate_button_bg_rect_params"
             ):
        validate_button[k] = locals()[k]


    # Defines button to scores coordinates
    validate_button_bg_rect_right = validate_button_bg_rect_params[0]+validate_button_bg_rect_params[2]

    scores_button_text_width,scores_button_text_height = menu_font.size(scores_button["name"])

    x_scores_button = validate_button_bg_rect_right+(menu_dimensions[0]-validate_button_bg_rect_right)/2-scores_button_text_width/2
    y_scores_button = y_validate_button

    scores_button_bg_rect_params = (x_scores_button-60,y_scores_button-20,scores_button_text_width+120,scores_button_text_height+40)

    for k in (
               "scores_button_text_width",
               "scores_button_text_height",
               "x_scores_button",
               "y_scores_button",
               "scores_button_bg_rect_params"
             ):
        scores_button[k] = locals()[k]
