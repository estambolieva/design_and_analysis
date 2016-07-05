# track the path between node s and node v in a graph
# implementation taken from Stackoverflow:
# http://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search

def bfs(graph, start, end):
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
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        print "adjacents to " + str(node) + " are " + str(graph.get(node, []))
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            print "new path is " + str(new_path)
            queue.append(new_path)

# example 1 - list of adjacent elements representation
graph = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['4', '5'],
    '4': ['5', '6'],
    '5': ['6'],
}

# example 3 - list of adjacent elements representation
graph = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}

print bfs(graph, '1', '6')