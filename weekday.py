#Rastislav Petras
#12 Feb 2020
#Excercise 5 
#Write a program that outputs whether or not today is a weekday.
#  An example of running this program on a Thursday is given below.

print()
print("Welcome in day teller.")
print()

import datetime      #import librarys with time functions.
import calendar      #import librarys with calendar functions.   

x = datetime.datetime.today()  #assign today current time


year = x.strftime("%Y")  # extract year from x 
#print("year:", year)
month = x.strftime("%m")  # extract month from x
#print("month:", month)
day = x.strftime("%d")  # extract day from x
#print("day:", day)

year = int(year)   #converts string into integer
month  = int(month)  #converts string into integer
day = int(day)   #converts string into integer


z = calendar.weekday(year, month,day)   # wwekday function calculates week day (1-7) based on date entered
#print(z)

if (z < 6):    #conditional statement if weekday is betwen 1-5
    print("Today",x ,"is a week day, unfortunately ;-(")
else:       #conditional statement if weekday is betwen 6 and 7
    print("Today",x ,"is a weekend ;-)")

print()    #empty blank lne

#bonus


year = int(input('Enter a year: '))     #input integer as follow: year month day
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

date1 = calendar.weekday(year, month, day)   # week day number is assigned to variable date1 not used in this case
date2 = datetime.date(year, month, day)    # fulll date is assigned to variable date2
date3 = calendar.day_name[date1]    # week day name is assigned to variable date3

print("Day you have entered", date2, "is: ",date3) # print out full date and week date name.


