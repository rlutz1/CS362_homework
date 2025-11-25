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
