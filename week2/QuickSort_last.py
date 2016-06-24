no_comparisons = 0

def quickSort(a,start, end):
    global no_comparisons, first_pass
    # base case
    if ((end - start) == 1):
        return a
    # select pivot - pivot is the last element of the array
    pivot_ind = end - 1
    pivot = a[pivot_ind]
    # partition around pivot
    i = start
    for j in range(start, end):
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
    temp_pivot = a[i]
    a[i] = a[pivot_ind]
    a[pivot_ind] = temp_pivot
    # recursive calls
    if ((i - start) >= 1):
        no_comparisons += (i - start - 1)
        quickSort(a, start, i)
    if (end - i - 1>= 1):

        no_comparisons += (end - i - 2)
        quickSort(a, i + 1, end)

fname = "C:\\Users\\estam_000\\Downloads\\quick_sorted_array.txt"
with open(fname) as f:
    content = f.readlines()
    content = map(int, content)
#content = [10, 1, 8, 2, 7, 3, 6, 4, 5, 20, 12]
#content = [3,8,2,5,1,4,7,6]
#content = [5,4,3,2,1]
n = len(content)
quickSort(content, 0, n)
no_comparisons += (n - 1)
print "sorted array is -> " + str(content)
print "number of comparisons -> " + str(no_comparisons)