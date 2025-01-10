from datetime import date, timedelta

def get_previous_week_range(weeks: int):
    current_week = 1
    total_weeks = current_week + weeks
    previous_date = date.today() - timedelta(days=7*total_weeks)
    print(previous_date)
    result = previous_date.isocalendar()
    print(result.year, result.week)


get_previous_week_range(1)
get_previous_week_range(2)
get_previous_week_range(52)