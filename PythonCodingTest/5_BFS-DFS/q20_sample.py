"""
Problem: https://www.acmicpc.net/problem/18428
- 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력
- input:
    - 각 행에서는 N개의 원소가 공백을 기준으로 구분되어 주어진다. (3 ≤ N ≤ 6)
    - 해당 위치에 학생이 있다면 S
    - 선생님이 있다면 T
    - 아무것도 존재하지 않는다면 X

Solution:
    장애물 을 정확히 3개 설치하는 모든 조합의 수는 최악의 경우 36C3이 될 것이다.
    이는 10 ^ 4 이하의 수이므로 모든 조합을 고려하여 완전 탐색을 수행해도 시간 초과 없이 문제를 해결할 수 있다
"""

from itertools import combinations

N = 0
board, teachers = list(), list()
spaces = list()
answer = False

def get_input():
    global N, board
    global teachers, spaces, answer

    # Initialization
    board = list()
    teachers = list()
    spaces = list()
    answer = False

    N = int(input())
    for r in range(N):
        board.append(list(input().split()))
        for c in range(N):
            # Save teachers' location
            if board[r][c] == "T":
                teachers.append((r, c))
            # Save empty spaces
            if board[r][c] == "X":
                spaces.append((r, c))

def set_barrier():
    global board, spaces, answer

    for barriers in combinations(spaces, 3):
        # Set barriers
        for (r, c) in barriers:
            board[r][c] = "B"
        if avoid_teachers():
            answer = True
            break
        # Remove barriers
        for (r, c) in barriers:
            board[r][c] = "X"

def avoid_teachers():
    global N, board, teachers

    def student_found(r, c):
        # left
        c_left = c
        while 0 <= c_left:
            if board[r][c_left] == "B":
                break
            if board[r][c_left] == "S":
                return True
            c_left -= 1
        # right
        c_right = c
        while c_right < N:
            if board[r][c_right] == "B":
                break
            if board[r][c_right] == "S":
                return True
            c_right += 1
        # up
        r_up = r
        while 0 <= r_up:
            if board[r_up][c] == "B":
                break
            if board[r_up][c] == "S":
                return True
            r_up -= 1
        # down
        r_down = r
        while r_down < N:
            if board[r_down][c] == "B":
                break
            if board[r_down][c] == "S":
                return True
            r_down += 1
        # Students not found
        return False

    for (r, c) in teachers:
        if student_found(r, c):
            return False
    return True


def main():
    get_input()
    set_barrier()

    if answer == True:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    test_case_count = int(input())
    for test_case in range(1, test_case_count + 1):
        print(f"test case: {test_case}", "=" * 30)
        print(main())