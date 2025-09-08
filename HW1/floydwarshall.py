# Solves the all-pairs shortest path
# problem using Floyd Warshall algorithm
def floydWarshall(dist):
    V = len(dist)

    # Add all vertices one by one to
    # the set of intermediate vertices.
    for k in range(V):

        # Pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination
            # for the above picked source
            for j in range(V):
                #shortest path from
                #i to j 
                if(dist[i][k] != 100000000 and dist[k][j]!= 100000000):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

if __name__ == "__main__":
    
    INF = 100000000

    dist = [
      [0, 1, INF, INF, 2, INF, 6, INF], # 0 -> x
      [1, 0, 3, INF, INF, INF, INF, INF], # 1 -> x
      [INF, 3, 0, 5, INF, INF, INF, INF], # 2 -> x
      [INF, INF, 5, 0, INF, INF, INF, 7], # 3 -> x
      [2, INF, INF, INF, 0, 6, INF, INF], # 4 -> x
      [INF, INF, INF, INF, 6, 0, INF, 8], # 5 -> x
      [6, INF, INF, INF, INF, INF, 0, 10], # 6 -> x
      [INF, INF, INF, 7, INF, 8, 10, 0] # 7 -> x
    ]
  
    floydWarshall(dist)
    for i in range(len(dist)):
        for j in range(len(dist)):
            print(dist[i][j], end=" ")
        print()