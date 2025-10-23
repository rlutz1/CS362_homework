def print_mtrx(A):
    for plane in A:
        print("---")
        for row in plane:
            print(row)


def fill_knapsacks(cap_1, cap_2, values, weights):

    n = len(values)

    # make a 3d array with + 1 dimension for each thing:
    # items are the PLANES
    # knapsack 1 units are the ROWS
    # knapsack 2 units are the COLUMNS
    dp = [[[0 for _ in range(cap_2 + 1)] for _ in range(cap_1 + 1)]
          for _ in range(n + 1)]

    # for every item
    for item in range(1, n + 1):
        v = values[item - 1] # current value
        w = weights[item - 1] # current weight
        for c_1 in range(0, cap_1 + 1): # for each unit capacity in knapsack 1
            for c_2 in range(0, cap_2 + 1): # for each unit capacity in knapsack 2
                exclude_in_both = dp[item - 1][c_1][c_2] # choice of excluding from both knaps
                include_in_k1 = 0 # init so if we cannot fit in a knap, doesn't fuck up max call
                include_in_k2 = 0

                if w <= c_1: # if we can fit in knap 1
                    include_in_k1 = v + dp[item - 1][c_1 - w][c_2] # try to include
                
                if w <= c_2: # if we can fit in knap 2
                    include_in_k2 = v + dp[item - 1][c_1][c_2 - w] # try to include

                # keep only the max value of all 3 options
                dp[item][c_1][c_2] = max(exclude_in_both, include_in_k1, include_in_k2)
    return dp

def items_included(dp, n, cap_1, cap_2, weights):
    all_included = []
    knap_1 = []
    knap_2 = []

    for item in range(n, 0, -1): # for every item
        w = weights[item - 1] # current weight

        # if the weight is less than current capacity left in k1
        # AND the prior item plane value is different (ie, item i made a difference in value)
        if w <= cap_1 and dp[item][cap_1][cap_2] > dp[item - 1][cap_1][cap_2]:
            all_included.append(item) # gather that item
            knap_1.append(item)
            cap_1 -= w # move back by w rows, reducing k1 capacity so to speak
        
        # otherwise, if the weight is less than current capacity left in k2
        # AND the prior item plane value is different (ie, item i made a difference in value)
        elif w <= cap_2 and dp[item][cap_1][cap_2] > dp[item - 1][cap_1][cap_2]:
            all_included.append(item) # gather the item
            knap_2.append(item)
            cap_2 -= w # move back by w columns, reducing k2 capacity so to speak
    
    print("Knapsack 1 took: ", knap_1)
    print("Knapsack 2 took: ", knap_2)
    return all_included


values = [10, 9, 25, 13]
weights = [1, 2, 6, 1]
capacity_1 = 3
capacity_2 = 6

dp = fill_knapsacks(capacity_1, capacity_2, values, weights)
print_mtrx(dp)

print("Max profit: ", dp[len(values)][capacity_1][capacity_2])

print("Total items included: ", items_included(dp, len(values), capacity_1, capacity_2, weights))



# # let's START with the recursive idea. i think that's easier to begin with
# # since DP is really just recordkeeping of a recursive algorithm
# # def knapsack_brute_force(capacity, n):
# #   print(f"knapsack_brute_force({capacity},{n})")
# #   if n == 0 or capacity == 0:
# #       return 0

# #   elif weights[n-1] > capacity:
# #       return knapsack_brute_force(capacity, n-1)

# #   else:
# #       include_item = values[n-1] + knapsack_brute_force(capacity-weights[n-1], n-1)
# #       exclude_item = knapsack_brute_force(capacity, n-1)
# #       return max(include_item, exclude_item)

# # values = [300, 200, 400, 500]
# # weights = [2, 1, 5, 3]
# # capacity = 10
# # n = len(values)

# # def knapsack_brute_force(capacity_1, capacity_2, n):
# #     print(f"knapsack_brute_force({capacity_1},{n} | {capacity_2}, {n})")
    
# #     # this is the condition of no more items left
# #     # or we can't get anything else in this knapsack
# #     if n == 0:
# #         return 0
    
# #     if n == 0 or capacity_1 == 0:
# #         if capacity_2 == 0:
# #           return 0
# #         try_in_k2 = values[n - 1] + knapsack_brute_force(capacity_1, capacity_2 - weights[n - 1], n - 1)
# #         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
# #         return max(try_in_k2, try_in_neither)

# #     elif n == 0 or capacity_2 == 0:
# #         if capacity_1 == 0:
# #             return 0
# #         try_in_k1 = values[n - 1] + knapsack_brute_force(capacity_1 - weights[n - 1], capacity_2, n - 1)
# #         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
# #         return max(try_in_k1, try_in_neither)

# #     elif weights[n - 1] > capacity_1:
# #         try_in_k2 = values[n - 1] + knapsack_brute_force(capacity_1, capacity_2 - weights[n - 1], n - 1)
# #         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
# #         return max(try_in_k2, try_in_neither)

# #     elif weights[n - 1] > capacity_2:
# #         try_in_k1 = values[n - 1] + knapsack_brute_force(capacity_1, capacity_2 - weights[n - 1], n - 1)
# #         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
# #         return max(try_in_k1, try_in_neither)

# #     else:
# #         try_in_k1 = values[n - 1] + knapsack_brute_force(capacity_1 - weights[n - 1], capacity_2, n - 1)
# #         try_in_k2 = values[n - 1] + knapsack_brute_force(capacity_1, capacity_2 - weights[n - 1], n - 1)
# #         try_in_neither = knapsack_brute_force(capacity_1, capacity_2, n - 1)
# #         return max(try_in_k1, try_in_k2, try_in_neither)

# # values = [3, 14, 7]
# # weights = [1, 2, 3]
# # capacity_1 = 4
# # capacity_2 = 2
# # n = len(values)

# # values = [3, 5, 2]
# # weights = [1, 2, 2]
# # capacity_1 = 4
# # capacity_2 = 2
# # n = len(values)

# # something is failing on this one
# # # algo takes all the items haha
# # values = [10, 9, 15, 13]
# # weights = [1, 2, 1, 1]
# # capacity_1 = 2
# # capacity_2 = 2
# # n = len(values)

# # print("\nMaximum value in Knapsack =", knapsack_brute_force(capacity_1, capacity_2, n))


# # w3 schools implementation of top down approach
# # def knapsack_tabulation():
# #   n = len(values)
# #   tab = [[0]*(capacity + 1) for y in range(n + 1)]

# #   for i in range(1, n+1):
# #       for w in range(1, capacity+1):
# #           if weights[i-1] <= w:
# #               include_item = values[i-1] + tab[i-1][w-weights[i-1]]
# #               exclude_item = tab[i-1][w]
# #               tab[i][w] = max(include_item, exclude_item)
# #           else:
# #               tab[i][w] = tab[i-1][w]
  
# #   for row in tab:
# #       print(row)
# #   return tab[n][capacity]

# def get_3d_array(x, y, z):
#     arr = []
#     for plane in range(0, z):
#         new_plane = []
#         arr.append(new_plane)
#         for row in range(0, y):
#             new_plane.append([0] * x)
#     return arr


# def knapsack_tabulation():
#   n = len(values)
#   tab = get_3d_array(capacity_1 + 1, n + 1, capacity_2 + 1) 

# #   print(tab)

#   for i in range(1, n + 1):
      
#       for k2_w in range(1, capacity_2 + 1):
            
#             for k1_w in range(1, capacity_1 + 1):

#                 if weights[i - 1] <= k1_w:
#                     # include_item_k2 = values[i - 1] + tab[k2_w - weights[i - 1]][i - 1][k1_w]
#                     include_item_k1 = values[i - 1] + tab[k2_w][i - 1][k1_w - weights[i - 1]]
#                     exclude_item_both = tab[k2_w][i - 1][k1_w]
#                     tab[k2_w][i][k1_w] = max(include_item_k1, exclude_item_both) #include_item_k2)
#                 else:
#                     tab[k2_w][i][k1_w] = tab[k2_w][i - 1][k1_w]
                
#                 if weights[i - 1] <= k2_w:
#                     curr_max = tab[k2_w][i][k1_w]
#                     include_item_k2 = values[i - 1] + tab[k2_w - weights[i - 1]][i - 1][k1_w]
#                     tab[k2_w][i][k1_w] = max(curr_max, include_item_k2)

    
#   for plane in tab:
#     print("-")
#     for row in plane:
#         print(row)
#   return tab

# values = [10, 9, 15, 13]
# weights = [1, 2, 10, 1]
# n = len(values)
# capacity_1 = 3
# capacity_2 = 0
# dp = knapsack_tabulation()
# print(dp)
# print("\nMaximum value in Knapsack 1 and 2 =", dp[capacity_2][n][capacity_1])



# # print(items_used)
# # 2 knapsacks
# # idea: get the max value from the largest knapsack first
# # then find what items were used in largest
# # rerun algorithm with second knapsack and remaining items

# # def fill_knapsacks(weights, values, capacity1, capacity2):
# #     n = len(weights)

# #     # Initialize a 3D DP array with dimensions 
# #     # (n+1) x (w1+1) x (w2+1)
# #    





# #     # Fill the DP array iteratively
# #     for i in range(1, n + 1):
# #         weight = weights[i - 1]
# #         val = values[i - 1]

# #         for j in range(capacity1 + 1):
# #             for k in range(capacity2 + 1):

# #                 # Option 1: Don't take the current item
# #                 dp[i][j][k] = dp[i - 1][j][k]

# #                 # Option 2: Take the current item in the 
# #                 # first knapsack, if possible
# #                 if j >= weight:
# #                     dp[i][j][k] = max(dp[i][j][k], val +
# #                                       dp[i - 1][j - weight][k])

# #                 # Option 3: Take the current item in the 
# #                 # second knapsack, if possible
# #                 if k >= weight:
# #                     dp[i][j][k] = max(dp[i][j][k], val +
# #                                       dp[i - 1][j][k - weight])

# #     return dp


# # values = [10, 9, 15, 13]
# # weights = [1, 2, 10, 1]
# # # arr = [8, 2, 3]
# # capacity_1 = 5
# # capacity_2 = 2
# # dp = fill_knapsacks(weights, values, capacity_1, capacity_2)
# # for item in dp:
# #     print("--")
# #     for row in item:
# #         print(row)
# # # print(dp)
# # print(dp[len(weights)][capacity_1][capacity_2])

# # # recover items used
# # item = len(weights)
# # row = capacity_1
# # col = capacity_2
# # items_used = []

# # while item > 0:
# #     # val = dp[plane][row][col]
# #     # above_val = dp[plane][row - 1][col]
# #     # print(col, " ", val, " ", above_val)

# #     # if val != above_val:
# #     #     items_used.append(row)
# #     #     row -= weights[row - 1]
# #     # col -= 1
    
#     if col - weights[item - 1] >= 0 and dp[item][row][col] - dp[item][row - 1][col - weights[item - 1]] == values[item - 1]:
#         print(values[item - 1])
#     #    the element 'i' is in the knapsack
#     #   i += 1 # only in 0-1 knapsack
#         items_used.append(item)
        
#         # line = line - weights[i - 1]
#     # else: 
#     elif row - weights[item - 1] >= 0 and dp[item][row][col] - dp[item][row - weights[item - 1]][col - 1] == values[item - 1]:
#         print(values[item - 1])
#         items_used.append(item)
#     print("asjdhasjdn")
#     item -= 1 
