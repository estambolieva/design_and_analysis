import random

def rMinCut(nodes, edges):
    # until we have only two nodes left
    while (len(nodes) > 2):
        # select at random an edge (u,v) from the list of edges
        edge_ind = random.randrange(0, len(nodes))
        uv = edges[edge_ind]
        u = uv[0]
        v = uv[1]
        node_to_remove = v
        # replace all v-s with u-s in the list of edges
        i = 0
        while (i < len(edges)):
            u1v1 = edges[i]
            u1 = u1v1[0]
            v1 = u1v1[1]
            if (u1 == v):
                edges[i] = (u, v1)
                # remove self-loops, e.g. (u,u)
                if (u == v1):
                    edges.remove(edges[i])
                    i -= 1
            if (v1 == v):
                edges[i] = (u1, u)
                # remove self-loops, e.g. (u,u)
                if (u1 == u):
                    edges.remove(edges[i])
                    i -= 1
            i += 1
        # remove u from the list of nodes
        nodes.remove(node_to_remove)

    return (len(edges)/2)

#example 1
#v = [1,2,3,4]
#e = [(1,2), (1,4), (2,1), (2,3), (2,4), (3,2), (3,4), (4,1), (4,2), (4,3)]

#example 2
#v = [1,2,3,4,5]
#e = [(1,2), (1,5), (2,1), (2,3), (2,4), (2,5), (3,2), (3,4), (3,5), (4,2), (4,3), (4,5), (5,1), (5,2), (5,3), (5,4)]

#example 3
#n = [1,2,3,4,5,6,7,8]
#e = [(1,2), (1,7), (1,8), (2,1), (2,3), (2,7), (2,8), (3,2), (3,4), (3,5), (3,6), (4,3), (4,5), (4,6), (5,3), (5,4), (5,6), (6,3), (6,4), (6,5), (6,7), (7,1), (7,2), (7,6), (7,8), (8,1), (8,2), (8,7)]

fname = "C:\\Users\\estam_000\\Downloads\\rMinCutGraph.txt"
v = []
e = []
with open(fname) as f:
    for line in f:
        content = line.split()
        content = map(int, content)
        cur_node = content[0]
        v.append(cur_node)
        content.remove(content[0])
        for i in content:
            e.append((cur_node, i))
print "nodes and edges lenght -> " + str(len(v)) + " and " + str(len(e))
run_ind = 0
outcomes = []
eds = e[:]
nds = v[:]
while run_ind < 4000:
    outcomes.append(rMinCut(v, e))
    run_ind += 1
    e = eds[:]
    v = nds[:]
print str(outcomes)
print "min cut is -> " + str(min(outcomes))