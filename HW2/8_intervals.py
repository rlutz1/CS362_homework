
# Example:
# Consider the following set of intervals: [[1, 8], [2, 5], [3, 7], [6, 9], [4, 6]] sorted intervals.
# [[1, 8], [2, 5], [3, 7], [4, 6], [6, 9]] (Note: [2,5] comes before [3,7] because 2 < 3. [4,6] comes before [6,9] because 4 < 6.) 

#     Iteration:
#         Interval: max_end is initially -infinity. 8 > -infinity. Update max_end = 8.
#         Interval: 5 <= 8. [2, 5] is contained. Add [2, 5] to contained list. max_end remains 8.
#         Interval: 7 <= 8. [3, 7] is contained. Add [3, 7] to contained list. max_end remains 8.
#         Interval: 6 <= 8. [4, 6] is contained. Add [4, 6] to contained list. max_end remains 8.
#         Interval: 9 > 8. [6, 9] is not contained by any previous interval that set max_end. Update max_end = 9. 
#     Result: The identified contained intervals are [[2, 5], [3, 7], [4, 6]]. 


#  BECAUSE I AM SO LOST IN THE KNAPSACK SAUCE



# TODO: sort the intervals by first: nlogn if done right:

def merge_sort(A, start, end):
  if start >= end:
    return
  
  mid = (start + end) // 2

  merge_sort(A, start, mid)
  merge_sort(A, mid + 1, end)
  merge(A, start, mid, end)

def merge(A, start, mid, end):
    i = 0
    j = 0
    length_left = mid - start + 1
    length_right = end - mid
    k = start
    L = [0] * length_left
    R = [0] * length_right
    # if s1 == s2: print("dumb")

    for e in range(length_left):
       L[e] = A[start + e]

    for f in range(length_right):
       R[f] = A[mid + 1 + f]
    # print(L, R)

    # length_left = mid - start
    # length_right = end - mid


    while i < length_left and j < length_right:
        if L[i][0] < R[j][0]:
            A[k] = L[i]
            i += 1
            
        else:
            A[k] = R[j]
            j += 1

        k += 1


    while i < length_left:
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < length_right:
        A[k] = R[j]
        j += 1
        k += 1
    # print(A)

# B = [6, 7, 2, -1, 9] # sort test
# merge_sort(B, 0, len(B) - 1)
# print(B)




# A = [[-1, 1], [0, 1], [3, 5], [3, 4], [3, 6], [3, 5]]

# gather intervals contained in others
# if the first of next is > than the top of last, not contained
# if the last of next <= top of last, all good
# i think you have to check all of them


def contained_intervals(A, n):
  if n > 0:
    # print(A) # unsorted

    merge_sort(A, 0, len(A) - 1) # sort by start of interval

    # print(A) # sorted by first value

    contained = []

    # init values, assume this is best
    curr_max = A[0][1] # 1
    curr_min = A[0][0] # -1
    curr = 0
    # print(curr_max)

    next = 1 # next value

    while next < n:
      # first = second - 1

      start = A[next][0] # start and end of next interval
      end = A[next][1]

      if start == curr_min: # if they start at same spot
        if curr_max > end: # if current is larger of two intervals
          contained.append(A[next]) # save the next interval
        else: # less than or equal
          contained.append(A[curr]) # save the current -- it's the smaller interval
          curr = next # update interval bookmark to larger
          curr_max = end # update curr_max to largest

      else: # start is past the last starting interval, which is the only other case once sorted
        if end <= curr_max: # if the end interval is less than or equal to the current max, it is contained
          contained.append(A[next])
        else: # this is the next interval to compare other intervals with
          curr = next
          curr_min = start
          curr_max = end

      next += 1 # progress linearly through the array
  
    return contained


# A = [[3, 4], [0, 1], [3, 6], [2, 4], [1, 2], [3, 5]]
A = [[-1, 1], [0, 1], [3, 4], [3, 6]]
# A = []
print(contained_intervals(A, len(A)))
    

# print(contained)
