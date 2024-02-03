"""
Problem:
https://www.testdome.com/questions/python/two-sum/94858

# Dictionary (Map)
"""

from collections import defaultdict

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    number_dict = defaultdict(list)
    for idx, num in enumerate(numbers):
        number_dict[num].append(idx)

    for idx, num in enumerate(numbers):
        matched_pair = target_sum - num
        if matched_pair in number_dict:
            matched_index_list = number_dict[matched_pair]

            # Duplicate numbers with and without solutions:
            for available_index in matched_index_list:
                if idx != available_index:
                    return (idx, available_index)
    return None


if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))