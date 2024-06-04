spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [n.get("name") for n in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [n for n in spicy_foods if n.get("heat_level")>5]
    pass


def print_spicy_foods(spicy_foods):
    print (("\n").join([f'{n.get("name")} ({n.get("cuisine")}) | Heat Level: {"🌶"*n.get("heat_level")}' for n in spicy_foods]))

    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [n for n in spicy_foods if n.get("cuisine")==cuisine][0]
    pass

def print_spiciest_foods(spicy_foods):
    print (("\n").join([f'{n.get("name")} ({n.get("cuisine")}) | Heat Level: {"🌶"*n.get("heat_level")}' for n in spicy_foods if n.get("heat_level")>5]))
    pass

def get_average_heat_level(spicy_foods):
    heat_levels_sum = sum([n.get("heat_level") for n in spicy_foods]) 
    return heat_levels_sum/len(spicy_foods)
    

    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass