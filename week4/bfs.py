# a breadth-first search implementation for graphs
import Queue

# find all findable nodes from a node s in the graph represented by nodes and edges
# input: nodes, edges, s
# output: all findable nodes from s
def bfs(nodes, edges, s):
    # all nodes initially unexplored
    explored = []
    # mark s as explored
    explored.append(s)
    # let q be a FIFO queue initiated with s
    q = Queue.Queue()
    q.put(s)
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
    return explored

# example 1 - see attached JPG for graphical representation of example 1
nodes = [1,2,3,4,5,6]
edges = [(1,2), (1,3), (2,1), (2,4), (3,4), (3,5),
         (4,2), (4,3), (4,5), (4,6), (5,3), (5,4), (5,6), (6,4), (6,5)]

# example 2
nodes = [1,2,3,4,5,6,7,8,9,10]
edges = [(1,3), (1,5), (3,1), (3,5), (5,1), (5,3), (5,7), (5,9), (7,5), (9,5),
         (2,4), (4,2), (6,8), (6,10), (8,6), (8,10), (10,6), (10,8)]

print str(bfs(nodes, edges, 6))