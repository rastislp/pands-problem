import random
import time

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
sample1 = 10
sample2 = 25
sample3 = 50
sample4 = 75
sample5 = 100
sample6 = 125
sample7 = 250
sample8 = 375
sample9 = 500
sample10 =625
sample11 =750
sample12 =875
sample13 =1000

#while i < 10000:
#    print(i)
#    num = i
#    if (i == 3):
#        break
#    i = i*10

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample1)]
    #print(nlist)
    bubbleSort(nlist)
    #print(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
    #print(time_elapsed)
    #print(total)   
#print(round((total/y),4))  # average time of 10 sampllings
result1 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample2)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result2 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample3)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result3 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample4)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result4 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample5)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result5 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample6)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result6 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample7)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result7 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample8)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result8 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample9)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result9 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample10)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result10 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample11)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result11 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample12)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result12 = (round((total/y),4))

for x in range (y):
    start_time = time.time()
    nlist = [random.randint(0, 10000) for x in range(1, sample13)]
    bubbleSort(nlist)
    end_time = time.time ()
    time_elapsed = end_time - start_time
    total = total + time_elapsed
result13 = (round((total/y),4))

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)
print(result13)

table = {'bubbleSort': result1 ,'sort':result3 }

print("size       ==>      100        250        250        500         750       1000       1250       2500       3750       5000       6250       7500       8250")

for algorithm, result in table.items():
     print(f'{algorithm:10} ==> {result1:10} {result2:10} {result3:10} {result4:10} {result5:10} {result6:10} {result7:10} {result8:10} {result9:10} {result10:10} {result11:10} {result12:10} {result13:10}')

