from meals import meals
import random

def print_meals(num_of_days,start_day,days):
    start_day_index = days.index(start_day)
    
    plan_days = []

    for i in range(num_of_days):
            day = days[(start_day_index + i)%7]
            plan_days.append(day)
    
    
    print("\n----     MEAL PLAN      ----")
    
    for i in range(num_of_days):
        breakfast = random.choice(meals["breakfast"])
        lunch = random.choice(meals["lunch"])
        dinner = random.choice(meals["dinner"])
    
        print(f"\n",plan_days[i])
        print("-----------")
        print("Breakfast:", breakfast)
        print("Lunch:", lunch)
        print("Dinner:", dinner)
    