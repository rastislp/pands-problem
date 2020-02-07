# Rastislav Petras
# 07 feb 2020
# excercise 3 strings

#Please enter a sentence: The quick brown fox jumps over the lazy dog.
#.o zletrv pu o wr cu h

#s = "The quick brown fox jumps over the lazy dog."
#print(s[0:45:2])

print()  #blank line
print("Excercise 3.") 
print() #blank line

#height = float(input ("Please enter your hight: "))
str = (input ("Please enter a sentence to be reversed!"))


#str = 'The quick brown fox jumps over the lazy dog.' #initial string
reversed=''.join(reversed(str)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed[0:45:2]) #print the reversed string