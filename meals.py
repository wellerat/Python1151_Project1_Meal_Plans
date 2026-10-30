import json

def load_meals():
    try:
        with open("meals.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Meal file not found.")
        return {
            "breakfast":[],
            "lunch":[],
            "dinner":[]
            }
    except json.JSONDecodeError:
        print("Meal file contains invalid JSON")
        return {
            "breakfast":[],
            "lunch":[],
            "dinner":[]
        }

def save_meals(meals):
    with open("meals.json", "w") as file:
        json.dump(meals, file, indent=4)    
    
meals = load_meals()

def add_additional_meals():
    """Add additional meals to breakfast, lunch or dinner until user quits"""

    meal_option = '';

    while meal_option != "Q":
        print("\nWhat meal category do you want to add? ")
        print("\nBreakfast (B), Lunch (L), Dinner (D), or Quit (Q)")
        meal_option = input("\nEnter your option: B, L, D, or Q:   ").upper()

        while meal_option not in ('B','L','D','Q'):
            print("Please enter B, L, D or Q")
            meal_option = input("\nEnter your option: B, L, D, or Q:   ").upper()

        if meal_option == "Q":
            break

        meal_description = input("\nEnter additional meal:  ")

        if meal_option == 'B':   
            meals["breakfast"].append(meal_description)
        elif meal_option == 'L':
            meals["lunch"].append(meal_description)
        elif meal_option == 'D':
            meals["dinner"].append(meal_description)

        save_meals(meals)   

        print(f"\n{meal_description} has been added.")

    print("\nAdding new meals complete.")   

def display_meals():
    """Display meals from a selected category."""

    print("\nWhich meal category would you like to view:")
    print("Breakfast (B)")
    print("Lunch (L)")
    print("Dinner (D)")

    category = input("\nEnter B, L, or D:  ").upper()

    while category not in ("B","L","D"):
        print("Please enter B, L, or D.")
        category = input("\nEnter B, L, or D:  ").upper()

    if category == "B":
        print("\nBreakfast Meals")
        print('-----------------')
        for meal in meals["breakfast"]:
            print(meal)

    elif category == "L":
        print("\nLunch Meals")
        print('-----------------')
        for meal in meals["lunch"]:
            print(meal)
        
    else: 
        print("\nDinner Meals")
        print('-----------------')
        for meal in meals["dinner"]:
            print(meal)

def delete_meal():
    """Remove a meal from selected category."""

    print("\nWhich category would you like to delete from?")
    print("Breakfast (B)")
    print("Lunch (L)")
    print("Dinner (D)")

    category = input("\nEnter B, L, or D:  ").upper()
    
    while category not in ("B","L","D"):
        print("Please enter B, L, or D.")
        category = input("\nEnter B, L, or D:  ").upper()

    if category =="B":
        category_name = "breakfast"
    elif category == "L":
        category_name = "lunch"
    else:
        category_name = "dinner"

    print(f"\n{category_name.capitalize()} Meals")
    print("-------------------------")

    for index, meal in enumerate(meals[category_name], start=1):
        print(f"{index}.{meal}")

    while True:
        try:
            choice = int(input("\nEnter meal number ot delete:  "))   

            if 1 <= choice <= len(meals[category_name]):
                break

            print("Please select a valid meal number.")

        except ValueError:
            print("Please enter a whole number.")
            
    deleted_meal = meals[category_name].pop(choice - 1)     

    save_meals(meals)

    print(f"\n{deleted_meal} has been removed.")
        
    