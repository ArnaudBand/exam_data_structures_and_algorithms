def adjacency_list(graph):
    adj_list = {}
    for node in graph:
        adj_list[node] = []
        for neighbor in graph[node]:
            adj_list[node].append(neighbor)
    return adj_list

graph = {
    1: {2: 14, 3: 5, 4: 29},
    2: {4: 42, 5: 16},
    3: {6: 5},
    4: {3: 100, 6: 99, 7: 17},
    5: {4: 7, 7: 76},
    6: {},
    7: {6: 82}
}


print(adjacency_list(graph))