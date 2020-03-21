# Rastislav Petras
# 06 March 2020
# Excercise 7 
# Write a program that reads in a text file and outputs the number of i's it contains. 
# The program should take the filename from an argument on the command line.



yourFile = (input ("Please enter defined location of your file:\n   for example: myfile.txt  ")) #write comand prompt on screen

with open(str(yourFile), 'r') as f:   #open file in a read mode note: string of full url or local file
    test_str = f.read()     # whole text asigned into variable test_str 

    count = 0      # counter initiated to 0
    for i in test_str:       # for loop 
        if i == 'e' or i =='E':     #conditional statement to include both e/E
            count = count + 1    # increment cont by 1
  
# printing result  
print ("Count is : " +  str(count))   # print count is and value of cont a a string   