from score_table.config import (
                    back_button_x,
                    back_button_y,
                    back_button_width,
                    back_button_height,

                    delete_scores_button_x,
                    delete_scores_button_y,
                    delete_scores_button_width,
                    delete_scores_button_height
                    )
from menu.menu import menu

def listen_back_button(mouse):
    if back_button_x <= mouse[0] <= back_button_x+back_button_width and back_button_y <= mouse[1] <= back_button_y+back_button_height:
        menu()


def listen_delete_scores_button(mouse):
    if delete_scores_button_x <= mouse[0] <= delete_scores_button_x+delete_scores_button_width and delete_scores_button_y <= mouse[1] <= delete_scores_button_y+delete_scores_button_height:
        with open("scores.json", "w") as file:
            file.write("{}")
        return True
    return True
