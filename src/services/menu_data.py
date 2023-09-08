from models.ingredient import Ingredient
from models.dish import Dish
import csv
# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = MenuData.generate_dishes(source_path)

    def generate_dishes(source_path):
        with open(source_path, encoding="utf-8") as file:
            dishes = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = dishes
        list_dishes = []
        for row in data:
            price = row[1]
            menu = Dish(row[0], float(price))
            if menu not in list_dishes:
                food = Ingredient(row[2])
                menu.add_ingredient_dependency(food, int(row[3]))
                list_dishes.append(menu)
            else:
                index_menu = list_dishes.index(menu)
                new_menu = list_dishes[index_menu]
                food = Ingredient(row[2])
                new_menu.add_ingredient_dependency(food, int(row[3]))
                list_dishes[index_menu] = new_menu
        new_set = set(list_dishes)
        return new_set
