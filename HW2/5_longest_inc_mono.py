# okay, so that...works, but it's doing a lot of extra work i feel.
# really all we truly need is that double loop if we're smart about it
# so, let's have a cleaner attempt 2

# A = [1, 2, 0, 3, 9] # expected answer: 1 -> 2 -> 3 -> 9
# A = [1, 3, 5, 7, 9, 11] # expected answer: 1 -> 3 -> 5 -> 7 -> 9 -> 11
# A = [3, 2, 1, 0] # yields: 0
A = [7, 6, 5, 7, 9, 11]

n = len(A)
best_path = []
dist = []

for i in range(0, n):
  dist.append(0)

# (1) use dp array to get the longest possible 
# increasing sequence length from each node, left to right
# O(n^2)
for src in range(0, n):
   for dest in range(src + 1, n):
      if A[dest] > A[src]:
         dist[src] += 1

# (2) find the max because i'm too tired to keep track in place
# O(n)
longest = 0
longest_index = 0
for i in range(0, n):
   if dist[i] > longest:
      longest_index = i
      longest = dist[i]

# (3) build the longest subsequence starting from max val
# O(n)
last = A[longest_index]
best_path.append(last)

for j in range(longest_index + 1, n):
   if (A[j] > last):
      last = A[j]
      best_path.append(last)
      
# so we're left with T(n) = 2O(n) + O(n^2) = O(n^2)

print("LONGEST PATH DISTANCES: ", dist)

print("LONGEST MONOTONICALLY INC PATH: ", best_path)

# =====================================================================
# literal DAG approach
# =====================================================================

# # A = [1, 2, 0, 3, 9] # expected answer: 1 -> 2 -> 3 -> 9
# # A = [1, 3, 5, 7, 9, 11] # expected answer: 1 -> 3 -> 5 -> 7 -> 9 -> 11
# A = [3, 2, 1, 0] # yields: 0

# class Node:
#     def __init__(self, val, edges, id):
#       self.val = val
#       self.edges = edges # list of of TO destinations
#       self.best_path = []
#       self.id = id
#       self.in_degree = 0
#     def print(self):
#       print("NODE")
#       print("ID: ", self.id, " VALUE: ", self.val, "INDEGREE: ", self.in_degree)
#       print("GOES TO:")
#       for e in self.edges:
#         print(e.val)

#       print("BEST PATH")
      
#       for node in self.best_path:
#         print(node.val, end=" ")
#       print()
      

# class Graph:
#   def __init__(self):
#       self.V = None # list of nodes

#   def print(self):
#       for v in self.V:
#         v.print()
    
#   def topo_sort(self):
#       temp = self.V.copy() # TODO needs a more careful copy
#       Q = []

#       while temp: # while not empty
#         for v in temp: # for each vertex in V
#           if v.in_degree == 0: # indegree 0
#              Q.append(v) # add to queue
#              for e in v.edges: # for each edge destination
#                 e.in_degree -= 1 # decrement the in degree
#              temp.remove(v) # remove the node
#       # self.V = temp # restore
#       return Q
                

       

   

# # step 1: turn the sequence into a DAG, O(n^2) loop
# dag = Graph()

# n = len(A)
# V = []
# id = 0

# for node in A:
#    V.append(Node(node, [], id))
#    id += 1

# dag.V = V


# i = 0
# j = 1

# for node in range(i, n): # for each element in A
#   E = [] # empty edges
#   for dest in range(node + 1, n): # for each element after u element

#     if (A[dest] > A[node]): # if it is an increasing value
#       E.append(dag.V[dest]) # add an edge from u -> v
#       dag.V[dest].in_degree += 1 # increment indegree for toposort

#   dag.V[node].edges = E

# dag.V = V

# # dag.print()

# # step 2: toposort that bad boy
# topo_sort = dag.topo_sort()
# for node in topo_sort:
#   print(node.val)

# # dag.print()

# # step 3: run a simple BF iteration through topo sort, keeping track of best path

# dist = []

# for i in range(0, n):
#   dist.append(0)


# for src in topo_sort:
#    for dest in src.edges:
#       if dist[src.id] + 1  > dist[dest.id]:
#          dist[dest.id] = dist[src.id] + 1 # update longest path so far
#          print(dist)
#          dest.best_path = []
#          for bp in src.best_path:
#             dest.best_path.append(bp)
#         #  dest.best_path = src.best_path # update the best path to path taken to source
#          dest.best_path.append(src) # add souce to best path
#         #  dest.best_path.append(dest) # add souce to best path
#         #  print("bp update ", "source: ", src.val, ", dest: ", dest.val)
#         #  for bp in dest.best_path:
#         #   print(bp.val, end="->")
#         #  print()

# for v in dag.V:
#    v.best_path.append(v)

# dag.print()

# # step 4: find longest path held
# longest = 0
# best = []
# for v in dag.V:
#    length = len(v.best_path)
#    if length > longest:
#       length = longest
#       best = v.best_path

# # print the longest monotonically increasing sequence
# print("(", end ="")
# for node in best:
#    if node == best[longest - 1]:
#      print(node.val, end = "") 
#    else:
#       print(node.val, end = ", ")
# print(")", end = ",  ")
# print("length: ", longest)


