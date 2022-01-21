from config import config_game

from game import start_game

def increment_nb_random_walls(n):
    global config_game
    config_game["nb_random_walls"] = max(0,config_game["nb_random_walls"]+n)

def increment_nb_wormholes(n):
    #global config_game
    config_game["nb_wormholes"] = max(0,config_game["nb_wormholes"]+n)

def increment_periodically_shrink_grill(n):
    global config_game
    config_game["periodically_shrink_grill"] = max(0,config_game["periodically_shrink_grill"]+n)

def change_new_random_walls_at_each_new_fruit():
    global config_game
    config_game["new_random_walls_at_each_new_fruit"] = False if config_game["new_random_walls_at_each_new_fruit"] else True

def change_use_tonic_grills():
    global use_tonic_grills
    config_game["use_tonic_grills"] = False if config_game["use_tonic_grills"] else True

def change_use_super_fruit():
    global use_super_fruit
    config_game["use_super_fruit"] = False if config_game["use_super_fruit"] else True

def change_use_bad_fruit():
    global use_bad_fruit
    config_game["use_bad_fruit"] = False if config_game["use_bad_fruit"] else True

def change_use_ghost_fruit():
    global use_ghost_fruit
    config_game["use_ghost_fruit"] = False if config_game["use_ghost_fruit"] else True

def change_use_fire_fruit():
    global use_fire_fruit
    config_game["use_fire_fruit"] = False if config_game["use_fire_fruit"] else True

validate_button = {
    "name": "Valider",
    "action": start_game
}

buttons = [
    {
        "name": "Murs aléatoires",
        "type": "integer",
        "increment": lambda: increment_nb_random_walls(1),
        "decrement": lambda: increment_nb_random_walls(-1),
        "get": lambda: str(config_game["nb_random_walls"])
    },
    {
        "name": "Murs aléatoire à chaque nouveau fruit",
        "type": "boolean",
        "change": change_new_random_walls_at_each_new_fruit,
        "get": lambda: "Oui" if config_game["new_random_walls_at_each_new_fruit"] else "Non"
    },
    {
        "name": "Nombre de trous de ver",
        "type": "integer",
        "increment": lambda: increment_nb_wormholes(1),
        "decrement": lambda: increment_nb_wormholes(-1),
        "get": lambda: str(config_game["nb_wormholes"])
    },
    {
        "name": "Grilles toriques",
        "type": "boolean",
        "change": change_use_tonic_grills,
        "get": lambda: "Oui" if config_game["use_tonic_grills"] else "Non"
    },
    {
        "name": "Régulièrement rétrecir la grille de :  ",
        "type": "integer",
        "increment": lambda: increment_periodically_shrink_grill(1),
        "decrement": lambda: increment_periodically_shrink_grill(-1),
        "get": lambda: str(config_game["periodically_shrink_grill"])
    },
    {
        "name": "Super fruits",
        "type": "boolean",
        "change": change_use_super_fruit,
        "get": lambda: "Oui" if config_game["use_super_fruit"] else "Non"
    },
    {
        "name": "Mauvais fruits",
        "type": "boolean",
        "change": change_use_bad_fruit,
        "get": lambda: "Oui" if  config_game["use_bad_fruit"] else "Non"
    },
    {
        "name": "Fruits fantômes",
        "type": "boolean",
        "change": change_use_ghost_fruit,
        "get": lambda: "Oui" if  config_game["use_ghost_fruit"] else "Non"
    },
    {
        "name": "Fruits de feu",
        "type": "boolean",
        "change": change_use_fire_fruit,
        "get": lambda: "Oui" if  config_game["use_fire_fruit"] else "Non"
    }
]
