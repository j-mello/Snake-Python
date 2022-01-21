from config import (
                   nb_random_walls,
                   new_random_walls_at_each_new_fruit,
                   nb_wormholes,
                   use_tonic_grills,
                   periodically_shrink_grill,
                   use_super_fruit,
                   use_bad_fruit,
                   use_ghost_fruit,
                   use_fire_fruit)

def increment_nb_random_walls(n):
    global nb_random_walls
    nb_random_walls = max(0,nb_random_walls+n)

def increment_nb_wormholes(n):
    global nb_wormholes
    nb_wormholes = max(0,nb_wormholes+n)

def increment_periodically_shrink_grill(n):
    global periodically_shrink_grill
    periodically_shrink_grill = max(0,periodically_shrink_grill+n)

def change_new_random_walls_at_each_new_fruit():
    global new_random_walls_at_each_new_fruit
    new_random_walls_at_each_new_fruit = False if new_random_walls_at_each_new_fruit else True

def change_use_tonic_grills():
    global use_tonic_grills
    use_tonic_grills = False if use_tonic_grills else True

def change_use_super_fruit():
    global use_super_fruit
    use_super_fruit = False if use_super_fruit else True

def change_use_bad_fruit():
    global use_bad_fruit
    use_bad_fruit = False if use_bad_fruit else True

def change_use_ghost_fruit():
    global use_ghost_fruit
    use_ghost_fruit = False if use_ghost_fruit else True

def change_use_fire_fruit():
    global use_fire_fruit
    use_fire_fruit = False if use_fire_fruit else True

validate_button = {
    "name": "Valider",
    "action": lambda: print("Validate")
}

buttons = [
    {
        "name": "Murs aléatoires",
        "type": "integer",
        "increment": lambda: increment_nb_random_walls(1),
        "decrement": lambda: increment_nb_random_walls(-1),
        "get": lambda: str(nb_random_walls)
    },
    {
        "name": "Murs aléatoire à chaque nouveau fruit",
        "type": "boolean",
        "change": change_new_random_walls_at_each_new_fruit,
        "get": lambda: "Oui" if new_random_walls_at_each_new_fruit else "Non"
    },
    {
        "name": "Nombre de trous de ver",
        "type": "integer",
        "increment": lambda: increment_nb_wormholes(1),
        "decrement": lambda: increment_nb_wormholes(-1),
        "get": lambda: str(nb_wormholes)
    },
    {
        "name": "Grilles toriques",
        "type": "boolean",
        "change": change_use_tonic_grills,
        "get": lambda: "Oui" if use_tonic_grills else "Non"
    },
    {
        "name": "Régulièrement rétrecir la grille de :  ",
        "type": "integer",
        "increment": lambda: increment_periodically_shrink_grill(1),
        "decrement": lambda: increment_periodically_shrink_grill(-1),
        "get": lambda: str(periodically_shrink_grill)
    },
    {
        "name": "Super fruits",
        "type": "boolean",
        "change": change_use_super_fruit,
        "get": lambda: "Oui" if use_super_fruit else "Non"
    },
    {
        "name": "Mauvais fruits",
        "type": "boolean",
        "change": change_use_bad_fruit,
        "get": lambda: "Oui" if  use_bad_fruit else "Non"
    },
    {
        "name": "Fruits fantômes",
        "type": "boolean",
        "change": change_use_ghost_fruit,
        "get": lambda: "Oui" if  use_ghost_fruit else "Non"
    },
    {
        "name": "Fruits de feu",
        "type": "boolean",
        "change": change_use_fire_fruit,
        "get": lambda: "Oui" if  use_fire_fruit else "Non"
    }
]
