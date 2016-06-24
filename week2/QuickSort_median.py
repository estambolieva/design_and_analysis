no_comparisons = 0

def choose_pivot(first, middle, last):
    list = [first, middle, last]
    list.sort()
    median = list[1]
    return median

def quickSort(a,start, end):
    global no_comparisons, first_pass
    # base case
    if ((end - start) == 1):
        return a
    first = a[start]
    last = a[end-1]
    middle_ind = start + int(((end-1-start)/2))
    middle = a[middle_ind]
    median = choose_pivot(first, middle, last)
    pivot_ind = a.index(median)
    pivot = a[pivot_ind]
    # swap pivot and the first element of the array
    a[pivot_ind] = a[start]
    a[start] = pivot
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
        no_comparisons += (i - start - 2)
        quickSort(a, start, i-1)
    if(end - i >= 1):
        no_comparisons += (end - i - 1)
        quickSort(a, i, end)

fname = "quick_sorted_array.txt"
with open(fname) as f:
    content = f.readlines()
    content = map(int, content)
#content = [10, 1, 8, 2, 7, 3, 6, 4, 5, 20, 12]
#content = [3,8,2,5,1,4,7,6]
#content = [8,2,4,5,7,1]
n = len(content)
quickSort(content, 0, n)
no_comparisons += (n - 1)
print "sorted array is -> " + str(content)
print "number of comparisons -> " + str(no_comparisons)