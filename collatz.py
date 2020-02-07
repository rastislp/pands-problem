# Rastislav Petras
# 07 feb 2020
# excercise 4 Write a program that asks the user to input any positive
#  integer and outputs the successive values of the following calculation.
#  At each step calculate the next value by taking the current value and
#  if it is even, divide it by two, but if it is odd, multiply it by three
#  and add one. Have the program end if the current value is one.

number= int(input ("Please choose your posiive number:  "))


if (number % 2) == 0 and number>0: #if number modelo 2 = 0 and greater than 0
    x=number/2
    print(x)
elif(number %2) ==1 and number>0: #if number modelo 2 = 1 and greater than 0
    x= (number*3) +1
    print(x)
else:
    number <0
    print("This is not positive number")     