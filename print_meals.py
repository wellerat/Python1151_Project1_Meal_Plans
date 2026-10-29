from meals import meals
from objects.weekplan import WeekPlan
from objects.dayplan import DayPlan
from objects.meal import Meal
import random

def print_meals(num_of_days,start_day,days):
    """ Print a meal plan starting on the giving day and the correct number of days"""
    start_day_index = days.index(start_day)
    
    plan_days = []
    week_plan = WeekPlan()

    for i in range(num_of_days):
            day = days[(start_day_index + i)%7]
            plan_days.append(day)
    
    
    print("\n----     MEAL PLAN      ----")
    
    for i in range(num_of_days):
        breakfast = Meal(random.choice(meals["breakfast"]),"breakfast")
        lunch = Meal(random.choice(meals["lunch"]),"lunch")
        dinner = Meal(random.choice(meals["dinner"]),"dinner")
        day_plan = DayPlan(breakfast,lunch,dinner)
        week_plan.add_day(day_plan)
    
        print(f"\n",plan_days[i])
        print("-----------")
        print("Breakfast:",breakfast.name)
        print("Lunch:", lunch.name)
        print("Dinner:", dinner.name)
    