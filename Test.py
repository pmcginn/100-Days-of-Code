age = int(input("How old are you? "))
weeks = age * 52
days = age * 365
months = age * 12
age_at_death = 90
print(f"You will die in {(age_at_death * 365) - days} days, {(age_at_death * 52) - weeks} weeks, and {(age_at_death * 12) - months} months.")