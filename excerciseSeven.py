# Rastislav Petras
# 06 March 2020
# Excercise 7 
# Write a program that reads in a text file and outputs the number of i's it contains. 
# The program should take the filename from an argument on the command line.

#This is a few words of my  new file john23 IIIiI

yourFile = (input ("Please enter defined location of your file:\n   for example: myfile.txt  "))

with open(str(yourFile), 'r') as f:
    test_str = f.read()

    count = 0
    for i in test_str: 
        if i == 'i' : 
            count = count + 1
  
# printing result  

print ("Count is : " +  str(count))     