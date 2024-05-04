# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Max, Min 값을 구하는 문제에서 default 값을 정할 때 문제의 조건을 반드시 확인할 것!


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def calculate_sum(arr, start_r, start_c):
    sum_ = 0

    hourglass_flag = [[1] * 3 for _ in range(3)]
    hourglass_flag[1][0] = 0
    hourglass_flag[1][2] = 0

    for r in range(3):
        for c in range(3):
            sum_ += hourglass_flag[r][c] * arr[start_r + r][start_c + c]
    return sum_


def hourglassSum(arr):
    R, C = len(arr), len(arr[0])
    max_sum = -9 * R * C
    for r in range(0, R - 2):
        for c in range(0, C - 2):
            max_sum = max(max_sum, calculate_sum(arr, r, c))
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
