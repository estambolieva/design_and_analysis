# a breadth-first search implementation for graphs
import Queue

def get_index(arr, a):
    ind = 0
    for i in range(len(arr)):
        if arr[i] == a:
            ind = i
    return ind

# find the distances between s and all findable from s nodes in the graph represented by nodes and edges
# where the graph is undirected and without weights
# input: nodes, edges, s
# output: an array of distances, where dist(s,s) = 0 and dist(s,v) != 0, when v != s
def bfs(nodes, edges, s):
    # all nodes initially unexplored
    explored = []
    # mark s as explored
    explored.append(s)
    # let q be a FIFO queue initiated with s
    q = Queue.Queue()
    q.put(s)
    # initialize distances from s
    dist = [-1] * len(nodes)
    # set the dist of s to be 0
    dist[get_index(nodes, s)] = 0

    while (not q.empty()):
        # remove the first node of the queue
        v = q.get()
        # for all edges (v, w)
        for e in edges:
            v1 = e[0]
            w = e[1]
            if (v1 == v) and (w not in explored):
                explored.append(w)
                q.put(w)
                node_ind = get_index(nodes, w)
                prev_node_ind = get_index(nodes, v)
                dist[node_ind] = dist[prev_node_ind] + 1
    print "distances are: " + str(dist)
    return explored

# example 1 - see attached JPG for graphical representation of example 1
nodes = [1,2,3,4,5,6]
edges = [(1,2), (1,3), (2,1), (2,4), (3,1), (3,4), (3,5),
         (4,2), (4,3), (4,5), (4,6), (5,3), (5,4), (5,6), (6,4), (6,5)]

# example 2
nodes = [1,2,3,4,5,6,7,8,9,10]
edges = [(1,3), (1,5), (3,1), (3,5), (5,1), (5,3), (5,7), (5,9), (7,5), (9,5),
         (2,4), (4,2), (6,8), (6,10), (8,6), (8,10), (10,6), (10,8)]

print "nodes are:     " + str(bfs(nodes, edges, 10))