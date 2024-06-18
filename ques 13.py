# 13.Write a program that asks the user for their birth year and calculates their age.
from datetime import date
birth_year = int(input("enter your birth year: "))
current_year = date.today().year
age_year = current_year - birth_year
print("Your age is: ", age_year)

