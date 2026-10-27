from meals import load_meals
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