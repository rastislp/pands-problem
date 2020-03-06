# Rastislav Petras
# 06 March 2020
# Excercise 6 
# Write a program that takes a positive floating-point number as input and outputs
#  an approximation of its square root. You should create a function called sqrt that does this.

print()
print("This is a function for square root of inputed number")
print()

import math

def calculation(k):
  if(k==k ):
    result = (math.sqrt(k))
    print("Square root of number ", x ,"is ","%.1f" % round(result,1), ".")
  return result


x = float(input ("Please enter a positive number : "))
calculation(x)