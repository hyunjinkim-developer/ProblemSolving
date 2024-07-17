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
        # Use two pointers, left and right,
        #   to represent the boundaries of the current substring.
        left, max_length = 0, 0
        char_set = set()

        for right in range(len(s)):
            # If the character is already present in the set,
            #   it indicates a repeating character within the current substring.
            while s[right] in char_set:
                # Move the left pointer forward,
                #   removing characters from the set until the repeating character is no longer present.
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length


        # # Solution 3:
        # # Handling exceptions: "c", " ", "au"
        # if (not s.isalpha()) or (len(s) in [1, 2]):
        #     return len(set(s))
        #
        # substring = set()
        #
        # for start in range(len(s)):
        #     for end in range(start + 1, len(s) + 1):
        #         # if not string with unique characters
        #         if len(set(s[start: end])) != len(s[start: end]): continue
        #
        #         if len(substring) < len(set(s[start: end])):
        #             substring = s[start: end]
        #             # print(start, end, s[start :end])
        #
        # return len(substring)

