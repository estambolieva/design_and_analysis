import random
def quickSort(a,start, end):
    # base case
    if ((end - start) == 1):
        return a
    # select pivot - pivot index is in [start, end)
    print "NEW ITERATION: (" + str(start) + ":" + str(end) + ")"
    pivot_ind = random.randrange(start, end)
    pivot = a[pivot_ind]
    print "pivot_ind is " + str(pivot_ind) + " and pivot is " + str(pivot)
    # partition around pivot
    if (pivot_ind != start):
        i = start
        j_initial = start
    else:
        i = start + 1
        j_initial = start + 1
    found_greater = False
    for j in range(j_initial, end):
        if (j != pivot_ind):
            print "for i=" + str(i) + " and j=" + str(j) + " ...."
            #check is there is a swap
            if (a[j] < pivot):
                print "a[j] is smaller than pivot and a is " + str(a)
                # swap
                if(i != j):
                    temp = a[j]
                    a[j] = a[i]
                    a[i] = temp
                    # advance indices
                    i = min(i+1, end-1)
                else:
                    if (not found_greater):
                        # advance indices
                        i = min(i+1, end-1)
                print "finished replacing a -> " + str(a)
        else:
            found_greater = True
    # put pivot in rightful position
    pivot_new_ind = a.index(pivot)
    replace_pos_ind = i if found_greater else j
    print "new pivot ind is " + str(pivot_new_ind) + "; and i is " + str(i) + "; and a is " + str(a)
    temp_pivot = a[replace_pos_ind]
    a[replace_pos_ind] = a[pivot_new_ind]
    a[pivot_new_ind] = temp_pivot
    print "before recursive calls - " + str(a)
    # recursive calls
    if((i-start) >= 1):
        quickSort(a, start, i)
    if(end-(i+1) >= 1):
        quickSort(a, i + 1, end)

#a = [3,8,2,5,1,4,7,6]
a = [5,4,3,2,1]
quickSort(a, 0, len(a))
print "sorted array is -> " + str(a)