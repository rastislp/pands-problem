# Rastislav Petras
# 06 March 2020
# Excercise 6 
# Write a program that takes a positive floating-point number as input and outputs
#  an approximation of its square root. You should create a function called sqrt that does this.

print()
print("This is a function for square root of inputed number")
print()


import decimal      # module provides support for fast correctly-rounded decimal floating point arithmetic. It offers several advantages over the float datatype:

 
def sqrt(n):    
    assert n > 0     # chck for positive number
    with decimal.localcontext() as ctx:   
        ctx.prec += 2         # increase precision to minimize round off error
        x, prior = decimal.Decimal(n), None
        while x != prior: 
            prior = x
            x = (x + n/x) / 2 # quadratic convergence 
    return +x # round in a global context


decimal.getcontext().prec = 80 # desirable precision

z = input ("Please enter a positive number : ")  #Promts user to enter number and store as z 
z = decimal.Decimal(z)  #function that change iputet value into floating-point model 
result= sqrt(z) #call function
print("Square root of number ", z ,"is ","%.1f" % round(result,1), ".") #print a result and round on 1 decimal place
