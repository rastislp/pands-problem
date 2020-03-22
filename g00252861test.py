import random   # importing module that holds a functions to generate random numbers
import time     # importing module that holds a functions and counter to work wih time 


def bubble_sort(nlist):         # defined function of Bubble sort algorithm
    for passnum in range(len(nlist)-1,0,-1):  #for loop of unordered list
        for i in range(passnum):      # for loop 
            if nlist[i]>nlist[i+1]:   # if element is greater than element next to
                temp = nlist[i]       # temorarly store element into variable temp
                nlist[i] = nlist[i+1] # increase index of element by 1 (move to the right of elemnt besides ) 
                nlist[i+1] = temp    # second element (besides current) becomes temp

def merge_sort(nlist):
    #print("Splitting ",nlist)
    if len(nlist)>1:  #conditional statement run until condition is meet
        mid = len(nlist)//2           # divide the list recursively into two halves until it can no more be divided.
        lefthalf = nlist[:mid]          # assign first half of elements into variable lefthalf
        righthalf = nlist[mid:]         # assign second half of elements into variable righthalf

        merge_sort(lefthalf)      # call function
        merge_sort(righthalf)       #call function
        i=j=k=0                     # 0 ssigne to all variables
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:   # used to swap(compare) left and right list elements once these are sorted.
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):        # while loop to deal with all element in lefthalf of list
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):  # while loop to deal with all element in righthalf of list
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
          a += 1    # increment a by 1
      placement *= RADIX
    return nlist        #return new list

def comb_sort(nlist):
    shrink_fact = 1.3  #Set the gap shrink factor
    gaps = len(nlist)  #Initialize gap size
    swapped = True   #Set  swap=1
    i = 0

    while gaps > 1 or swapped:      #Update the gap value for a next comb
        gaps = int(float(gaps) / shrink_fact)   #gap become fraction of shrink_fact

        swapped = False  # If this assignment never happens within the loop,
                         # then there have been no swaps and the list is sorted.
        i = 0

        while gaps + i < len(nlist):
            if nlist[i] > nlist[i+gaps]: 
                nlist[i], nlist[i+gaps] = nlist[i+gaps], nlist[i]
                swapped = True
            i += 1
    return nlist  #return new list

def pancake_sort(nlist):
    arr_len = len(nlist)       # assign count of nlist element into arr_len 
    while arr_len > 1:         # run while condition is meet
        mi = nlist.index(max(nlist[0:arr_len]))    #Find index of the maximum element in arr 
        nlist = nlist[mi::-1] + nlist[mi+1:len(nlist)]   #Call flip(array, iMax)
        nlist = nlist[arr_len-1::-1] + nlist[arr_len:len(nlist)] # Call flip(array, unsorted_array_size -1)
        arr_len -= 1     # decrement length of nlist by 1
    return nlist        #return new list

y = 10       # y is initialized to 10 defined  amount of sampling. 
list1 =[101,251,501,751,1001,1251,2501,3751,5001,6751,7501,8751,10001]     # array of input size n 
print()
print("*************************************************************************************************************************************************************************************")
print("   100       250        500        750       1000       1250       2500       3750       5000       6750       7500       8750       10000     *   size n   * Time to complete [sec]*")

total = 0      # total is initialized to 0 used for purpouse of mean(average)
i = 0          # i is initialized to 0
start_time1 = time.time() #assigning start_time1 variable (start clock) for purpouse of time to complete full task 
while i < len(list1):   # while loop is used to assign elements of array list1  
    r = list1[i]        # to variable r which is a top limit of range in formula below
    list1[i] = list1[i] 
    i = i + 1       # increment array index 
    
    for x in range (y):       # for loop for 10 samples
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
end_time1 = time.time ()   #assigning end_time1 variable (stop clock) for purpouse of time to complete full task 
time_elapsed1 = (end_time1 - start_time1)   # calculation of time taken to complete full sorting task
total1 = (f'{ (round((time_elapsed1),4)):2.4f}') #formatting
res1 = total1.zfill(8)    # formating output to seven eight digit number including 4 dec. spaces / filling space with 0 if less than 8
print("* bubble sor *       ",res1,"      *")       # inline print of name algorithm used 

#no comments below as code is reapeating for remainning 4 algorithm

total =0
i = 0
start_time1 = time.time()
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
end_time1 = time.time ()
time_elapsed1 = (end_time1 - start_time1)
total1 = (f'{ (round((time_elapsed1),4)):2.4f}')   
res1 = total1.zfill(8) 
print("* merge sort *       ",res1,"      *")    

total =0
i = 0
start_time1 = time.time()
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
end_time1 = time.time ()
time_elapsed1 = end_time1 - start_time1  
total1 = (f'{ (round((time_elapsed1),4)):2.4f}')  
res1 = total1.zfill(8)  
print("* radix sort *       ",res1,"      *")    

total =0
i = 0
start_time1 = time.time()
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
end_time1 = time.time ()
time_elapsed1 = end_time1 - start_time1  
total1 = (f'{ (round((time_elapsed1),4)):2.4f}')   
res1 = total1.zfill(8) 
print("* comb sort  *       ",res1,"      *")    

total =0
i = 0
start_time1 = time.time()
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
end_time1 = time.time ()
time_elapsed1 = end_time1 - start_time1  
total1 = (f'{ (round((time_elapsed1),4)):2.4f}')   
res1 = total1.zfill(8) 
print("* pancake so *       "  ,res1,"      *"   )    

print("*************************************************************************************************************************************************************************************")

#-----------------------------This is end of application----------------------------#