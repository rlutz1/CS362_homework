# illustration of linear time solution to #6

A = [27, 32, 1, -5]
o = [3, 1, 2, 0]
# [-5, 32, 1, 27]

i = 0
for order in o:
  o[i] = A[order]
  i += 1

print(o)

# sassy alternate version to achieve nlogn

A = [27, 32, 1, -5, 1, 1, 1, 1]
o = [6, 1, 2, 0, 4, 7, 3, 5]
# [-5, 32, 1, 27]

n = len(o)
i = 0

for order in o:
  o[i] = A[order]
  i += 1
  
  j = n
  while j > 1:
    # print("Filler loop to meet theta req.")
    j = j // 2

print(o)