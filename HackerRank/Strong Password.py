#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    checked = [False] * 4
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    for c in password:
        if c in numbers:
            checked[0] = True
        if c in lower_case:
            checked[1] = True
        if c in upper_case:
            checked[2] = True
        if c in special_characters:
            checked[3] = True

    min_num = 6 - n
    min_num = max(min_num, 4 - sum(checked))
    return min_num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()