import math

def mergeSort(a):
    #divide
    start = 0
    end = len(a)
    middle = int(math.ceil(end/float(2)))
    if(len(a) > 1):
        b = mergeSort(a[start:middle])
        c = mergeSort(a[middle:end])
    else:
        return a

    #conquer - e.g. merge
    merged = [0]*(len(b) + len(c))
    print "b and c are:" + str(b) + " and " + str(c)
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
            if (j+1 == len(c)):
                merged[k:] = b[i:]
                k = len(merged)
            else:
                j+=1
    return merged

a = [6,5,4,1,4,8,7,2,6,3,5]
print "final sorted array is - " + str(mergeSort(a))