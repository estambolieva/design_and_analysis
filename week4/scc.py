import sys
import pdb

sys.setrecursionlimit(2000)

times = []
time = 0
s = 0
explored = []
leaders = []

scc_len = []
curr_scc = []

def scc(graph, graph_rev):
    global s, num_nodes, nodes, explored, curr_scc
    # 1.reverse graph
    # 2.run DFS-loop on reversed graph: get graph timings and leaders
    for i in range(num_nodes, 0, -1):
        if i not in explored:
            s = i
            dfs_rev(graph_rev, i)
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

def dfs_rev(graph_rev, i):
    global s, leaders, time, times
    explored.append(i)
    leaders[i-1] = s
    # for each arc (i, head_node)
    if i in graph_rev:
        for head_node in graph_rev.get(i):
            if head_node not in explored:
                dfs_rev(graph_rev, head_node)
    time += 1
    times[i-1] = time

def dfs(graph, node):
    global explored, curr_scc
    explored.append(node)
    curr_scc.append(node)
    # for arc (node, head_node)
    if node in graph:
        for head_node in graph.get(node):
            if head_node not in explored:
                dfs(graph, head_node)

graph = []
fname = "C:\\Users\\estam_000\\Downloads\\scc_graph.txt"
cnt = 0

nodes = set()
graph = {}
graph_rev = {}
with open(fname) as f:
    for line in f:
        cnt += 1
        edge_nodes = line.split()
        tail_node = int(edge_nodes[0])
        head_node = int(edge_nodes[1])
        # add this edge to graph
        if tail_node not in graph:
            graph[tail_node] = [head_node]
        else:
            other_edges = graph[tail_node]
            other_edges.append(head_node)
            graph[tail_node] = other_edges
        # add reverse edge to reverse graph
        if head_node not in graph_rev:
            graph_rev[head_node] = [tail_node]
        else:
            other_rev_edges = graph_rev[head_node]
            other_rev_edges.append(tail_node)
            graph_rev[head_node] = other_rev_edges
        # record nodes
        nodes.add(int(head_node))
        nodes.add(int(tail_node))
        if (cnt % 10000 == 0):
            print "read " + str(cnt) + " ............"

# get all nodes
#nodes = get_nodes_l(graph)
nodes = list(nodes)
num_nodes = len(nodes)
print len(graph)
print num_nodes
# do initialization
times = [-1] * num_nodes
leaders = [-1] * num_nodes

# call the SCC method
scc(graph, graph_rev)
print "SCCs found are of lenght -> " + str(sorted(scc_len, reverse=True))
