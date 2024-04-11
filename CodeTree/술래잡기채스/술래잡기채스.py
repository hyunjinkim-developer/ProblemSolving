"""
# Solution 1:
# Save location of each runner in dictionary to acces in O(1)


answer = 0
N = 4
graph = [
    [(0, 0) for _ in range(4)]
    for _ in range(4)
]
SEEKER = (-2, -2)
VACANT = (-1, -1)
runner_location = dict() # Acces runner's location in O(1)
# 방향 d는 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
d_to_direction = {0: (-1, 0),
                 1: (-1, -1),
                 2: (0, -1),
                 3: (1, -1),
                 4: (1, 0),
                 5: (1, 1),
                 6: (0, 1),
                 7: (-1, 1)}

# #debug
# def print_matrix(matrix):
#     global VACANT, SEEKER
#     for x in range(4):
#         for y in range(4):
#             if (matrix[x][y] == VACANT) or (matrix[x][y] == SEEKER):
#                 print(matrix[x][y], end='\t')
#             else:
#                 idx, d = matrix[x][y]
#                 dir = d_to_direction[d]
#                 print(idx, dir, end='\t')
#         print()
#
# def print_dict(dictionary):
#     global N
#     for i in range(1, len(dictionary) + 1):
#         print(i, dictionary[i])

def get_input():
    global answer, N, graph, runner_location

    # Initialization
    answer = 0
    graph = [
        [(0, 0) for _ in range(N)]
        for _ in range(N)
    ]

    for x in range(N):
        data = list(map(int, input().split()))
        for i in range(N):
            y = i
            runner_idx = data[2 * i]
            d = data[2 * i + 1] - 1
            graph[x][y] = (runner_idx, d)
            runner_location[runner_idx] = (x, y)


def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def move_runner(runner_idx):
    global runner_location, d_to_direction, SEEKER, VACANT

    runner_x, runner_y = runner_location[runner_idx]
    _, d_idx = graph[runner_x][runner_y]

    # 도둑 말은 이동할 수 있을 때까지 45도 반시계 회전하며 갈 수 있는 칸을 탐색
    for i in range(8):
        d = (d_idx + i) % 8
        dx, dy = d_to_direction[d]
        nx, ny = runner_x + dx, runner_y + dy

        # 술래말이 있는 칸이나 격자를 벗어나는 곳으로는 이동할 수 없습니다
        if not in_range(nx, ny): continue
        if graph[nx][ny] == SEEKER: continue

        # 빈 칸이나 다른 도둑말이 있는 칸은 이동할 수 있는 칸
        # 해당 칸에 다른 도둑말이 있다면 해당 말과 위치를 바꿉니다
        if graph[nx][ny] != VACANT:
            swapped_runner_idx, _ = graph[nx][ny]
            runner_location[swapped_runner_idx] = (runner_x, runner_y)
        runner_location[runner_idx] = (nx, ny)

        graph[runner_x][runner_y] = (runner_idx, d) # Change current runner's direction
        graph[runner_x][runner_y], graph[nx][ny] = graph[nx][ny], graph[runner_x][runner_y]
        break

def runner_turn():
    global N, graph, runner_location, SEEKER

    def runner_can_move(x, y):
        return in_range(x, y) and graph[x][y] != SEEKER

    # 도둑말은 번호가 작은 순서대로 본인이 가지고 있는 이동 방향대로 이동
    for runner_idx in range(1, N * N + 1):
        # caught runner
        if runner_location[runner_idx] == -1: continue

        move_runner(runner_idx)


def search_max_score(seeker_x, seeker_y, d, score):
    global answer, N, graph, runner_location, d_to_direction
    seeker_dx, seeker_dy = d_to_direction[d]

    def seeker_can_move(x, y):
        return in_range(x, y) and graph[x][y] != (-1, -1) # Seeker cannot move to vacant space

    def done_traversal(seeker_x, seeker_y, seeker_dx, seeker_dy):
        # 현재 위치에도 한 곳이라도 갈 수 있는지 확인합니다.
        # 존재한다면, 아직 게임은 끝나지 않았습니다.
        for distance in range(1, N + 1):
            nx, ny = seeker_x + distance * seeker_dx, seeker_y + distance * seeker_dy
            if seeker_can_move(nx, ny):
                return False
        return True

    if done_traversal(seeker_x, seeker_y, seeker_dx, seeker_dy):
        answer = max(answer, score)
        return

    # 현재 턴에 움직일 수 있는 곳을 전부 탐색합니다.
    for distance in range(1, N + 1):
        nx, ny = seeker_x + distance * seeker_dx, seeker_y + distance * seeker_dy
        if not seeker_can_move(nx, ny): continue

        # 더 탐색을 진행한 이후, 초기 상태로 다시 만들기 위해
        # save_data 배열에 현재 board 상태를 저장해놓습니다.
        save_data = [
            [graph[x][y] for y in range(N)]
            for x in range(N)
        ]

        # 해당 위치의 도둑말을 잡고
        extra_score, next_dir = graph[nx][ny]
        runner_location[extra_score] = -1
        graph[nx][ny], graph[seeker_x][seeker_y] = SEEKER, VACANT
        # 모든 도둑말을 움직입니다.
        runner_turn()
        # 그 다음 탐색을 진행합니다.
        search_max_score(nx, ny, next_dir, score + extra_score)

        # 선택한 위치에서의 최대 score 계산 후, graph, runner_location를 원래 상태로 복원
        for i in range(N):
            for j in range(N):
                graph[i][j] = save_data[i][j]
        for x in range(N):
            for y in range(N):
                runner_idx, d = graph[x][y]
                if (runner_idx, d) != SEEKER and (runner_idx, d) != VACANT:
                    runner_location[runner_idx] = (x, y)


def main():
    global answer, graph, runner_location

    get_input()

    # 1. 초기에는 (0, 0)에 있는 도둑말을 잡으며 시작
    init_score, init_dir = graph[0][0]
    answer += init_score
    graph[0][0] = SEEKER
    runner_location[init_score] = -1

    runner_turn()
    # 술래말이 이동할 수 있는 곳에 도둑말이 더이상 존재하지 않으면 게임을 끝냅니다
    search_max_score(0, 0, init_dir, answer)
    print(answer)
'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

# test case answer
# 21
# 1
# 45

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    main()

    # # debug
    # print(f"Test case: {test_case}", "="*30)
    # if test_case == 3:
    #     main()
    # else:
    #     get_input()
    # ///////////////////////////////////////////////////////////////////////////////////
"""






# Solution 2:
# Using only 2-dimensional array,
# whose row(x) and column(y) represents each runner's location
#   Saved data represents (each runner's index, direction(d))
# Use dictionary to access user's location in O(1)
# Time consuming bug:
#   Be careful with the iterator name! Should be different from other variables

# Global variables
max_score = 0

N = 4
graph = [
    [(0, 0) for _ in range(N)]
    for _ in range(N)
]

SEEKER = (-2, -2)
VACANT = (-1, -1)

# 문제에서 주어진 순서대로
# 방향을 정의합니다.
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]


#debug
d_to_direction = {0: (-1, 0),
                      1: (-1, -1),
                      2: (0, -1),
                      3: (1, -1),
                      4: (1, 0),
                      5: (1, 1),
                      6: (0, 1),
                      7: (-1, 1)}
def print_matrix(matrix):
    global VACANT, SEEKER, d_to_direction

    for x in range(4):
        for y in range(4):
            if (matrix[x][y] == VACANT) or (matrix[x][y] == SEEKER):
                print(matrix[x][y], end='\t')
            else:
                idx, d = matrix[x][y]
                dir = d_to_direction[d]
                print(idx, dir, end='\t')
        print()



def get_input():
    global max_score, N, graph

    # Initiization
    max_score = 0
    graph = [
        [(0, 0) for _ in range(N)]
        for _ in range(N)
    ]

    for x in range(N):
        given_row = list(map(int, input().split()))
        for i in range(N):
            runner_idx, dir = given_row[i * 2], given_row[i * 2 + 1]
            y = i
            graph[x][y] = (runner_idx, dir - 1) # dir - 1: to use modulo operation


def in_range(x, y):
    global N
    return 0 <= x < N and 0 <= y < N
def move_runner(target_runner_idx):
    global N, graph, SEEKER

    def find_next_move(x, y, d):
        def runner_can_move(x, y):
            return in_range(x, y) and graph[x][y] != SEEKER

        # 45'씩 8번 회전해보면서 최초로 이동 가능한 곳으로 움직입니다.
        for rotate_count in range(8):
            new_d_idx = (d + rotate_count) % 8
            next_x, next_y = x + dxs[new_d_idx], y + dys[new_d_idx]
            if runner_can_move(next_x, next_y):
                return (next_x, next_y, new_d_idx)

    def swap(x, y, nx, ny):
        graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]

    for x in range(N):
        for y in range(N):
            runner_idx, d = graph[x][y]
            if target_runner_idx == runner_idx:
                # Find direction to move
                nx, ny, nd = find_next_move(x, y, d)
                graph[x][y] = (target_runner_idx, nd)
                swap(x, y, nx, ny)
                return

def move_all_runners():
    global N

    for i in range(1, N * N + 1):
        move_runner(i)


# 현재 술래말의 위치가 (x, y),
# 바라보고 있는 방향이 d이고
# 지금까지 얻은 점수가 score일때
# DFS방식으로 최고 점수를 찾는 함수
def search_max_score(x, y, d, score):
    global max_score, N, graph, VACANT, SEEKER

    def seeker_can_move(x, y):
        return in_range(x, y) and graph[x][y] != VACANT

    def done(x, y, d):
        for dist in range(1, N + 1):
            nx, ny = x + dxs[d] * dist, y + dys[d] * dist
            if seeker_can_move(nx, ny):
                return False
        return True

    # Base case for recursive function
    if done(x, y, d):
        max_score = max(max_score, score)
        return

    for dist in range(1, N + 1):
        nx, ny = x + dxs[d] * dist, y + dys[d] * dist
        if not seeker_can_move(nx, ny): continue

        # Save data to recover for depth first search
        recovery_data = [
            [graph[x][y] for y in range(N)]
            for x in range(N)
        ]

        # The seeker catch a runner
        extra_score, next_dir = graph[nx][ny]
        graph[nx][ny], graph[x][y] = SEEKER, VACANT

        # Run next round
        move_all_runners()
        search_max_score(nx, ny, next_dir, score + extra_score)

        # Recover the data
        for i in range(N):
            for j in range(N):
                # Update graph
                graph[i][j] = recovery_data[i][j]




def main():
    global graph, SEEKER, max_score

    get_input()

    # 1) Seeker move to (0, 0)
    init_score, init_dir = graph[0][0]
    graph[0][0] = SEEKER
    # 2) Move all runners for the first time
    move_all_runners()

    # Depth first search to find max score
    search_max_score(0, 0, init_dir, init_score)
    print(max_score)


# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

# test case answer
# 21
# 1
# 45

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    main()
    # ///////////////////////////////////////////////////////////////////////////////////
