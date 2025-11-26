def h(x, n): # super basic hash func
  return x % n

def union(S, T, B, n): # union of bloom filter
  for s in S:
    B[h(s, n)] = 1
  for t in T:
    B[h(t, n)] = 1
  return B

def intersect(S, T, B, n):
  B = union(S, T, B, n)
  for s in S:
    B[h(s, n)] = B[h(s, n)] ^ 1
  for t in T:
    B[h(t, n)] = B[h(t, n)] ^ 1
  return B


# simplest case bloom
# let m == n
m = 4
n = 4
B = [0] * n
S = [0, 3, 2]
T = [0, 1, 5]

B = union(S, T, B, n)
print(B)

B = intersect(S, T, B, n)
print(B)


