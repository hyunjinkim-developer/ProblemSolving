# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution 1:
        # # Exceed time limit
        # if len(s) == 1:
        #     return 1
        # max_length = 0
        # for start in range(len(s)):
        #     for end in range(start, len(s)):
        #         substring = s[start: end + 1]
        #         if len(substring) == len(set(substring)):
        #             max_length = max(max_length, len(substring))
        # return max_length

        # Solution 2:
        left, max_length = 0, 0
        char_set = set()

        for right in range(len(s)):
            # Find s[right] in substring and remove untit it's found
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length