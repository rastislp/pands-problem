#Rastislav Petras
#12 Feb 2020
#Excercise 5 
#Write a program that outputs whether or not today is a weekday.
#  An example of running this program on a Thursday is given below.

print()
print("Welcome in day teller.")
print()

import datetime
import calendar

x = datetime.datetime.today()


year = x.strftime("%Y")
#print("year:", year)
month = x.strftime("%m")
#print("month:", month)
day = x.strftime("%d")
#print("day:", day)

year = int(year)
month  = int(month)
day = int(day)


z = calendar.weekday(year, month,day)
#print(z)

if (z < 5):
    print("Today",x ,"is a week day, unfortunately ;-(")
else:
    print("Today",x ,"is a weekend ;-)")

print()    


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

date1 = calendar.weekday(year, month, day)
date2 = datetime.date(year, month, day)
date3 = calendar.day_name[date1]

print("Day you have entered", date2, "is: ",date3)


