# Rastislav Petras
# 06 March 2020
# week 7
# open file

with open('.gitignore', 'r') as f:
#with open('C:\\Users\\user\\Anaconda3\\python.exe', 'r') as f:    
    #print(f.readline(), end=" ")
    for line in f:
        print(line,end=" ")


print("This is end")    


f.close()