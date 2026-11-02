"""
Meal Planner - Weel Plan Module

Description:
    This module contains the WeekPlan class which stores 
    multiple DayPlan objects that make up a meal plan.
    
Author:
    Ann Cooper
    
Starter Code:
    None
    
Date:
    October 2026
"""
class WeekPlan:
    """Store a collection of Dayplan objects"""
    def __init__(self):
        """Initialize an empty weekly meal plan."""
        self.days = []

    def add_day(self, day_plan):
        """Add a DayPlan object to the weekly meal plan."""
        self.days.append(day_plan)