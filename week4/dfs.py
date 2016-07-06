# Depth-first search algorithms to find all findable nodes from a start node s
# input: graph, s
# output: a list of findable nodes

explored = []

def dfs(graph, start):
    global explored
    # add the start vertex s to the list of explored nodes
    explored.append(start)
    # for each edge (s,v)
    if start in graph.keys():
        for v in graph.get(start):
            if v not in explored:
                dfs(graph, v)

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
dfs(graph, '1')
print explored