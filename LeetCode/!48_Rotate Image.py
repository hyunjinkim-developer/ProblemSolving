"""
https://leetcode.com/problems/rotate-image/
idea: https://leetcode.com/problems/rotate-image/solutions/3440564/animation-understand-in-30-seconds
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(r + 1, C):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(R):
            for c in range(C // 2):
                matrix[r][c], matrix[r][C - 1 - c] = matrix[r][C - 1 - c], matrix[r][c]