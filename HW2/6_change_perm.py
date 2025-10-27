# illustration of linear time solution to #6



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

# n = len(o)
# i = 0

# for order in o:
#   o[i] = A[order]
#   i += 1
  
#   j = n
#   while j > 1:
#     print("Filler loop to meet theta req.")
#     j = j // 2

# print(o)


# assume we are getting one indexing
def reorder(o):
  n = len(o)

  # convert to zero index because i just can't anymore
  # for i in range(0, n):
  #   o[i] -= 1 

  # for i in range(n):
  #   o[i] *= -1 # make them all negative

  for current_position in range(0, n):
    print(o)
    print(current_position)
    element_index = o[current_position]
    # print("order ", order)

    # if this is already negative, continue on
    if element_index < 0:
      continue

    

    # get the element number at the position we need to swap with
    element_at_needed_position = o[element_index - 1] # this will be 1 indexed
    # print("temp ", temp)

     # if the element number there is positive/not swapped yet
    if element_at_needed_position > 0:
      # if the element number over that element is the correct ordering
      if element_at_needed_position == current_position + 1:
        print("skjdhajksd ", current_position + 1)
        o[current_position] = (-1) * o[current_position] # make it negative, unchanged
        # o[element_index - 1] = (-1) * o[element_index - 1] # make it negative unchanged
        continue
      
      # general case, we need to change the element number at current position to the neg curr position
      o[element_index - 1] = (-1) * (current_position + 1) 
      print(o)
      # we need to also set the element at needed position to the position being replaced
      temp = o[element_at_needed_position - 1]
      o[element_at_needed_position - 1] = (-1) * element_index
      print(o)
      # last, 3rd step
      o[current_position] = (-1) * element_at_needed_position
      print(o)
    else: 
       o[current_position] = (-1) * o[current_position] # make it negative, unchanged
    
    


    
def heapify(heap, permutation, parent, n):
  min = parent
  l_child = (2 * parent) + 1
  r_child = (2 * parent) + 2

  if l_child < n and permutation[l_child] < permutation[min]:
    min = l_child

  if r_child < n and permutation[r_child] < permutation[min]:
    min = r_child
  
  if min != parent:
    # swap the original array elements
    temp = heap[parent]
    heap[parent] = heap[min]
    heap[min] = temp
    # swap the permutation elements likewise
    temp = permutation[parent]
    permutation[parent] = permutation[min]
    permutation[min] = temp

    # print(A)
    # print(o)
    heapify(heap, permutation, min, n)

# Main function to do heap sort
def heap_sort(A, o):
    n = len(A)
    if n > 0:
      # heap it up
      start = (n // 2) - 1 # last parent node
      
      for i in range(start, -1, -1): # from last parent up to root
        heapify(A, o, i, n)

      print("done with heapify")
      print(A)
      print(o)
      # one by one extract an element from heap
      for i in range(n - 1, -1, -1):

          # Move current root to end
          A[0], A[i] = A[i], A[0]
          o[0], o[i] = o[i], o[0]
          print("post swap")
          print(A)
          print(o)
          # Call max heapify on the reduced heap
          heapify(A, o, 0, i)
          print("post heapify 2")
          print(A)
          print(o)


 




# o = [3, 4, 2, 1]
# o = [2, 3, 1]
# o = [1, 2, 3]
# A = [10.5, 9.3, 2.7, 13.6] # working
# o = [4, 2, 3, 1]
A = ['A', 'B', 'C', 'D', 'E']
test_A = ['A', 'B', 'C', 'D', 'E']

# o = [1, 2, 3, 4] # unchanged
# test_o = [1, 2, 3, 4]
# o = [1, 4, 3, 2] # ADCB
# test_o = [1, 4, 3, 2]

# o = [1, 4, 2, 3] # ADBC
# test_o = [1, 4, 2, 3]

o = [5, 2, 1, 4, 3] # EBADC
test_o = [5, 2, 1, 4, 3]

# o = [1, 2, 3] # A B C
# test_o = [1, 2, 3]

# o = [1, 3, 2] # A C B
# test_o = [1, 3, 2]

# o = [2, 1, 3] # B A C
# test_o = [2, 1, 3]

# o = [2, 3, 1] # B C A # these are swapped for some reason
# test_o = [2, 3, 1]

# o = [3, 1, 2] # C A B
# test_o = [3, 1, 2]

# o = [3, 2, 1] # C B A
# test_o = [3, 2, 1]

print(o)
print(A)
# print()
reorder(o)
print("reordering o")
print(o)
heap_sort(A, o)
print("REORDERED")
print(A)



i = 0
for order in test_o:
  test_o[i] = test_A[order - 1]
  i += 1

print(test_o)

