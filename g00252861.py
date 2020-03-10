import random   # importing module that holds a functions to generate random numbers
import time     # importing module that holds a functions and counter to work wih time 


def bubble_sort(nlist):         # defined function of Bubble sort algorithm
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

def merge_sort(nlist):
    #print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",nlist)        

def radix_sort(nlist):
    RADIX = 10
    placement = 1
    max_digit = max(nlist)

    while placement < max_digit:
      buckets = [list() for _ in range( RADIX )]
      for i in nlist:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          nlist[a] = i
          a += 1
      placement *= RADIX
    return nlist        

def comb_sort(nlist):
    shrink_fact = 1.3
    gaps = len(nlist)
    swapped = True
    i = 0

    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink_fact)

        swapped = False
        i = 0

        while gaps + i < len(nlist):
            if nlist[i] > nlist[i+gaps]:
                nlist[i], nlist[i+gaps] = nlist[i+gaps], nlist[i]
                swapped = True
            i += 1
    return nlist  

def pancake_sort(nlist):
    arr_len = len(nlist)
    while arr_len > 1:
        mi = nlist.index(max(nlist[0:arr_len]))
        nlist = nlist[mi::-1] + nlist[mi+1:len(nlist)]
        nlist = nlist[arr_len-1::-1] + nlist[arr_len:len(nlist)]
        arr_len -= 1
    return nlist

y = 10       # y is initialized to 10 defined  amount of sampling. 
list1 =[101,251,501,751,1001,1251,2501,3751,5001,6751,7501,8751,10001]     # array of input size n 

print()
print("**************************************************************************************************************************************************************")
print("   100       250        500        750       1000       1250       2500       3750       5000       6750       7500       8750       10000      size n       *")

total = 0      # total is initialized to 0 used for purpouse of mean(average)
i = 0          # i is initialized to 0
while i < len(list1):   # while loop is used to assign elements of array list1  
    r = list1[i]        # to variable r which is a top limit of range in formula below
    list1[i] = list1[i] 
    i = i + 1       # increment array index 
    
    for x in range (y):       #
        start_time = time.time()        #definning and assigning start_time (start clock)
        nlist = [random.randint(0, 100000)       # generating un-ordered list(nlist) from range 0-99999
        for x in range(1, r)]        # for loop that runs "r" times -> defined earlier in while loops 
        #print(nlist)       # debug purpouse prints un-ordered list
        bubble_sort(nlist)  # performing desired function SORTING
        #print(nlist)       # debug purpouse prints ordered list
        end_time = time.time ()        #definning and assigning end_time 
        time_elapsed = end_time - start_time    #calculates elapsed time 
        total = total + time_elapsed    # adding current elapsed time to previous total 
        res =(f'{ (round((total/y),4)):2.4f}')    # performing  calculation of average total(10) time_samples + formatting to 4 dec. spaces
        res = res.zfill(7)     # formating output to seven digit number including 4 dec. spaces / filling space with 0 if less than 7 
    print(res, end= "    ")    # inline print of result with space appart
print("bubble sort   *")       # inline print of name algorithm used 


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
        merge_sort(nlist)
        #print(nlist)
        end_time = time.time ()
        time_elapsed = end_time - start_time
        total = total + time_elapsed
        res =(f'{ (round((total/y),4)):2.4f}')
        res = res.zfill(7)
    print(res, end= "    ")   
print("merge sort    *")    

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
        radix_sort(nlist)
        #print(nlist)
        end_time = time.time ()
        time_elapsed = end_time - start_time
        total = total + time_elapsed
        #print(time_elapsed)
        res =(f'{ (round((total/y),4)):2.4f}')
        res = res.zfill(7)
    print(res, end= "    ")
print("radix sort    *")    

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
        comb_sort(nlist)
        #print(nlist)
        end_time = time.time ()
        time_elapsed = end_time - start_time
        total = total + time_elapsed
        #print(time_elapsed)
        res =(f'{ (round((total/y),4)):2.4f}')
        res = res.zfill(7)
    print(res, end= "    ")
print("comb sort     *")    

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
        pancake_sort(nlist)
        #print(nlist)
        end_time = time.time ()
        time_elapsed = end_time - start_time
        total = total + time_elapsed
        #print(time_elapsed)
        res =(f'{ (round((total/y),4)):2.4f}')
        res = res.zfill(7)
    print(res, end= "    ")
print("pancake sort  * ")    

print("**************************************************************************************************************************************************************")

#-----------------------------This is end of application----------------------------#