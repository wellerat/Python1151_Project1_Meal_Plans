class Meal:
    """Represent a single meal option"""
    def __init__(self, name, meal_type):
        """Initialize a meal wiht a name and category"""
        self.name = name
        self.meal_type = meal_type

    def describe(self):
        """Return the meal's name and meal type"""
        return f"{self.name} ({self.meal_type})"

class FavoriteMeal(Meal):
    """Represent a favorite meal selected by the user - future project"""
    pass    