"""
# Soltuion 1:
from copy import deepcopy

N = 0

def get_input():
    global N
    N = int(input())
    triangle = []
    for i in range(N):
        triangle.append(list(map(int, input().split())))
    return triangle

def tree_traversal(triangle):
    dp_table = deepcopy(triangle)

    for row in range(1, N):
        for col in range(len(triangle[row])):
            if col == 0:
                dp_table[row][col] = dp_table[row - 1][col] + triangle[row][col]
            elif col == row:
                dp_table[row][col] = dp_table[row - 1][col - 1] + triangle[row][col]
            else:
                dp_table[row][col] = max(dp_table[row - 1][col - 1], dp_table[row - 1][col]) + triangle[row][col]
    return max(dp_table[-1])

def main():
    triangle = get_input()

    answer = tree_traversal(triangle)
    return answer
"""


# Solution2: Sample Solution
N = 0
dp_table = []

def get_input():
    global N
    N = int(input())
    for _ in range(N):
        dp_table.append(list(map(int, input().split())))

def tree_traversal():
    for row in range(1, N):
        for col in range(row + 1):
            # Coming to the first element of the row
            if col == 0:
                upper_left = 0
            else:
                upper_left = dp_table[row - 1][col - 1]
            # Coming to the last element of the row
            if row == col:
                upper_right = 0
            else:
                upper_right = dp_table[row - 1][col]
            dp_table[row][col] = dp_table[row][col] + max(upper_left, upper_right)
    return max(dp_table[N - 1])

def main():
    get_input()
    answer = tree_traversal()
    return answer


if __name__ == "__main__":
    print(main())