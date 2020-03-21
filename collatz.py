# Rastislav Petras
# 07 feb 2020
# excercise 4 Write a program that asks the user to input any positive
#  integer and outputs the successive values of the following calculation.
#  At each step calculate the next value by taking the current value and
#  if it is even, divide it by two, but if it is odd, multiply it by three
#  and add one. Have the program end if the current value is one.

#number= int(input ("Please choose your posiive number:  "))

#while(number != 1):
#    if (number % 2) == 0 and number>0: #if number modelo 2 = 0 and greater than 0
#        x=number/2
#        print("Answer is: ",x)
#       break
#    elif(number %2) ==1 and number>0: #if number modelo 2 = 1 and greater than 0
#        x= (number*3) +1
#        print("Answer is: ",x)
#        break
#   else:
#        number <0
#        print("This is not positive number")  
#        break
#print()     
#print("Program Terminated")      

number= int(input ("Please choose your posiive number:  "))  #promt user to enter positive integer
while(number > 1):   #while loop continue running until condition is meet.
    if (number % 2) == 0:   # if number is dividible without remainder
        print(number)   #print current number
        number=number/2    #divide current number by 2     
        
    else :           # otherwise  
       print(number)   #print odd number 
       number= (number*3)+1      #perform multiplication and add 1 to current number
print(1.0)        #print last figure 1 

           
#took me while as i missread but finally got it