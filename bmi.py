# week 2 
#28/1/2020 10:39
# Rastislav Petras
# program to calculate bmi

print() # print blank line
print("Welcome in your personal bmi calculator.")  # stdout string
print()  # print blank line

height = float(input ("Please enter your hight: "))  #assign heigth upon promt as a float
weight = float(input ("Please enter your weight: "))  #assign weight upon promt as a float

bmi=weight/(height*height)  # perform calculation.
print("Calculated bmi is",bmi,".")  # print out string along with bmi value.
print() # print blank line