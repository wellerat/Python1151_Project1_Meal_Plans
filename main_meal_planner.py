"""
Meal Planner - Project 1

Description
    This program will print out a set of meals for the amount
    of days you would like the plan to run.

Author:
    Ann Cooper

Starter code:
    None

Date:
    Sept. 21, 2026
"""
from meals import meals, add_additional_meals
import random

days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
def main():

    print("\n----     Meal Planner     ----")
    add_meals = input('\nWould you like to add meals to the current options? (Y/N)   ')

    while (add_meals != 'Y') and (add_meals != 'N'):
        print('\nInvalid response please pick "N" or "Y"')
        add_meals = input('\nWould you like to add meals to the current options? (Y/N)   ')

    if add_meals == 'Y':
        add_additional_meals()

    num_of_days = int(input("\nMeal planning for how many days (1-7)?   "))
    start_day = input("\nStarting on what day? (ex. Monday)   ")

    

    start_day_index = days.index(start_day)

    plan_days = []

    for i in range(num_of_days):
        day = days[(start_day_index + i)%7]
        plan_days.append(day)

    for i in range(num_of_days):
        breakfast = random.choice(meals["breakfast"])
        lunch = random.choice(meals["lunch"])
        dinner = random.choice(meals["dinner"])

        print(f"\n",plan_days[i])
        print("Breakfast:", breakfast)
        print("Lunch:", lunch)
        print("Dinner:", dinner)

main()