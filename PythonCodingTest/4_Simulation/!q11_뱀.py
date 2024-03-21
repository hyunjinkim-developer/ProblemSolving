# """
# Solution 1:
from collections import deque

N = 0
apple_location = deque()
redirection = dict()
DEBUG = False #debug

#debug
def print_snake(snake):
    global N, apple_location

    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for r, c in apple_location:
        graph[r][c] = "A"

    for idx, (r, c) in enumerate(snake):
        if idx == 0:
            graph[r][c] = "H"
        elif idx == len(snake) - 1:
            graph[r][c] = "T"
        else:
            graph[r][c] = "*"

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            print(graph[row][col], end='\t')
        print()

def get_input():
    global N, apple_location, redirection

    # Initialization
    N = 0
    apple_location = deque()
    redirection = dict()

    N = int(input())

    K = int(input())
    for _ in range(K):
        row, col = map(int, input().split())
        apple_location.append((row, col))

    L = int(input())
    for _ in range(L):
        X, C = input().split()
        redirection[int(X)] = C

def run_dummy():
    running_time = 0
    global N, apple_location, redirection

    # From right in clockwise
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def in_range(r, c):
        return 1 <= r < N + 1 and 1 <= c < N + 1 # upper left corner: (1, 1)

    # Initialize the snake
    start_row, start_col= 1, 1
    # start_direction = 0, 1
    start_direction = 0
    snake = deque([(start_row, start_col)])

    r, c = start_row, start_col
    d = start_direction
    while True:
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc

        # 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝납니다.
        if not in_range(nr, nc) or (nr, nc) in snake:
            running_time += 1
            break

        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
        if (nr, nc) in apple_location:
            snake.appendleft((nr, nc))
            apple_location.remove((nr, nc))
        # 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다.
        else:
            snake.appendleft((nr, nc))
            snake.pop()
        # End game for of running_time second

        r, c = nr, nc
        running_time += 1
        if running_time in redirection:
            change_direction = redirection[running_time]
            # 왼쪽(C가 ‘L’) 또는 오른쪽(C가 ‘D’)으로 90도 방향을 회전
            if change_direction == "L":
                d = (d - 1) % 4
            elif change_direction == "D":
                d = (d + 1) % 4

            #debug
            if DEBUG == True:
                print(f"change direction {change_direction}: {d}", "*"*20)
        if DEBUG == True:
            print(f"running time: {running_time}")  # d
            print(f"direction: {d}")
            print(f"nr, nc: {nr, nc}")  # d
            print_snake(snake)
            print("-"*10)

    return running_time

def main():
    get_input()
    print(run_dummy())
# """


"""
# Solution 2: Sample solution
N = 0
graph = []
redirections = []

DEBUG = False #debug

#debug
def print_snake(graph):
    global N

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            print(graph[row][col], end='\t')
        print()

def get_input():
    global N, graph, redirections
    # Initialization
    N, graph, redirections = 0, [], []

    N = int(input())
    graph = [[0] * (N + 1) for _ in range(N + 1)]

    # apples
    K = int(input())
    for _ in range(K):
        r, c = map(int, input().split())
        graph[r][c] = 1 # graph value of 1: apple

    L = int(input())
    for _ in range(L):
        X, C = input().split()
        redirections.append((int(X), C))

def turn(direction_idx, C):
    if C == "L":
        direction_idx = (direction_idx - 1) % 4
    elif C == "D":
        direction_idx = (direction_idx + 1) % 4
    return direction_idx

def simulate():
    global N, graph, redirections
    time = 0

    start_direction = 0
    start_row, start_col = 1, 1
    graph[start_row][start_row] = 2  # graph value of 2: snake

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def in_range(r, c):
        return 1 <= r <= N and 1 <= c <= N

    snake = [(start_row, start_col)]  # index 0: Tail/ last index: Head
    d = start_direction
    r, c = start_row, start_col
    redirection_idx = 0
    while True:
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and graph[nr][nc] != 2:
            # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
            if graph[nr][nc] == 1:
                graph[nr][nc] = 2
                snake.append((nr, nc))

            # 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다.
            if graph[nr][nc] == 0:
                # Add head
                graph[nr][nc] = 2
                snake.append((nr, nc))
                # Remove tail
                prev_tail_r, prev_tail_c = snake.pop(0)
                graph[prev_tail_r][prev_tail_c] = 0
        else: # 뱀이 맵을 벗어나거나 뱀이 자기 자신과 부딪힌 경우
            time += 1
            break

        r, c = nr, nc # 다음 위치로 머리 이동
        time += 1
        # if statement runs from left to right
        # Condition redirection_idx < len(redirections) is False, rest conditions will not run
        if redirection_idx < len(redirections) and time == redirections[redirection_idx][0]: # 1 <= L <= 100
            d = turn(d, redirections[redirection_idx][1])
            redirection_idx += 1

        #debug
        if DEBUG == True:
            print(f"time: {time}")
            print_snake(graph)
    return time

def main():
    get_input()
    print(simulate())
"""


# Get input automatically
import sys
sys.stdin = open("q11.txt", "r")
# Test case cateory:
# 1: 벽과 부딪힘
# 2: 벽과 부딪힘
# 3: 자기 자신과 부딪힘

if __name__ == "__main__":
    # if __name__ == "__main__": can access global variable without defining keyword global
    # global DEBUG # Should NOT use like this
    # When run the code above, SyntaxError: name 'DEBUG' is assigned to before global declaration

    T = int(input())
    for test_case in range(1, T + 1):
        # Run all test cases
        DEBUG = False
        print(f"test case: {test_case}", "=" * 30)
        main()

        # #debug
        # DEBUG = True
        # if test_case == 2:
        #     print(f"test case: {test_case}", "="*30)
        #     main()
        # else:
        #     get_input()
