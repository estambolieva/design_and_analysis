# initialize the heap as an empty array
heap = []

# implement the insert function for MIN heap - 0(nlogn)
def insert_min(array):
    global heap
    for i in range(len(array)):
        elem = array[i]
        # insert this element in the first non-empty spacce
        heap.append(elem)
        # bubble this element up to its position at the heap
        no_parent = True
        ind_elem = len(heap)
        while no_parent:
            ind_parent = ind_elem/2
            # check if this element in the root element
            # this is true when the ind of the elem is 1, and its parent ind is 0
            if ind_parent == 0:
                no_parent = False
            # the elem has a parent, compare and swap with parent if necessary
            else:
                parent = heap[ind_parent - 1]
                if elem < parent:
                    # swap elements
                    heap[ind_elem-1] = parent
                    heap[ind_parent-1] = elem
                    # remember indices
                    ind_elem = ind_parent
                else:
                    no_parent = False

# implement the insert function for MIN heap - O(n)
# see illustrated example of this in WSU's lecture slides - starting slide 31
# http://www.eecs.wsu.edu/~ananth/CptS223/Lectures/heaps.pdf
def build_heap(array):
    global heap
    # randomly populate the heap, e.g. copy the array into the heap
    heap = array[:]
    print heap
    # perform bubble up from each internal node starting from the leaves to take care of heap order properly



# implement the extract-min function of the heap
def extract_min():
    global heap
    # delete root
    min_elem = heap.pop(0)
    # take last element and put it as root
    new_root = heap.pop()
    heap.insert(0, new_root)
    # get indices of root and its children
    root_ind = 1
    # bubble root down
    not_done = True
    while not_done:
        first_child_ind = 2*root_ind
        second_child_ind = 2*root_ind + 1
        if new_root <= first_child_ind and new_root <= second_child_ind:
            not_done = False
        else:
            first_child = heap[first_child_ind-1]
            second_child = heap[second_child_ind-1]
            if first_child < second_child:
                # swap root with its first child
                heap[root_ind-1] = first_child
                heap[first_child_ind-1] = new_root
                # update root index
                root_ind = first_child_ind
            else:
                # swap root with its second child
                heap[root_ind-1] = second_child
                heap[second_child_ind-1] = new_root
                # update root index
                root_ind = second_child_ind
    return min_elem

# an array with the elements to be inserted in a heap given in an arbitrary order
array = [13,11,9,4,12,9,4,8,4]
#array = [13,4,11,8,9,4,4,9,12]
array = [150,80,40,30,10,70,110,100,20,90,60,50,120,140,130]
build_heap(array)
print "heap is " + str(heap)
#extract_min()
#print "new heap with popped root is " + str(heap)