# 1. Initialize distances to all vertices as infinite and the distance to the source vertex as 0.
# 2. Relax all edges |V| - 1 times.
# 3. If we can find a shorter path, then there is a negative weight cycle in the graph


def bellman_ford(graph, source):
    # Step 1: Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
            print(u, ": ", distances)

            

    # Step 3: Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

    return distances


# Example
graph = {
    '0': {'1': 1, '4': 2, '6': 6},
    '1': {'0': 1, '2': 3},
    '2': {'1': 3, '3': 5},
    '3': {'2': 5, '7': 7},
    '4': {'0': 2, '5': 6},
    '5': {'4': 6, '7': 8},
    '6': {'0': 6, '7': 10},
    '7': {'6': 10, '5': 8, '3': 7}

}
source = '0'

shortest_distances = bellman_ford(graph, source)
print(shortest_distances)