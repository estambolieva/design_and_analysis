def dijkstra(graph, start_node):
    global distances, heap, heap_set, edges
    distances[start_node] = 0
    cnt = 0
    while heap:
        # popped_vertex == start_node for the first iteration
        popped_vertex = extract_min()
        heap_dict.pop(popped_vertex)
        # check if there is not only one elem left in heap
        if len(heap) == 1:
            last_vertex = heap.pop(0)
            break
        # see all edges (u,v) where u == popped_vertex
        vertices = graph[popped_vertex]
        for head_vertex in vertices:
            # check if this vertex has been removed from the heap
            if head_vertex in heap_dict:
                dist = edges.get((popped_vertex, head_vertex))
                # for each vertex
                # a. remove it from the heap
                remove_vertex(head_vertex)
                # b. calculate the new distance of vertex - min(old_distance, dist[u] + (u,vertex))
                old_dist = distances.get(vertex)
                distances[head_vertex] = \
                    min(old_dist, distances.get(popped_vertex) + edges.get((popped_vertex, head_vertex)))
                # c. re-insert vertex with its new distance and adjust according the order property
                reinsert_vertex(head_vertex)
                cnt += 1

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
    parent_ind = ((vert_ind - 1)/2)
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
        parent_ind = (vertex_ind-1)/2
        # check if the parent index is smaller than the root index
        if parent_ind < 1:
            break
        parent = heap[parent_ind - 1]
        vert_dist = distances.get(vertex)
        parent_dist = distances.get(parent)
        not_done = (parent_dist > vert_dist)


def extract_min():
    global heap
    # delete the first element
    min_elem = heap.pop(0)
    # take last element and put it as root and update heap indices
    new_root = heap.pop()
    heap_indices.pop(min_elem)
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
                heap_indices[first_child_ind] = new_root_ind
                # update new root index
                new_root_ind = first_child_ind
    return min_elem

graph = {}
edges = {}
nodes = set()
distances = {}
heap_indices = {}
# read graph
fname = "dijkstra_small2.txt"
with open(fname) as f:
    for line in f:
        parts = line.split(" ")
        vertex = int(parts[0])
        nodes.add(vertex)
        parts.pop(0)
        while parts:
            vertex_dist = parts[0].split(",")
            head_vertex = int(vertex_dist[0])
            distance = int(vertex_dist[1])
            # update graph
            other_head_nodes = []
            if vertex in graph:
                other_head_nodes = graph[vertex]
            other_head_nodes.append(head_vertex)
            graph[vertex] = other_head_nodes
            # update edges
            edges[(vertex,head_vertex)] = distance
            parts.pop(0)
nodes = list(nodes)
ind = 1
for node in nodes:
    distances[node] = float('inf')
    heap_indices[node] = ind
    ind += 1
heap = nodes[:]
heap_dict = {}
for node in heap:
    heap_dict[node] = True
dijkstra(graph, 1)

print distances