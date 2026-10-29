class DayPlan:
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

    def to_dict(self):
        return {
            "breakfast": self.breakfast.describe(),
            "lunch": self.lunch.decribe,
            "dinner": self.dinner.describe()
        }