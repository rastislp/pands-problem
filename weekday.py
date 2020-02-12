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

x = datetime.datetime.now()
print(x)


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

date1 = calendar.weekday(year, month, day)
date2 = datetime.date(year, month, day)
date3 = calendar.day_name[date1]

print("Day you have entered", date2, "is: ",date1)

#if (date1 % 7) ==0 :
#    print("Monday")
#elif (date1 %7 ) ==1 :
#    print("Tuesday")
#else:
#    print("W-S")

