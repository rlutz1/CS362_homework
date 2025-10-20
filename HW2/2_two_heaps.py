def is_min_heap(heap, parent, n):
  if parent >= n: return True

  l_child = (2 * parent) + 1
  r_child = (2 * parent) + 2

  if l_child < n and heap[l_child] < heap [parent]:
    return False
  
  if r_child < n and heap[r_child] < heap [parent]:
    return False
  
  return is_min_heap(heap, l_child, n) and is_min_heap(heap, r_child, n)
  


def build_heap(heap):
  n = len(heap)
  if n != 0:
    start = (n // 2) - 1 # last parent node
    
    for i in range(start, -1, -1): # from last parent up to root
      heapify(heap, i, n)

    # return heap

def heapify(heap, parent, n):
  min = parent
  l_child = (2 * parent) + 1
  r_child = (2 * parent) + 2

  if l_child < n and heap[l_child] < heap[min]:
    min = l_child

  if r_child < n and heap[r_child] < heap[min]:
    min = r_child
  
  if min != parent:
    temp = heap[parent]
    heap[parent] = heap[min]
    heap[min] = temp

    heapify(heap, min, n)


# actual run of code

A = [10, 7, 6, 5, 4, 2, 3]
B = [6, 5, 1, 4, 3]

# first, concat A and B
C = A + B

print(C)

# then, build heap from C using sift up technique, O(m + n)
build_heap(C)

# run through test to ensure this is a proper heap
print(is_min_heap(C, 0, len(C)))
# print the heap
print(C)