

def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}  # store distance from starting node
    parents = {start_node: start_node}  # parents contains an adjacency map of all nodes

    while open_set:
        n = min(open_set, key=lambda x: g[x] + heuristic(x))
        
        if n == stop_node:
            path = reconstruct_path(parents, start_node, stop_node)
            print('Path found:', path)
            return path

        open_set.remove(n)
        closed_set.add(n)

        for (m, weight) in get_neighbors(n):
            if m in closed_set:
                continue

            if m not in open_set:
                open_set.add(m)

            if g.get(m, float('inf')) > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n

    print('Path does not exist!')
    return None

def reconstruct_path(parents, start, stop):
    path = []
    n = stop
    while n != start:
        path.append(n)
        n = parents[n]
    path.append(start)
    path.reverse()
    return path

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return []

def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(n, float('inf'))

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)], 
}

aStarAlgo('A', 'G')

