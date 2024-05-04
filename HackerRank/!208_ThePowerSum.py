# Problem : https://www.hackerrank.com/challenges/the-power-sum/problem?isFullScreen=true
# Reference : https://youtu.be/AIw5ljcTuyg?si=-G_BHqa9yrrWaITy

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N

def calculate(selected):
    result = 0
    for num in selected:
        result += (num ** 2)
    return result


def powerSum(X, N):
    def recursive(total, power, num):
        value = total - (num ** power)
        # Base condition
        if value == 0:
            return 1
        if value < 0:
            return 0

        # Recursive call
        return recursive(value, power, num + 1) + recursive(total, power, num + 1)

    return recursive(X, N, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
