import random
import time
import plotly.graph_objects as go


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

# Declaration of all variables
total = 0       # used for purpouse of mean(average)
y = 10          # defined  amount of sampling
i = 10  


list1 =[ 100, 300,1000,2000,2500]

print("  test        test         test         test         test        size")
i = 0
while i < len(list1):
    r = list1[i] 
    list1[i] = list1[i] 
    i = i + 1
    
    for x in range (y):
        start_time = time.time()
        nlist = [random.randint(0, 100000)
        for x in range(1, r)]
        #print(nlist)
        bubbleSort(nlist)
        #print(nlist)
        end_time = time.time ()
        time_elapsed = end_time - start_time
        total = total + time_elapsed
        #print(time_elapsed)
        #print(total)   
        #print(round((total/y),4))  # average time of 10 sampllings
    res = (round((total/y),4))
    
    print(res, end= "       ")



print("bubble sort")


list1 =[ 100, 300,1000,2000,2500]
total =0

i = 0
while i < len(list1):
    r = list1[i] 
    list1[i] = list1[i] 
    i = i + 1
    
    for x in range (y):
        start_time = time.time()
        nlist = [random.randint(0, 100000)
        for x in range(1, r)]
        #print(nlist)
        bubbleSort(nlist)
        #print(nlist)
        end_time = time.time ()
        time_elapsed = end_time - start_time
        total = total + time_elapsed
        #print(time_elapsed)
        #print(total)   
        #print(round((total/y),4))  # average time of 10 sampllings
    resu = (round((total/y),4))
    
    print(resu, end= "       ")

print("other")    
    
    
 




 


