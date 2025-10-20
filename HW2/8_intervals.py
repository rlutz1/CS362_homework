
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