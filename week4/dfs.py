# Depth-first search algorithms to do a topological sort
# input: graph, s
# output: a dict with the order for each vertex

explored = []
curr_label = 0
nodes = []
topological_order = {}

# count the number of nodes in the graph
def get_nodes(graph):
    nodes = []
    for k in graph:
        list_of_v = graph[k]
        if k not in nodes:
            nodes.append(k)
        for v in list_of_v:
            if v not in nodes:
                nodes.append(v)
    return nodes

def dfs_topological(graph):
    global explored
    for node in graph:
        if node not in explored:
            dfs(graph, node)

def dfs(graph, node):
    global explored, curr_label
    explored.append(node)
    if (node in graph):
        for v in graph.get(node):
            if v not in explored:
                dfs(graph, v)
    topological_order[node] = curr_label
    curr_label -= 1

# example 1 - list of adjacent elements representation. See ./week4/examples/example_1_&_2.jpg
graph = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['4', '5'],
    '4': ['5', '6'],
    '5': ['6'],
}

# example 3 - list of adjacent elements representation. See ./week4/examples/example_3.jpg
#graph = {
#    '1': ['2', '3', '4'],
#    '2': ['5', '6'],
#    '5': ['9', '10'],
#    '4': ['7', '8'],
#    '7': ['11', '12']
#}

# example 4
graph = {
    's': ['w', 'v'],
    'w': ['t'],
    'v': ['k'],
    't': ['g', 'i'],
    'k': ['i'],
    'i': ['l']
}

# example 5
graph = {
    'i': ['j', 'k'],
    'a': ['c'],
    'b': ['c']
}

nodes = get_nodes(graph)
curr_label = len(nodes)
explored = []
dfs_topological(graph)
print topological_order