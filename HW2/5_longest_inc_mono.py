A = [1, 2, 0, 3, 9] # expected answer: 1 -> 2 -> 3 -> 9

class Node:
    def __init__(self, val, edges, id):
      self.val = val
      self.edges = edges # list of of TO destinations
      self.best_path = []
      self.id = id
      

class Graph:
   def __init__(self):
      self.V = None # list of nodes

   def print(self):
      for v in self.V:
        print("NODE")
        print("ID: ", v.id, " VALUE: ", v.val)
        print("GOES TO:")
        for e in v.edges:
            print(e.val)

# step 1: turn the sequence into a DAG, O(n^2) loop
dag = Graph()

n = len(A)
V = []
id = 0

for node in A:
   V.append(Node(node, [], id))
   id += 1

dag.V = V


i = 0
j = 1

for node in range(i, n): # for each element in A
  E = [] # empty edges
  for dest in range(node + 1, n): # for each element after u element

    if (A[dest] > A[node]): # if it is an increasing value
      E.append(dag.V[dest]) # add an edge from u -> v

  dag.V[node].edges = E

dag.V = V

dag.print()
