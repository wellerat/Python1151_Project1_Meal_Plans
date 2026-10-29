class Meal:
    def __init__(self, name, meal_type):
        self.name = name
        self.meal_type = meal_type

    def describe(self):
        return f"{self.name} ({self.meal_type})"

class FavoriteMeal(Meal):
    pass    