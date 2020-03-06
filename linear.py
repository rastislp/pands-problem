
def linear_search(list, target):
    for i in range(len(list)):
        var = list[i]
        if var == target:
            return i
    return -1
    
def linear_search_sorted(list, target):
    for i in range(len(list)):
        var = list[i]
        if var == target:
            return i
        elif var > target:
            return -1
    return -1
    
l = [2,1,3,4,56,74,31]

ls = [1,2,4,5,6,7,8,12,22,23]

print(linear_search(l, 2))

print(linear_search(l, 23))

print(l[-1])

print(linear_search_sorted(ls, 8))