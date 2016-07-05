# find all paths between node start and a desired node end
# implementation taken from Stackoverflow:

def bfs(graph, start, end, paths):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            paths.append(path)
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

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

paths = []
bfs(graph, '1', '6', paths)
print paths