#Rastislav Petras
#12 Feb 2020
#Excercise 5 
#Write a program that outputs whether or not today is a weekday.
#  An example of running this program on a Thursday is given below.

print()
print("Welcome in day teller.")
print()

import datetime
x = datetime.datetime.now()
print(x)


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date1 = datetime.date(year, month, day)

print(date1)