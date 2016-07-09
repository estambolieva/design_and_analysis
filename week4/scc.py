times = []
time = 0
s = 0
explored = []
leaders = []

scc_len = []
curr_scc = []

def scc(graph):
    global s, num_nodes, nodes, explored, curr_scc
    # 1.reverse graph
    # 2.run DFS-loop on reversed graph: get graph timings and leaders
    for i in range(num_nodes, 0, -1):
        if i not in explored:
            s = i
            dfs_rev(graph, i)
    # 3.run DFS-loop on normal graph with nodes the running time of each node
    # e.g. iterate over the nodes in reverse order of their timing
    # 3.1. update order of nodes according to timing
    new_node_indices = [-1]*num_nodes
    for ind in range(num_nodes):
        curr_node = nodes[ind]
        new_node_indices[ind] = times[curr_node-1]

    # 3.2 iterate over nodes according to descending timing
    explored = []
    for i in range(num_nodes, 0, -1):
        timing_ind = new_node_indices.index(i)
        node = nodes[timing_ind]
        curr_scc = []
        if node not in explored:
            dfs(graph, node)
            scc_len.append(len(curr_scc))
            curr_scc = []

def dfs_rev(graph, i):
    global s, leaders, time, times
    explored.append(i)
    leaders[i-1] = s
    for edge in graph:
        u = edge[0]
        v = edge[1]
        if v == i:
            if u not in explored:
                dfs_rev(graph, u)
    time += 1
    times[i-1] = time

def dfs(graph, node):
    global explored, curr_scc
    explored.append(node)
    curr_scc.append(node)
    for edge in graph:
        u = edge[0]
        v = edge[1]
        if u == node:
            if v not in explored:
                dfs(graph, v)

def get_nodes_l(graph):
    nodes = []
    for k in graph:
        for i in k:
            if i not in nodes:
                nodes.append(i)
    return nodes

# scc example 6 - list of adjacent elements representation. See ./week4/examples/scc_example_6.jpg
graph = [[1,4],[4,7],[7,1],[9,7],[9,3],[3,6],[6,9],[8,6],[8,5],[5,2],[2,8]]

# scc example 7 - list of adjacent elements representation. See ./week4/examples/scc_example_7.jpg
graph = [[1,2],[2,3],[3,1],[2,4],[4,9],[4,10],[9,10],
         [10,11],[11,9],[3,5],[3,6],[5,6],[6,7],[6,8],[7,8],[8,5],[6,9],[7,11]]

# get all nodes
nodes = get_nodes_l(graph)
num_nodes = len(nodes)
# do initialization
times = [-1] * num_nodes
leaders = [-1] * num_nodes

# call the SCC method
scc(graph)
print "SCCs found are of lenght -> " + str(scc_len)
