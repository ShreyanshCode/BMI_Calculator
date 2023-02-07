age = input("What is your current age?")
age_as_int = int(age)
remaining_age = 90-age_as_int
days = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left")
