class Meal:
    """Represent a single meal option"""
    def __init__(self, name, meal_type):
        self.name = name
        self.meal_type = meal_type

    def describe(self):
        """Return the meal's name and meal type"""
        return f"{self.name} ({self.meal_type})"

class FavoriteMeal(Meal):
    pass    