# Problem: https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        counts = [0] * (n + 1)
        counts[1] = 1
        counts[2] = 2
        for i in range(3, n + 1):
            counts[i] = counts[i - 1] + counts[i - 2]
        return counts[n]