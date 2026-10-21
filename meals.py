import json

def load_meals():
    with open("meals.json", "r") as file:
        return json.load(file)
    
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

        print(f"\n{meal_description} has been added.")

    print("\nAdding new meals complete.")   


