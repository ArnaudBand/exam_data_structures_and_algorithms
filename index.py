import heapq

# Dijkstra's algorithm implementation to find the shortest path between nodes in a weighted graph
def dijkstra(graph, start, end):
    # Initialize distances dictionary with infinite values for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Create a priority queue with the start node and its distance (0)
    priority_queue = [(0, start)]

    # Continue until the priority queue is empty
    while priority_queue:
        # Extract the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current node is the end node, return its distance
        if current_node == end:
            return current_distance

        # Iterate over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to the neighbor through the current node
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update its distance and add it to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # If no path is found from the start node to the end node, return infinity
    return float('inf')

# Example graph represented as an adjacency list
graph = {
    1: {2: 14, 3: 5, 4: 29},
    2: {4: 42, 5: 16},
    3: {6: 5},
    4: {3: 100, 6: 99, 7: 17},
    5: {4: 7, 7: 76},
    6: {},
    7: {6: 82}
}

# Example usage: Find the shortest path from node 1 to node 2
print(dijkstra(graph, 1, 7))