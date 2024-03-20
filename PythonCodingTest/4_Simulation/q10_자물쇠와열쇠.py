"""
Problem: https://programmers.co.kr/learn/courses/30/lessons/60059
"""

"""
# Solution 1:
# Time complexity: O(9 * N^2) ~ O(N^2)
#     condition: M <= N
#     assume M == N
#
#     Time complexity for each function:
#     extend_lock(): O(N^2)
#     rotate(): O(M^2) ~ in maximum O(N^2)
#     put_key_into_lock(): O(M^2) ~ in maximum O(N^2)
#     remove_key_from_lock(): O(M^2) ~ in maximum O(N^2)
#     check_fit(): O(N^2)
#     match(): O((2 * N)^2) ~ O(4 * N^2)

M, N = 0, 0

# debug
def print_matrix(matrix):
    L = len(matrix)
    for row in range(L):
        print(matrix[row])

def extend_lock(lock):
    global N

    extended_lock = [[1] * (3 * N) for _ in range(3 * N)]
    for row in range(N):
        for col in range(N):
            new_row, new_col = row + N, col + N
            extended_lock[new_row][new_col] = lock[row][col]
    return extended_lock

def rotate(key):
    global M

    # r' = c
    # c' = (M - 1) - r
    rotated_key = [[0] * M for _ in range(M)]
    for row in range(M):
        for col in range(M):
            rotated_key[col][M - 1 - row] = key[row][col]
    return rotated_key

def put_key_into_lock(key, extended_lock, start_row, start_col):
    global M

    for r in range(M):
        for c in range(M):
            row, col = start_row + r, start_col + c
            extended_lock[row][col] += key[r][c]
    return extended_lock

def remove_key_from_lock(key, extended_lock, start_row, start_col):
    global M

    for r in range(M):
        for c in range(M):
            row, col = start_row + r, start_col + c
            extended_lock[row][col] -= key[r][c]
    return extended_lock

def check_fit(extended_lock):
    global N

    fit = 0
    for row in range(N, 2 * N):
        for col in range(N, 2 * N):
            if extended_lock[row][col] == 1:
                fit += 1
    if fit == N * N:
        return True
    else:
        return False

def match(key, extended_lock):
    global M, N
    matched = False

    for key_start_row in range(2 * N):
        for key_start_col in range(2 * N):
            extended_lock = put_key_into_lock(key, extended_lock, key_start_row, key_start_col)
            matched = check_fit(extended_lock)
            if matched == True:
                return True
            extended_lock = remove_key_from_lock(key, extended_lock, key_start_row, key_start_col)
    return False

def solution(key, lock):
    answer = True

    global M, N
    M, N = len(key), len(lock)

    extended_lock = extend_lock(lock)
    for _ in range(4):
        key = rotate(key)
        answer = match(key, extended_lock)
    return answer
"""

# Solution 2: Smaple solution
M, N = 0, 0

def extend_lock(lock):
    global N

    extended_lock = [[0] * (3 * N) for _ in range(3 * N)]
    for row in range(N):
        for col in range(N):
            extended_lock[N + row][N + col] = lock[row][col]
    return extended_lock

def rotate_key_by_90_degree(key):
    global M, N

    rotated_key = [[0] * M for _ in range(M)]
    for row in range(M):
        for col in range(M):
            rotated_key[col][(M - 1) - row] = key[row][col]
    return rotated_key

def fit_key_in_lock(key, extended_lock, key_start_row, key_start_col):
    global M

    for row in range(M):
        for col in range(M):
            extended_lock[key_start_row + row][key_start_col + col] += key[row][col]
    return extended_lock

def unfit_key_in_lock(key, extended_lock, key_start_row, key_start_col):
    global M

    for row in range(M):
        for col in range(M):
            extended_lock[key_start_row + row][key_start_col + col] -= key[row][col]
    return extended_lock

def check_fit(extended_lock):
    global N

    count_fit = 0
    for row in range(N, 2 * N):
        for col in range(N, 2 * N):
            if extended_lock[row][col] != 1:
                return False # More efficient than Solution 1
    return True


def solution(key, lock):
    answer = False
    global M, N
    M, N = len(key), len(lock)

    extended_lock = extend_lock(lock)
    for _ in range(4):
        key = rotate_key_by_90_degree(key)
        for key_start_row in range(2 * N):
            for key_start_col in range(2 * N):
                extended_lock = fit_key_in_lock(key, extended_lock, key_start_row, key_start_col)
                answer = check_fit(extended_lock)
                if answer == True:
                    return answer
                extended_lock = unfit_key_in_lock(key, extended_lock, key_start_row, key_start_col)
    return answer