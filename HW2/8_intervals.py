
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

A = [[0, 1], [3, 4], [-1, 1]]

# TODO: sort the intervals by first: nlogn if done right:

A = [[-1, 1], [0, 1], [3, 5], [3, 4], [3, 6], [3, 5]]

# gather intervals contained in others
# if the first of next is > than the top of last, not contained
# if the last of next <= top of last, all good
# i think you have to check all of them

contained = []

curr_max = A[0][1] # 1
curr_min = A[0][0] # -1
curr = 0
# print(curr_max)

n = len(A)
next = 1
while next < n:
  # first = second - 1

  start = A[next][0]
  end = A[next][1]

  if start == curr_min:
    if curr_max > end: # larger of two intervals
      contained.append(A[next])
    else: # less than or equal
      contained.append(A[curr])
      curr = next # update interval bookmark
      curr_max = end # update curr_max to largest

  elif start > curr_min: # start is past the last starting interval, which is the only other case if sorted
    if end <= curr_max:
      contained.append(A[next])
    else:
      curr = next
      curr_min = start
      curr_max = end

  

  # if A[next][1] <= curr_max:
  #   contained.append(A[next])
  #   next += 1
  #   continue

  next += 1

  

print(contained)
