class WeekPlan:
    """Store all generated day plans."""

    def __init__(self):
        self.days = []

    def add_day(self, day_plan):
        self.days.append(day_plan)