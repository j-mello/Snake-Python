from config import menu_font
from menu.buttons import buttons, validate_button

def listen_buttons(mouse):
    for button in buttons:
        text_width,text_height = menu_font.size(button["name"])

        settable_value_bg_rect_params, settable_value_width, settable_value_height = [button[k] for k in ('settable_value_bg_rect_params','settable_value_width', 'settable_value_height')]

        x_area, y_area, width_area, height_area = settable_value_bg_rect_params

        if button["type"] == "boolean" and x_area <= mouse[0] <= x_area+width_area and y_area <= mouse[1] <= y_area+height_area:
            button["change"]()
        elif button["type"] == "integer":
            (
                x_area,
                y_increment_area,
                y_decrement_area,
                button_width_area,
                button_height_area
            ) = [button[k] for k in (
                                    "buttons_increment_and_decrement_x",
                                    "button_increment_y",
                                    "button_decrement_y",
                                    "buttons_increment_and_decrement_width",
                                    "buttons_increment_and_decrement_height"
                                   )]

            if x_area <= mouse[0] <= x_area+button_width_area:
                if y_increment_area-3 <= mouse[1] <= y_increment_area+button_height_area+3:
                    button["increment"]()
                elif y_decrement_area-3 <= mouse[1] <= y_decrement_area+button_height_area+3:
                    button["decrement"]()


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
    x_area, y_area, width_area, height_area = validate_button_bg_rect_params
    if x_area <= mouse[0] <= x_area+width_area and y_area <= mouse[1] <= y_area+height_area:
        validate_button["action"]()
