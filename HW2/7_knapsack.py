# let's START with the recursive idea. i think that's easier to begin with
# since DP is really just recordkeeping of a recursive algorithm
# def knapsack_brute_force(capacity, n):
#   print(f"knapsack_brute_force({capacity},{n})")
#   if n == 0 or capacity == 0:
#       return 0

#   elif weights[n-1] > capacity:
#       return knapsack_brute_force(capacity, n-1)

#   else:
#       include_item = values[n-1] + knapsack_brute_force(capacity-weights[n-1], n-1)
#       exclude_item = knapsack_brute_force(capacity, n-1)
#       return max(include_item, exclude_item)

# values = [300, 200, 400, 500]
# weights = [2, 1, 5, 3]
# capacity = 10
# n = len(values)

# def knapsack_brute_force(capacity_1, capacity_2, n):
#     print(f"knapsack_brute_force({capacity_1},{n} | {capacity_2}, {n})")
    
#     # this is the condition of no more items left
#     # or we can't get anything else in this knapsack
#     if n == 0:
#         return 0
    
#     if n == 0 or capacity_1 == 0:
#         if capacity_2 == 0:
#           return 0
#         try_in_k2 = values[n - 1] + knapsack_brute_force(capacity_1, capacity_2 - weights[n - 1], n - 1)
#         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
#         return max(try_in_k2, try_in_neither)

#     elif n == 0 or capacity_2 == 0:
#         if capacity_1 == 0:
#             return 0
#         try_in_k1 = values[n - 1] + knapsack_brute_force(capacity_1 - weights[n - 1], capacity_2, n - 1)
#         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
#         return max(try_in_k1, try_in_neither)

#     elif weights[n - 1] > capacity_1:
#         try_in_k2 = values[n - 1] + knapsack_brute_force(capacity_1, capacity_2 - weights[n - 1], n - 1)
#         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
#         return max(try_in_k2, try_in_neither)

#     elif weights[n - 1] > capacity_2:
#         try_in_k1 = values[n - 1] + knapsack_brute_force(capacity_1, capacity_2 - weights[n - 1], n - 1)
#         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
#         return max(try_in_k1, try_in_neither)

#     else:
#         try_in_k1 = values[n - 1] + knapsack_brute_force(capacity_1 - weights[n - 1], capacity_2, n - 1)
#         try_in_k2 = values[n - 1] + knapsack_brute_force(capacity_1, capacity_2 - weights[n - 1], n - 1)
#         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
#         return max(try_in_k1, try_in_k2, try_in_neither)

# values = [3, 14, 7]
# weights = [1, 2, 3]
# capacity_1 = 4
# capacity_2 = 2
# n = len(values)

# values = [3, 5, 2]
# weights = [1, 2, 2]
# capacity_1 = 4
# capacity_2 = 2
# n = len(values)

# something is failing on this one
# # algo takes all the items haha
# values = [10, 9, 15, 13]
# weights = [1, 2, 1, 1]
# capacity_1 = 2
# capacity_2 = 2
# n = len(values)

# print("\nMaximum value in Knapsack =", knapsack_brute_force(capacity_1, capacity_2, n))


# w3 schools implementation of top down approach
# def knapsack_tabulation():
#   n = len(values)
#   tab = [[0]*(capacity + 1) for y in range(n + 1)]

#   for i in range(1, n+1):
#       for w in range(1, capacity+1):
#           if weights[i-1] <= w:
#               include_item = values[i-1] + tab[i-1][w-weights[i-1]]
#               exclude_item = tab[i-1][w]
#               tab[i][w] = max(include_item, exclude_item)
#           else:
#               tab[i][w] = tab[i-1][w]
  
#   for row in tab:
#       print(row)
#   return tab[n][capacity]

def get_3d_array(x, y, z):
    arr = []
    for plane in range(0, z):
        new_plane = []
        arr.append(new_plane)
        for row in range(0, y):
            new_plane.append([0] * x)
    return arr


def knapsack_tabulation():
  n = len(values)
  tab = get_3d_array(capacity_1 + 1, n + 1, capacity_2 + 1) 

#   print(tab)

  for i in range(1, n + 1):
      
      for k2_w in range(1, capacity_2 + 1):
            
            for k1_w in range(1, capacity_1 + 1):

                if weights[i - 1] <= k1_w:
                    # include_item_k2 = values[i - 1] + tab[k2_w - weights[i - 1]][i - 1][k1_w]
                    include_item_k1 = values[i - 1] + tab[k2_w][i - 1][k1_w - weights[i - 1]]
                    exclude_item_both = tab[k2_w][i - 1][k1_w]
                    tab[k2_w][i][k1_w] = max(include_item_k1, exclude_item_both) #include_item_k2)
                else:
                    tab[k2_w][i][k1_w] = tab[k2_w][i - 1][k1_w]
                
                if weights[i - 1] <= k2_w:
                    curr_max = tab[k2_w][i][k1_w]
                    include_item_k2 = values[i - 1] + tab[k2_w - weights[i - 1]][i - 1][k1_w]
                    tab[k2_w][i][k1_w] = max(curr_max, include_item_k2)

    
  for plane in tab:
    for row in plane:
        print(row)
  return tab[capacity_2][n][capacity_1]

values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity_1 = 5
capacity_2 = 2
print("\nMaximum value in Knapsack =", knapsack_tabulation())

# 2 knapsacks
# idea: get the max value from the largest knapsack first
# then find what items were used in largest
# rerun algorithm with second knapsack and remaining items