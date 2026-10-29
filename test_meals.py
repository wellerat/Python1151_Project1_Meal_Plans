from meals import load_meals
from objects.weekplan import WeekPlan
from objects.dayplan import DayPlan
from objects.meal import Meal


def test_load_meals():
    meals = load_meals()

    assert "breakfast" in meals
    assert "lunch" in meals
    assert "dinner" in meals


def test_breakfast_contains_meals():
    meals = load_meals()

    assert len(meals["breakfast"]) > 0

def test_meal_creation():
    meal = Meal("Pancakes","breakfast")

    assert meal.name == "Pancakes"
    assert meal.meal_type == "breakfast"

def test_meal_describe():
    meal = Meal("Pancakes", "breakfast")

    assert meal.describe() == "Pancakes (breakfast)"

def test_day_plan_creation():
    breakfast = Meal("Pancakes","breakfast")
    lunch = Meal("Sandwich","lunch")
    dinner = Meal("Tacos","dinner")

    day = DayPlan(breakfast,lunch,dinner)

    assert day.breakfast.name == "Pancakes"
    assert day.lunch.name == "Sandwich"
    assert day.dinner.name == "Tacos"

def test_week_plan_add_day():

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