import random
def quickSort(a,start, end):
    # base case
    if ((end - start) == 1):
        return a
    # select pivot - pivot index is in [start, end)
    pivot_ind = random.randrange(start, end)
    pivot = a[pivot_ind]
    # partition around pivot
    i = start
    j_initial = start
    for j in range(j_initial, end):
        #check is there is a swap
        if (a[j] < pivot):
            # swap
            if (i != j):
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
            # advance indices
            i += 1
    # put pivot in rightful position
    new_pivot_ind = a.index(pivot)
    temp_pivot = a[i]
    a[i] = a[new_pivot_ind]
    a[new_pivot_ind] = temp_pivot
    # recursive calls
    if((i-start) >= 1):
        quickSort(a, start, i)
    if(end-(i+1) >= 1):
        quickSort(a, i + 1, end)

#a = [3,8,2,5,1,4,7,6]
#a = [10,9,7,8,5,6,4,3,2,1]
a = [1,2,3,4,5,6]
quickSort(a, 0, len(a))
print "sorted array is -> " + str(a)