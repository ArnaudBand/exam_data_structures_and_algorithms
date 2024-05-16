def adjacency_matrix(graph):
    n = len(graph)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for node in range(n):
        for neighbor, weight in graph[node + 1].items():
            matrix[node][neighbor - 1] = weight
    return matrix

graph = {
    1: {2: 14, 3: 5, 4: 29},
    2: {4: 42, 5: 16},
    3: {6: 5},
    4: {3: 100, 6: 99, 7: 17},
    5: {4: 7, 7: 76},
    6: {},
    7: {6: 82}
}

print(adjacency_matrix(graph))
