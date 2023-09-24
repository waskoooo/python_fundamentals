days_per_year = 365.2422
hours_per_day = 24
minutes_per_hour = 60

centuries = int(input())
years = centuries * 100
days = int(years * days_per_year)
hours = days * hours_per_day
minutes = hours * minutes_per_hour

print(f"{int(centuries)} centuries = "
      f"{int(years)} years = "
      f"{int(days)} days = "
      f"{int(hours)} hours = "
      f"{int(minutes)} minutes")