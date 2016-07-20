class MinHeap():

    min_heap = []

    def insert_one(self, entry):
        # insert one element into the min heap
        self.min_heap.append(entry)
        # bubble up - compare the newly inserted entry to its parent, swap if parent is bigger than it
        entry_ind = len(self.min_heap) - 1
        not_done = True
        while not_done:
            parent_ind = (entry_ind - 1)/2
            if entry_ind < 1:
                not_done = False
            else:
                parent = self.min_heap[parent_ind]
                if (parent > entry):
                    self.min_heap[parent_ind] = entry
                    self.min_heap[entry_ind] = parent
                    entry_ind = parent_ind
                else:
                    not_done = False

    # extract the root element of the heap, e.g. the min elem
    def extract(self):
        # 1. pop the root out of the heap
        min_elem = self.min_heap.pop(0)
        # 2. make the last heap element the root
        new_root = self.min_heap.pop()
        new_root_ind = 1
        self.min_heap.insert(new_root_ind - 1, new_root)
        # 3. bubble down the new root to its rightful place - follow the lower of both children
        continue_bubble_down = True
        while continue_bubble_down:
            # have the leaves been reached? if yes, interrupt
            if (2*new_root_ind) > len(self.min_heap):
                break
            first_child_ind = 2*new_root_ind
            second_child_ind = first_child_ind + 1
            first_child = self.min_heap[first_child_ind - 1]
            second_child = float("inf")
            if second_child_ind - 1 <= len(self.min_heap):
                second_child = self.min_heap[second_child_ind - 1]
            if new_root > first_child or new_root > second_child:
                if first_child <= second_child:
                    self.min_heap[new_root_ind - 1] = first_child
                    self.min_heap[first_child_ind - 1] = new_root
                    new_root_ind = first_child_ind
                else:
                    self.min_heap[new_root_ind - 1] = second_child
                    self.min_heap[second_child_ind - 1] = new_root
                    new_root_ind = second_child_ind
            else:
                continue_bubble_down = False
        return min_elem

    def length(self):
        return len(self.min_heap)

    def printString(self):
        heap = []
        for entry in self.min_heap:
            heap.append(entry)
        print str(heap)

class MaxHeap():

    max_heap = []

    def insert_one(self, entry):
        # put at the end of the heap
        self.max_heap.append(entry)
        entry_ind = len(self.max_heap) - 1
        # bubble up to preserve order propertyentry_ind = len(self.min_heap) - 1
        not_done = True
        while not_done:
            parent_ind = (entry_ind - 1)/2
            if entry_ind < 1:
                not_done = False
            else:
                parent = self.max_heap[parent_ind]
                if (parent < entry):
                    self.max_heap[parent_ind] = entry
                    self.max_heap[entry_ind] = parent
                    entry_ind = parent_ind
                else:
                    not_done = False

    def extract(self):
        # 1. pop the root out of the heap
        max_elem = self.max_heap.pop(0)
        # 2. make the last heap element the root
        new_root = self.max_heap.pop()
        new_root_ind = 1
        self.max_heap.insert(new_root_ind - 1, new_root)
        # 3. bubble down the new root to its rightful place - follow the lower of both children
        continue_bubble_down = True
        while continue_bubble_down:
            # have the leaves been reached? if yes, interrupt
            if (2 * new_root_ind) > len(self.max_heap):
                break
            first_child_ind = 2 * new_root_ind
            second_child_ind = first_child_ind + 1
            first_child = self.max_heap[first_child_ind - 1]
            second_child = float("-inf")
            if second_child_ind <= len(self.max_heap):
                second_child = self.max_heap[second_child_ind - 1]
            print "curr, first and second children " + str(new_root) + " -> " + str(first_child) + " - " + str(second_child)
            if new_root < first_child or new_root < second_child:
                if first_child >= second_child:
                    self.max_heap[new_root_ind - 1] = first_child
                    self.max_heap[first_child_ind - 1] = new_root
                    new_root_ind = first_child_ind
                else:
                    self.max_heap[new_root_ind - 1] = second_child
                    self.max_heap[second_child_ind - 1] = new_root
                    new_root_ind = second_child_ind
            else:
                continue_bubble_down = False
        return max_elem


    def length(self):
        return len(self.min_heap)

    def printString(self):
        heap = []
        for entry in self.max_heap:
            heap.append(entry)
        print str(heap)


min_h = MinHeap()
max_h = MaxHeap()
arr = [20,9,19,11,14,8,15,23,6,50,32,22]
#arr = [1,2,34,23,20,19,18,50,6]
#arr = [10,9,8,7,6,5,4,3,2,1]
#arr = [1,2,3,4,5,6,7,8,9,10,11]
for i in arr:
    max_h.insert_one(i)
print max_h.printString()

max_h.extract()
print max_h.printString()
max_h.extract()
print max_h.printString()
