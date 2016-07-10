scc_len = []

def scc(graph, graph_rev):
    global num_nodes, nodes, scc_len, time
    # 1.reverse graph
    # 2.run DFS-loop on reversed graph: get graph timings and leaders
    explored = set()
    new_nodes = [-1]*num_nodes
    stack = []
    for tail_node in range(num_nodes, 0, -1):
        if tail_node not in explored:
            stack.append(tail_node)
            explored.add(tail_node)
        while stack:
            this_node = stack[-1]
            explored.add(this_node)
            if this_node in graph_rev:
                head_nodes = graph_rev.get(this_node)
                # if there is still an unexplored vertex from these head nodes, explore it
                unexplored_edges_found, unexplored_head_nodes = find_unexplored_edges(head_nodes, explored)
                if unexplored_edges_found:
                    # take the firsts unexplored edge and visit its head node
                    unexplored_vertex = unexplored_head_nodes.pop(0)
                    stack.append(unexplored_vertex)
                else:
                    # reached a deepest point, remember its timing
                    timed_node = stack.pop()
                    new_nodes[time-1]= timed_node
                    time += 1
            else:
                curr_node = stack.pop()
                new_nodes[time-1] = curr_node
                time += 1

    print "Passed Step 1"
    # 3.run DFS-loop on normal graph with nodes the running time of each node
    # e.g. iterate over nodes according to descending timing
    explored = set()
    scc_stack = []
    for i in range(num_nodes-1, 0, -1):
        node = new_nodes[i]
        if node not in explored:
            curr_scc = [node]
            scc_stack.append(node)
            explored.add(node)
            while scc_stack:
                tail_node = scc_stack.pop()
                if tail_node in graph:
                    for head_node in graph.get(tail_node):
                        if head_node not in explored:
                            explored.add(head_node)
                            scc_stack.append(head_node)
                            curr_scc.append(head_node)
            scc_len.append(len(curr_scc))
    print "Passed Step 2"
    #print "new nodes " + str(new_nodes)

def find_unexplored_edges(head_nodes, explored):
    unexplored = []
    for node in head_nodes:
        if node not in explored:
            unexplored.append(node)
    return (len(unexplored) != 0), unexplored

graph = []
fname = "C:\\Users\\estam_000\\Downloads\\scc_graph.txt"

nodes = set()
graph = {}
graph_rev = {}
cnt = 0
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
        if cnt % 20000 == 0:
            print "read " + str(cnt) + " lines ......"

# get all nodes
nodes = list(nodes)
num_nodes = len(nodes)

# do initialization
time = 1
times = [-1] * num_nodes
leaders = [-1] * num_nodes

# call the SCC method
scc(graph, graph_rev)
print "SCCs found are of lenght -> " + str(sorted(scc_len, reverse=True)[0:5])

