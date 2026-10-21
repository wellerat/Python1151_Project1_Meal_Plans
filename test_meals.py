from meals import load_meals

def test_load_meals():
    meals = load_meals()

    assert "breakfast" in meals
    assert "lunch" in meals
    assert "dinner" in meals

def test_breakfast_contains_meals():
    meals = load_meals()

    assert len(meals["breakfast"]) > 0
