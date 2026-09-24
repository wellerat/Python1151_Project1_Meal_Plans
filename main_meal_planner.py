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
from print_meals import print_meals
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

    print_meals(num_of_days,start_day,days)
    
main()