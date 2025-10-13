INF = 100000000



adj = [
  [0, 1, 3, 6],
  [INF, 0, INF, 4],
  [INF, 10, 0, INF],
  [INF, INF, 4, 0]
]

new = [
  [0, 1, 3, 6],
  [INF, 0, INF, 4],
  [INF, 10, 0, INF],
  [INF, INF, 4, 0]
]

V = [0, 1, 2, 3]


src = 0
sink = 2
x = 10 # success but only by default
# x = 19 failure
# iterations = [1, 2]

# for i in iterations:
for k in V:
  for a in V:
    for b in V:
      if adj[a][k] != INF and adj[a][b] > adj[a][k] + adj[k][b]: # vanilla sp

      # if adj[a][k] != INF and adj[a][b] > adj[a][k] + adj[k][b]: # vanilla sp
      
      # if adj[a][k] != INF and abs(adj[a][b] - x) > abs(adj[a][k] + adj[k][b] - x): 
      # if adj[a][k] != INF and (adj[a][b] == x or adj[a][k] + adj[k][b] == x):
        adj[a][b] = adj[a][k] + adj[k][b]

  print(k, " paths")
  print(adj)

print("all source shortest paths:")
print(adj)
if adj[src][sink] == x:
  print("congrats, path found from ", src, " to ", sink, " of exactly ", x)
elif x < adj[src][sink]:
  print("sorry NO PATH found from ", src, " to ", sink, " of exactly ", x)
else:
  # hard case. what can we do
  print("third case")
  success = False
  shortestPathDist = adj[src][sink]
  for k in V:
    for a in V:
      for b in V:
        if  new[src][k] != INF and new[k][sink] != INF:
          if shortestPathDist + new[src][k] + new[k][sink] == x:
            print("success: ", shortestPathDist, " + ", src, "->", k, " + ", k, "->", sink)
            success = True
            break
          print(shortestPathDist, " + ", src, "->", k, " + ", k, "->", sink)
      if success: break
    if success: break

  print(success)
  