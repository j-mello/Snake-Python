from score_table.config import (
                    back_button_x,
                    back_button_y,
                    back_button_width,
                    back_button_height
                    )
from menu.menu import menu

def listen_back_button(mouse):
    if back_button_x <= mouse[0] <= back_button_x+back_button_width and back_button_y <= mouse[1] <= back_button_y+back_button_height:
        menu()
