"""
https://leetcode.com/problems/maximum-subarray/description/
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        largest_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            largest_sum = max(current_sum, largest_sum)
        return largest_sum