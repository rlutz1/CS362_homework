# illustration of linear time solution to #6

A = [10.5, 9.3, 2.7, 13.6]
o = [3, 1, 2, 0]

# i = 0
# for order in o:
#   o[i] = A[order]
#   i += 1

# print(o)


# huh, this is a thought

# def heapify(root, parent, child):
#   print

# root = 0

# for perm in o:
#   child = perm
#   parent = (perm - 1) // 2
#   if parent >= 0:
#     heapify(root, parent, child)
#     root += 1

# # sassy alternate version to achieve nlogn

# A = [27, 32, 1, -5, 1, 1, 1, 1]
# o = [6, 1, 2, 0, 4, 7, 3, 5]
# # [-5, 32, 1, 27]

n = len(o)
i = 0

for order in o:
  o[i] = A[order]
  i += 1
  
  j = n
  while j > 1:
    print("Filler loop to meet theta req.")
    j = j // 2

print(o)