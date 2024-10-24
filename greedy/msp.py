mst_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def prim_method(graph):
    visited_nodes = set()
    visited_nodes.add(next(iter(graph)))
    results = []
    while(len(visited_nodes) < len(graph)):  
        smallest_weight = None
        smallest_node = None 
        origin_node = None
        for visited_node in visited_nodes:
            for node, weight in graph[visited_node].items():
                if (smallest_weight is None or weight < smallest_weight) and node not in visited_nodes:
                    smallest_weight = weight
                    smallest_node = node
                    origin_node = visited_node
            
        if smallest_node is not None:
            visited_nodes.add(smallest_node)
            results.append((origin_node , smallest_node, smallest_weight))
            
    return results

print(prim_method(mst_graph))

    