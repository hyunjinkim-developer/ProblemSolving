"""
Problem:
https://www.testdome.com/questions/python/sorted-search/110599
less than: < (not containing the number)

Binary Search
"""

"""
# Solution 1:
from bisect import bisect_left

def count_numbers(sorted_list, less_than):
  return bisect_left(sorted_list, less_than)
"""


"""
# Solution 2:
# Implementation of bisect.bisect_left 
def count_numbers(sorted_list, less_than):
  low, high = 0, len(sorted_list) # mid should be calculated at least once

# Handling exceptions of empty sorted_list
#  if low < 0:
#    return -1

  while low < high:
    mid = (low + high) // 2
    print(low, high, "/", mid)
    if sorted_list[mid] < less_than:
      low = mid + 1
    else:
      high = mid
  return low
"""


"""
# Solution 3_Greedy:
"""
def count_numbers(sorted_list, less_than):
    # Handling exceptions of empty sorted_list
    if len(sorted_list) == 0:
        return -1

    left_idx, right_idx = 0, len(sorted_list) - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2

        if sorted_list[mid_idx] == less_than:
            return mid_idx

        elif sorted_list[mid_idx] < less_than:
            left_idx = mid_idx + 1

        else:
            right_idx = mid_idx - 1

    return left_idx


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4))  # should print 2
    print(count_numbers(sorted_list, 7))  # should print 3_Greedy