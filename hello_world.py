# import date module
from datetime import date

# get name from user
name = input("enter your name: ")

# get role from user
role = input("enter your internship role: ")

# store today's date
today_date = date.today()

# print name
print("name:", name)

# print role
print("internship role:", role)

# print date
print("today's date:", today_date)
