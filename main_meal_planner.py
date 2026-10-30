"""
Meal Planner - Project 2

Description
    Main program file for the Meal Planner Application.
    This program allows users to view meals, add meals, delete meals, 
    and generate meal plans fr 1-7 days.

Author:
    Ann Cooper

Starter code:
    None

Date:
    October 2026
"""
from meals import (
    meals, 
    add_additional_meals, 
    display_meals, 
    delete_meal)
from print_meals import print_meals

import random

# Valid says used for meal plan generation
days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def get_days():
    """Ask the user for number of days (1-7) to plan meals"""
    while True:
        value = input("\nMeal planning for how many days (1-7)?   ")

        try:
            num_days = int(value)
        except ValueError:
            print("Invalid input.  Please enter a whole number.")
            continue

        if 1 <= num_days <= 7:
            return num_days
        else:
            print("Value out of range. Please enter a number between 1 and 7.")


def get_start_day():
    """Prompts the user for a starting day of the week"""
    while True:
        value = input(f"\nStarting on what day? (ex. Monday):  ")     

        value = value.capitalize()

        if value in days:
            return value
        else:
            print(f"Invalid entry.  Please choose one of {days}")

def display_menu():
    """Display the main menu and return the user's choice"""

    print("\nMeal Planner Options")
    print("----------------------") 
    print("1. Generate Meal Plan")
    print("2. View Meal Options")
    print("3. Add Meals") 
    print("4. Delete Meals")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5):  ")

    return choice              


def main():
    """Run the Meal Planner application.
       Displays the main menu and routes user selections
       to the appropriate program functionality
    """

    print("\n\n               ----     Meal Planner    ----")
    print('\n\nThis program will create a meal plan for up to a week.')
    print('The plan will include a breakfast, lunch, and dinner option.')
    while True:

        choice = display_menu()

        if choice == '1':
            num_of_days = get_days()
            start_day = get_start_day()

            print_meals(
                num_of_days, start_day, days
            )

        elif choice =="2":
            display_meals()

        elif choice == "3":
            add_additional_meals()

        elif choice == "4":
            delete_meal()

        elif choice =="5":
            print("\nThank you for using Meal Planner.")
            break
        else:
            print("Please enter a valid option")    


main()