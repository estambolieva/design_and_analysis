mstree = set()
seen = set()
covered = set()

def mst(graph):
    global heap, coming_from, seen, original_node_ind, mstree, distances, covered
    # implementation of Prim's Minimun Spanning Tree algorithm
    # using a heap in which we store the vertices of a graph
    while len(heap) > 1:
        # 1. remove min element from min heap
        start_vertex = extract_min()
        start_ind = original_node_ind[start_vertex]
        seen.add(start_vertex)
        # 2. recalculate heap according to the edges coming from start_node
        edge_vertices = graph[start_vertex]
        greedy_node = start_vertex
        greedy_distance = float('inf')
        for tail_vertex in edge_vertices:
            if tail_vertex not in seen:
                tail_ind = original_node_ind[tail_vertex]
                # recalculate its distance and update heap only if distance has changed
                new_distance = edges[(start_vertex, tail_vertex)]
                old_distance = distances[tail_vertex]
                # bookeeping: know the node with we choose on this greedy iteration
                if new_distance < greedy_distance:
                    greedy_distance = new_distance
                    greedy_node = tail_vertex
                # update distances
                if new_distance < old_distance:
                    distances[tail_vertex] = new_distance
                    coming_from[tail_ind] = start_vertex
                    # delete tail_vertex from heap
                    remove_vertex(tail_vertex)
                    # re-insert tail vertex in heap
                    reinsert_vertex(tail_vertex)
        # add the best greedy edge for this round to the Minimum Spanning Tree
        if start_vertex != greedy_node:
            mstree.add((start_vertex, greedy_node))
            covered.add(start_vertex)
            covered.add(greedy_node)
    # take care of vertices which are not yet included in the MST
    for not_covered_vertex in seen.difference(covered):
        mstree.add((coming_from[original_node_ind[not_covered_vertex]], not_covered_vertex))

##############################
# HEAP OPERATIONS: Delete element from the middle, re-insert element, extract-min
##############################
def remove_vertex(vertex):
    global heap, heap_indices
    vertex_ind = heap_indices.get(vertex)
    # bubble vertex up
    # 1 swap vertex and its parent until parent is root
    while vertex_ind != 1:
        parent_ind = vertex_ind/2
        # swap vertices
        parent = heap[parent_ind-1]
        heap[vertex_ind-1] = parent
        heap[parent_ind-1] = vertex
        # swap heap indices
        temp_ind = heap_indices.get(vertex)
        heap_indices[vertex] = heap_indices.get(parent)
        heap_indices[parent] = temp_ind
        # update the new index of the vertex
        vertex_ind = parent_ind
    # 2 remove from top of the heap
    popped_vertex = extract_min()

def reinsert_vertex(vertex):
    global heap, heap_indices
    # a. add vertex at the end of the heap
    heap.append(vertex)
    vert_ind = len(heap)
    heap_indices[vertex] = vert_ind
    # b. bubble up if necessary
    vert_dist = distances.get(vertex)
    parent_ind = (vert_ind/2)
    parent = heap[parent_ind - 1]
    parent_dist = distances.get(parent)
    not_done = (parent_dist > vert_dist)
    while not_done:
        # b.1 swap vertex with its parent
        vertex_ind = heap_indices.get(vertex)
        parent_ind = heap_indices.get(parent)
        heap[vertex_ind - 1] = parent
        heap[parent_ind - 1] = vertex
        # b.2 update vertex and parent indices
        heap_indices[parent] = vertex_ind
        heap_indices[vertex] = parent_ind
        # update not_done
        vertex_ind = parent_ind
        parent_ind = vertex_ind/2
        # check if the parent index is smaller than the root index
        if parent_ind < 1:
            break
        parent = heap[parent_ind - 1]
        vert_dist = distances.get(vertex)
        parent_dist = distances.get(parent)
        not_done = (parent_dist > vert_dist)


def extract_min():
    global heap, heap_indices
    # delete the first element
    min_elem = heap.pop(0)
    heap_indices.pop(min_elem)
    # take last element and put it as root and update heap indices
    new_root = heap.pop()
    # take the last elem and make it the new root
    heap.insert(0, new_root)
    heap_indices[new_root] = 1
    new_root_ind = 1
    # bubble down new root if needed, and according to the distances
    order_not_preserved = True
    while order_not_preserved:
        curr_root = heap[new_root_ind-1]
        curr_dist = distances[curr_root]
        # if we are in the leaves of the heap, interrupt
        first_child_ind = 2*new_root_ind
        if first_child_ind > len(heap):
            break
        first_child = heap[first_child_ind-1]
        first_child_dist = distances[first_child]
        # check if there is a second child of the curr_node
        second_child_ind = 2*new_root_ind + 1
        second_child = float('inf')
        second_child_dist = float('inf')
        if second_child_ind <= len(heap):
            second_child = heap[second_child_ind-1]
            second_child_dist = distances[second_child]
        # check if the heap order property is preserved
        if curr_dist <= first_child_dist and curr_dist <= second_child_dist:
            order_not_preserved = False
        else:
            if first_child_dist >= second_child_dist:
                heap[new_root_ind - 1] = second_child
                heap[second_child_ind - 1] = curr_root
                # update heap indices
                heap_indices[curr_root] = second_child_ind
                heap_indices[second_child] = new_root_ind
                # update new root index
                new_root_ind = second_child_ind
            else:
                heap[new_root_ind - 1] = first_child
                heap[first_child_ind -1] = curr_root
                # update heap indices
                heap_indices[curr_root] = first_child_ind
                heap_indices[first_child] = new_root_ind
                # update new root index
                new_root_ind = first_child_ind
    return min_elem
##############################
# HEAP Operations END
##############################

def add_to_graph(head_vertex, tail_vertex):
    global graph
    other_vertices = []
    if head_vertex in graph:
        other_vertices = graph[head_vertex]
    other_vertices.append(tail_vertex)
    graph[head_vertex] = other_vertices

# 1. read graph
graph = {}
edges = {}
nodes = set()
distances = {}
heap_indices = {}
# read graph
fname = "mst2.txt"
with open(fname) as f:
    for line in f:
        edge_details = line.split(" ")
        head_vertex = int(edge_details[0])
        tail_vertex = int(edge_details[1])
        length = int(edge_details[2])
        nodes.add(head_vertex)
        nodes.add(tail_vertex)
        # update graph dict
        add_to_graph(head_vertex, tail_vertex)
        add_to_graph(tail_vertex, head_vertex)
        # update edge dict
        edges[(head_vertex, tail_vertex)] = length
        edges[(tail_vertex, head_vertex)] = length
        # update distances
        distances[head_vertex] = float('inf')
        distances[tail_vertex]= float('inf')

list_nodes = list(nodes)[:]
ind = 0
original_node_ind = {}
for node in list_nodes:
    original_node_ind[node] = ind
    heap_indices[node] = ind + 1
    ind += 1
heap = list_nodes
start_node = heap[0]
coming_from = [start_node]*len(heap)

mst(graph)
print "the Minimum Spanning Tree of the graph is " + str(mstree)