# Rastislav Petras
# 06 March 2020
# Excercise 7 
# Write a program that reads in a text file and outputs the number of e's it contains. 
# The program should take the filename from an argument on the command line.

#This is a few words of my  new file john23

with open('myfile.txt', 'r') as f:
    test_str = f.readline()

    count = 0
    for i in test_str: 
        if i == 'i' or 'I': 
            count = count + 1
  
# printing result  
count= count-40
print ("Count is : " +  str(count))     