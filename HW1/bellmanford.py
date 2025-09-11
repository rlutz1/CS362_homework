class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            #self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bellman_ford(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0

        for i in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    if self.adj_matrix[u][v] != 0:
                        if distances[u] + self.adj_matrix[u][v] < distances[v]:
                            distances[v] = distances[u] + self.adj_matrix[u][v]
                            print(f"Relaxing edge {self.vertex_data[u]}-{self.vertex_data[v]}, Updated distance to {self.vertex_data[v]}: {distances[v]}")
                        # else:
                            # print("NOT relaxing edge (", u, ", ", v, ").") # added by RL

        return distances

g = Graph(8)

g.add_vertex_data(0, '0')
g.add_vertex_data(1, '1')
g.add_vertex_data(2, '2')
g.add_vertex_data(3, '3')
g.add_vertex_data(4, '4')
g.add_vertex_data(5, '5')
g.add_vertex_data(6, '6')
g.add_vertex_data(7, '7')

g.add_edge(0, 1, 1) # 0 -- 1, weight 1
g.add_edge(1, 0, 1) 

g.add_edge(1, 2, 3) # 1 -- 2, weight 3
g.add_edge(2, 1, 3) 

g.add_edge(2, 3, 5) # 2 -- 3, weight 5
g.add_edge(3, 2, 5) 

g.add_edge(3, 7, 7) # 3 -- 7, weight 7
g.add_edge(7, 3, 7) 

g.add_edge(0, 4, 2) # 0 -- 4, weight 2
g.add_edge(4, 0, 2)

g.add_edge(4, 5, 6) # 4 -- 5, weight 6
g.add_edge(5, 4, 6)

g.add_edge(5, 7, 8) # 5 -- 7, weight 8
g.add_edge(7, 5, 8)

g.add_edge(0, 6, 6) # 0 -- 6, weight 6
g.add_edge(6, 0, 6)

g.add_edge(6, 7, 10) # 6 -- 7, weight 10
g.add_edge(7, 6, 10)

# Running the Bellman-Ford algorithm from D to all vertices
print("\nThe Bellman-Ford Algorithm starting from vertex 0:")
distances = g.bellman_ford('0')
for i, d in enumerate(distances):
    print(f"Distance from 0 to {g.vertex_data[i]}: {d}")

#  -------------------------------------------------------------
#  A DIFFERENT IMPLEMENTATION AS TEST
#  https://www.geeksforgeeks.org/dsa/bellman-ford-algorithm-in-python/
#  -------------------------------------------------------------


# # 1. Initialize distances to all vertices as infinite and the distance to the source vertex as 0.
# # 2. Relax all edges |V| - 1 times.
# # 3. If we can find a shorter path, then there is a negative weight cycle in the graph


# def bellman_ford(graph, source):
#     # Step 1: Initialize distances
#     distances = {vertex: float('inf') for vertex in graph}
#     distances[source] = 0

#     # Step 2: Relax edges |V| - 1 times
#     for _ in range(len(graph) - 1):
#         for u in graph:
#             for v, weight in graph[u].items():
#                 if distances[u] != float('inf') and distances[u] + weight < distances[v]:
#                     distances[v] = distances[u] + weight
#             print("vertex ", u, ": ", distances)
#         print("iterated through all edges") 
#         print()


            

#     # Step 3: Check for negative weight cycles
#     for u in graph:
#         for v, weight in graph[u].items():
#             if distances[u] != float('inf') and distances[u] + weight < distances[v]:
#                 raise ValueError("Graph contains negative weight cycle")

#     return distances


# # Example

# # hw example
# # graph = {
# #     '0': {'1': 1, '4': 2, '6': 6},
# #     '1': {'0': 1, '2': 3},
# #     '2': {'1': 3, '3': 5},
# #     '3': {'2': 5, '7': 7},
# #     '4': {'0': 2, '5': 6},
# #     '5': {'4': 6, '7': 8},
# #     '6': {'0': 6, '7': 10},
# #     '7': {'6': 10, '5': 8, '3': 7}
# # }

# # toying with the NUMERIC order of vertices
# # now 0 -> 6 -> 7 is found first, lol
# graph = {
#     '0': {'6': 1, '4': 2, '1': 6},
#     '1': {'0': 6, '7': 10},
#     '2': {'1': 3, '3': 5},
#     '3': {'2': 5, '7': 7},
#     '4': {'0': 2, '5': 6},
#     '5': {'4': 6, '7': 8},
#     '6': {'0': 1, '2': 3},
#     '7': {'6': 10, '5': 8, '3': 7}
# }

# # with a neg edge 
# # graph = {
# #     '0' : { '1': 4, '2': 5 }, 
# #     '1' : { '3': 4 },
# #     '2' : { '4': 2 },
# #     '3' : { '2': -5 },
# #     '4' : {}
# # }

# # with a neg cycle
# # graph = {
# #     '0' : { '1': 4, '2': 5 }, 
# #     '1' : { '3': 4 },
# #     '2' : { '4': 2 },
# #     '3' : { '2': -5 },
# #     '4' : { '3': 2 }
# # }
# source = '0'

# shortest_distances = bellman_ford(graph, source)
# print(shortest_distances)