"""Meal Planner - Test Module

Description:
    Contains automated tests for meal loading,
    meal objects, day plans, and week plans.
    
Author:
    Ann Cooper
    
Starter Code:
    None

Date:
    October 2026
"""

from meals import load_meals
from objects.weekplan import WeekPlan
from objects.dayplan import DayPlan
from objects.meal import Meal


def test_load_meals():
    """Verify meal categories are loaded from teh JSON file."""
    meals = load_meals()

    assert "breakfast" in meals
    assert "lunch" in meals
    assert "dinner" in meals


def test_breakfast_contains_meals():
    """Verify the breakfast category contains meal data"""
    meals = load_meals()

    assert len(meals["breakfast"]) > 0

def test_meal_creation():
    """Verify a Meal object is created correctly"""
    meal = Meal("Pancakes","breakfast")

    assert meal.name == "Pancakes"
    assert meal.meal_type == "breakfast"

def test_meal_describe():
    """Verify Meal.describe() returns the correct string."""
    meal = Meal("Pancakes", "breakfast")

    assert meal.describe() == "Pancakes (breakfast)"

def test_day_plan_creation():
    """Verify a DayPlan stores breakfast, lunch, and dinner meals."""
    breakfast = Meal("Pancakes","breakfast")
    lunch = Meal("Sandwich","lunch")
    dinner = Meal("Tacos","dinner")

    day = DayPlan(breakfast,lunch,dinner)

    assert day.breakfast.name == "Pancakes"
    assert day.lunch.name == "Sandwich"
    assert day.dinner.name == "Tacos"

def test_week_plan_add_day():
    """Verify a DayPlan can be added to a WeekPlan"""
    week = WeekPlan()

    breakfast = Meal("Pancakes","breakfast")
    lunch = Meal("Sandwich","lunch")
    dinner = Meal("Tacos","dinner")

    day = DayPlan (
        breakfast,
        lunch,
        dinner
    )

    week.add_day(day)

    assert len(week.days) == 1