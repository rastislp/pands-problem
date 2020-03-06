# Rastislav Petras
# 06 March 2020
# Excercise 6 
# Write a program that reads in a text file and outputs the number of e's it contains. 
# The program should take the filename from an argument on the command line.

with open('.gitignore', 'r') as f:
    #print(f.readline(), end=" ")
    for line in f:
        print(line,end=" ")


print("This is end")    


f.close()