#count the number of inversions a mergeSort needs to perform
# left inversion: if i,j < n/2
# right inversion: if i, j >= n/2
# split inversion: if i< n/2 <= j
import math

def mergeSort(a):
    no_inversions = 0
    #divide
    start = 0
    end = len(a)
    middle = int(math.ceil(end/float(2)))
    if(len(a) > 1):
        b, part_inv_count1 = mergeSort(a[start:middle])
        c, part_inv_count2 = mergeSort(a[middle:end])
        no_inversions += part_inv_count1
        no_inversions += part_inv_count2
    else:
        return a, no_inversions

    #conquer - e.g. merge
    merged = [0]*(len(b) + len(c))
    jump = 0
    k = 0
    i = 0
    j = 0
    while (k < len(merged)):
        if(b[i]<=c[j]):
            merged[k] = b[i]
            k += 1
            if (i+1 == len(b)):
                merged[k:] = c[j:]
                k = len(merged)
            else:
                i+=1
        if(b[i]>c[j]):
            merged[k] = c[j]
            k += 1
            #count inversions
            tmp_inversions = no_inversions
            no_inversions += (len(b) - i)

            if (j+1 == len(c)):
                merged[k:] = b[i:]
                k = len(merged)
            else:
                j+=1
    return merged, no_inversions

fname = "unsorted_array.txt"
with open(fname) as f:
    content = f.readlines()
    content = map(int, content)
sorted_array, no_inversions = mergeSort(content)
print "final sorted array is - " + str(sorted_array)
print "total number of inversions -> " + str(no_inversions)