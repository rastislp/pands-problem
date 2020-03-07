#Rastislav Petras 
#CTA Project
#bubble sort algorithm

import random
import time


def bubbleSort(nlist):

    for passnum in range(len(nlist)-1,0,-1):

        for i in range(passnum):

            if nlist[i]>nlist[i+1]:

                temp = nlist[i]

                nlist[i] = nlist[i+1]

                nlist[i+1] = temp




total = 0   # 
y = 10   # defined  amount of sampling 

for x in range (y):

    start_time = time.time()

    nlist = [random.randint(0, 100000) for x in range(1, 1001)]

    #print(nlist)

    bubbleSort(nlist)

    #print(nlist)

    end_time = time.time ()

    time_elapsed = end_time - start_time

    total = total + time_elapsed

    #print(time_elapsed)
#print(total)    
print(total/y)  # average time of 10 sampllings






