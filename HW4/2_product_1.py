# kk, so i might be dumb, but i think this works?
# just need a little bookeeping...

# why this fails: REAL NUMBERS.
# 2 * 1/2 is allowed!! this would work if it was limited to integers only.

def product_1_ints(A):
  one_one_found = False
  one_neg_one_found = False

  for a in A:
    if a == 1 and not one_one_found:
      one_one_found = True
    elif a == 1 and one_one_found:
      return True
    elif a == -1 and not one_neg_one_found:
      one_neg_one_found = True
    elif a == -1 and one_neg_one_found:
      return True

  return False

def product_1_reals(A, n):
  list.sort(A) # O(nlogn) sort
  print(A)
  # search for the reciprocal of each number 
  for i in range(n - 1, 0, -1): # from back to front, O(nlogn) searches
    key = A[i] # key for binary search
    if key != 0: # no division by 0 please and thank you
      target = (1 / key) # target we're looking for, key * inverse_key = 1
      
      left = 0
      right = i - 1
 
      while left <= right:
        mid = (left + right) // 2
        if target == A[mid]:
          print(key, " * ",  A[mid], " = 1, ", mid, " ", i)
          return True
        elif target < A[mid]:
          right = mid - 1
        else:
          left = mid + 1
  return False

def product_1_with_hash(A, n):
  H = set() # empty hash set
  for key in A:
    if ((1 / key) in H):
      return True
    H.add(key)
  return False




A = [(1/3), 1.3, 1, -20, 25000, 3.1416, 3,  -1] # true
print(product_1_with_hash(A, len(A)))

A = [(1/3), 1.3, 1, -20, 25000, 3.1416, -1] # false
print(product_1_with_hash(A, len(A)))

A = [(1/3), 1.3, -1, -20, 25000, 3.1416, -1] # true
print(product_1_with_hash(A, len(A)))

A = [(1/3), 1.3, 1, -20, 25000, 3.1416] # false
print(product_1_with_hash(A, len(A)))

A = [(1/3), 1.3, 1, -20, 25000, 0.5, -2, 3.1416] # false
print(product_1_with_hash(A, len(A)))

A = [(1/3), 1.3, 1, -20, 25000, -0.5, -2, 3.1416] # true
print(product_1_with_hash(A, len(A)))


# A = [(1/3), 1.3, 1, -20, 25000, 3.1416, 3,  -1] # true
# print(product_1_reals(A, len(A)))

# A = [(1/3), 1.3, 1, -20, 25000, 3.1416, -1] # false
# print(product_1_reals(A, len(A)))

# A = [(1/3), 1.3, -1, -20, 25000, 3.1416, -1] # true
# print(product_1_reals(A, len(A)))

# A = [(1/3), 1.3, 1, -20, 25000, 3.1416] # false
# print(product_1_reals(A, len(A)))

# A = [(1/3), 1.3, 1, -20, 25000, 0.5, -2, 3.1416] # false
# print(product_1_reals(A, len(A)))

# A = [(1/3), 1.3, 1, -20, 25000, -0.5, -2, 3.1416] # true
# print(product_1_reals(A, len(A)))



# A = [1.3, 1, -20, 25000, 3.1416, -1] # false
# print(product_1_ints(A))

# A = [1.3, -1, -20, 25000, 3.1416, 1] # false
# print(product_1_ints(A))

# A = [1.3, 1, -20, 25000, 3.1416] # false
# print(product_1_ints(A))

# A = [1.3, -20, 25000, 3.1416, -1] # false
# print(product_1_ints(A))

# A = [1.3, -1, -20, 25000, 3.1416, -1, 1] # true
# print(product_1_ints(A)) 
    
# A = [1.3, 1, -20, 25000, -3.1416, 1, -1] # true
# print(product_1_ints(A)) 

# A = [1.3, -20, 25000, 3.1416] # false
# print(product_1_ints(A)) 
