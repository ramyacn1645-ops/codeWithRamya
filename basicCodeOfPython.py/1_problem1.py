from datetime import date
Name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
today_date = date.today()
current_year =today_date.year
age = current_year - birth_year
if age > 60:
    print("You are a senior citizen.")
else:
    print("You are not a senior citizen.")