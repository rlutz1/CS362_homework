class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = 1e7

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and 
                   sptSet[v] == False and 
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

# Driver program
g = Graph(8)
#           0  1  2  3  4  5  6  7
g.graph = [[0, 1, 0, 0, 2, 0, 6, 0], # 0 -> x
           [1, 0, 3, 0, 0, 0, 0, 0], # 1 -> x
           [0, 3, 0, 5, 0, 0, 0, 0], # 2 -> x
           [0, 0, 5, 0, 0, 0, 0, 7], # 3 -> x
           [2, 0, 0, 0, 0, 6, 0, 0], # 4 -> x
           [0, 0, 0, 0, 6, 0, 0, 8], # 5 -> x
           [6, 0, 0, 0, 0, 0, 0, 10], # 6 -> x
           [0, 0, 0, 7, 0, 8, 10, 0] # 7 -> x
           ]

g.dijkstra(0)