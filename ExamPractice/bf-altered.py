def bellmanFord(V, edges, src, dest, x):
    
    # Initially distance from source to all other vertices 
    # is not known(Infinite) e.g. 1e8.
    dist = [100000000] * V
    dist[src] = 0

    # Relaxation of all the edges V times, not (V - 1) as we
    # need one additional relaxation to detect negative cycle
    
    for i in range(V):
    # while dist[dest] > x:
      for edge in edges:
          u, v, wt = edge
          # if dist[u] != 100000000 and dist[u] + wt < dist[v]:
          if dist[u] != 100000000 and (abs(dist[v] - x) > abs(dist[u] + wt - x)):
              # If this is the Vth relaxation, then there 
              # is a negative cycle
              # if i == V - 1:
              #     return [-1]
              
              # Update shortest distance to node v
              dist[v] = dist[u] + wt

          print(' '.join(map(str, dist)))
    return dist

if __name__ == '__main__':
    V = 4
    # edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
    edges = [
        [0, 1, 1],
        [0, 2, 3],
        [0, 3, 7],
        [1, 3, 4],
        [2, 1, 10],
        [3, 2, 4]
    ]

    src = 0
    dest = 1
    x = 50
    ans = bellmanFord(V, edges, src, dest, x)
    print(' '.join(map(str, ans)))
    
    if ans[dest] == x:
        print("There is a path from ", src, " to ", dest, " of exactly x = ", x)