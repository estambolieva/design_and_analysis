######
# Compute the target values t in the interval [-10000,10000]
# such that there are distinct numbers x,y in the input array
# that satisfy x + y = t
#
# input: an unsorted array of numbers: both positive and negative
# output: the count of all distinct t-s
######
def two_sum(array, lower_bound, upper_bound):
    new_lower_bound_ind = 0
    new_upper_bound_ind = 0
    explored = set()
    pair_set = set()
    # sort array
    quickSort(array, 0, len(array))
    print array
    # for each unique array entries
    cnt = 0
    for i in range(len(array)):
        entry = array[i]
        if entry not in explored:
            # find the new bounds
            new_lower_bound = lower_bound - entry
            new_upper_bound = upper_bound - entry
            l = 0
            r = len(array)
            # binary search for lower_bound for each entry
            new_lower_bound_ind = binary_lower_search(array, l, r, new_lower_bound)
            # binary search for higher_bound for each entry
            new_upper_bound_ind = binary_upper_search(array, l, r, new_upper_bound)
            # find all ys for this particular x, entry ==x
            for j in range(new_lower_bound_ind, new_upper_bound_ind+1):
                y = array[j]
                if i != j:
                    pair_set.add((entry, y))
            explored.add(entry)
    return len(pair_set)

# find the first element which is smaller than entry in sorted array
def binary_lower_search(array, l, r, entry):
    ind = 0
    sub_arr = array[l:r]
    while len(sub_arr) > 0:
        middle_ind = l + (r - l) / 2
        middle_elem = array[middle_ind]
        if middle_elem < entry:
            l = middle_ind + 1
        if middle_elem >= entry:
            ind = middle_ind
            r = middle_ind
        sub_arr = array[l:r]
    return ind

# find the first element which is greater than entry in sorted array
def binary_upper_search(array, l, r, entry):
    ind = 0
    sub_arr = array[l:r]
    while len(sub_arr) > 0:
        middle_ind = l + (r - l) / 2
        middle_elem = array[middle_ind]
        if middle_elem <= entry:
            ind = middle_ind
            l = middle_ind + 1
        if middle_elem > entry:
            r = middle_ind
        sub_arr = array[l:r]
    return ind


def quickSort(a,start, end):
    # base case
    if ((end - start) == 1):
        return a
    # select pivot - pivot is the first element of the array
    pivot = a[start]
    # partition around pivot
    i = start + 1
    for j in range(start + 1, end):
        #check is there is a swap
        if (a[j] < pivot):
            # swap
            if (i != j):
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
            # advance indices
            i = i+1
    # put pivot in rightful position
    new_pivot_ind = a.index(pivot)
    temp_pivot = a[i - 1]
    a[i - 1] = a[new_pivot_ind]
    a[new_pivot_ind] = temp_pivot
    # recursive calls
    if((i-start-2) >= 1):
        quickSort(a, start, i-1)
    if(end - i >= 1):
        quickSort(a, i, end)

unsorted_array = []
fname = "C:\\Users\\estam_000\\Downloads\\2sum_small_arr.txt"
with open(fname) as f:
    for line in f:
        number = int(line)
        unsorted_array.append(number)

count = two_sum(unsorted_array, 3, 10)
print "count is " + str(count)
