import random

def rSelect(a, start, end, k):
    # base case
    if ((end - start) == 1):
        return a[start:end][0]
    # get the index of the k-th order statistics
    k_ind = k - 1
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
    # recursive call
    if (i == k_ind):
        return a[i]
    if(i > k_ind):
        return rSelect(a, start, i, k)
    else:
        return rSelect(a, i + 1, end, k)

#a = [3,8,2,5,1,4,7,6]
a = [10,8,2,4]
# get the 3rd order statistics of the array [10,8,2,4]
ith_order = rSelect(a, 0, len(a), 3)
print "i-th order is " + str(ith_order)