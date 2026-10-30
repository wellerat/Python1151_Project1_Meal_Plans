"""
Meal Planner - Day Plan Module

Description:
    This module contains the DayPlan class which stores 
    breakfast, lunch, and dinner meals for a single day.
    
Author:
    Ann Cooper
    
Starter Code:
    None
    
Date:
    October 2026
"""
class DayPlan:
    """Stores breakfast, lunch, and dinner meals for one day"""
    def __init__(self, breakfast, lunch, dinner):
        """Initialize a daily meal plan."""
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

    def to_dict(self):
        """Convert the DayPlan Object to a dictionary"""
        return {
            "breakfast": self.breakfast.describe(),
            "lunch": self.lunch.describe(),
            "dinner": self.dinner.describe()
        }