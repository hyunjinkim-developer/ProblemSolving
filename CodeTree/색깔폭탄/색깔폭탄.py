# Soltuion
# * bomb group을 찾을 때,
#     RED가 아닌 색을 가진 위치를 중심으로 BFS하고 BFS조건에서 RED까지 bomb group에 포함하도록 작성
# * BFS하고 나면 중복되는 bomb group들이 생길텐데, 굳이 제거할 필요 없음
#     우선 순위에 해당하는 삭제할 bomb group과 그 그룹의 C(폭탄 개수)만 알면 되기 때문

from collections import deque

answer = 0

N, M = 0, 0
land = []
ROCK, RED = -1, 0
EMPTY = -2
EMPTY_GROUP = (-1, -1, -1, -1)

drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]


# # debug
# def print_matrix(matrix):
#     global N
#
#     for r in range(N):
#         for c in range(N):
#             print(matrix[r][c], end='\t')
#         print()
#     print('-' * 10)
#
# def print_list(list_):
#     for element in list_:
#         print(element)
#     print('-' * 10)


def get_input():
    # -1은 해당 칸에 검은색 돌이,
    # 0은 빨간색 폭탄이,
    # 1이상 m이하의 숫자는 빨간색과는 다른 서로 다른 색의 폭탄이 들어가 있음
    # 2 ≤ n ≤ 20
    # 2 ≤ m ≤ 5
    global answer, N, M, land

    # Initialization
    answer = 0
    N, M = 0, 0
    land = []

    N, M = map(int, input().split())
    for _ in range(N):
        land.append(list(map(int, input().split())))

def in_range(r, c):
    global N
    return 0 <= r < N and 0 <= c < N

def search_bomb_group(sr, sc, target_color):
    # 폭탄 묶음이란 2개 이상의 폭탄으로 이루어져 있어야 하며,
    # 모두 같은 색깔의 폭탄으로만 이루어져 있거나
    # 빨간색 폭탄을 포함하여 정확히 2개의 색깔로만 이루어진 폭탄을 의미
    # 다만, 빨간색 폭탄으로만 이루어져 있는 경우는 올바른 폭탄 묶음이 아니며,
    # 모든 폭탄들이 전부 격자 상에서 연결되어 있어야만 합니다.
    # 여기서 연결되어 있다는 말은,
    # 폭탄 묶음 내 한 폭탄으로부터 시작하여 상하좌우 인접한 곳에 있는 폭탄 묶음 내 폭탄으로만 이동했을 때 모든 폭탄들에 도달이 가능
    global N, land, drs, dcs, RED
    reds, others = [], []

    visited = [[False] * N for _ in range(N)]

    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    if land[sr][sc] == RED:
        reds.append((sr, sc))
    else:
        others.append((sr, sc))

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc]: continue
            if land[nr][nc] != target_color and land[nr][nc] != RED: continue

            if land[nr][nc] == RED:
                reds.append((nr, nc))
            else:
                others.append((nr, nc))
            visited[nr][nc] = True
            q.append((nr, nc))
    return reds, others


def find_bomb_group_priority(r, c):
    global land, EMPTY_GROUP
    ref_r, ref_c = -1, -1
    bomb_group, bomb_count, red_bomb_cnt = [], 0, 0

    target_color = land[r][c]
    reds, others = search_bomb_group(r, c, target_color)

    bomb_count = len(reds) + len(others)
    red_bomb_cnt = len(reds)

    # 폭탄 묶음이란 2개 이상의 폭탄으로 이루어져 있어야
    # 모두 같은 색깔의 폭탄으로만 이루어져 있거나
    # 빨간색 폭탄을 포함하여 정확히 2개의 색깔로만 이루어진 폭탄을 의미
    if bomb_count < 2:
        return bomb_group, EMPTY_GROUP


    # 기준점이란,
    # 해당 폭탄 묶음을 이루고 있는 폭탄들 중 빨간색이 아니면서
    # 행이 가장 큰 칸을 의미하며,
    # 만약 행이 가장 큰 폭탄이 여러 개라면 그 중 열이 가장 작은 칸을 의미합니다.
    def custom_sort(element):
        r, c = element
        return r * -1, c
    others = sorted(others, key=custom_sort)
    ref_r, ref_c = others[0]
    bomb_group.extend(reds)
    bomb_group.extend(others)

    # 열이 가장 작은 폭탄이 우선 순위를 가지는데 tuple값을
    # target_priority < priority로 비교하기 때문에 ref_c에 -1을 곱해서 우선순위를 높여야 함
    return bomb_group, (bomb_count, red_bomb_cnt * -1, ref_r, ref_c * -1)

def find_target_bomb_group():
    # 크기가 가장 큰 폭탄 묶음이라는 것은,
    # 가장 많은 수의 폭탄들로 이루어진 폭탄 묶음을 의미합니다.
    # 만약 크기가 큰 폭탄 묶음이 여러 개라면 다음 우선순위에 따라 폭탄 묶음을 선택합니다.
    # (1) 크기가 큰 폭탄 묶음들 중 빨간색 폭탄이 가장 적게 포함된 것 부터 선택합니다.
    # (2) 만약 (1)번 조건까지 동일한 폭탄 묶음이 여러 개라면, 각 폭탄 묶음의 기준점 중 가장 행이 큰 폭탄 묶음을 선택합니다.
    # 여기서 기준점이란,
    # 해당 폭탄 묶음을 이루고 있는 폭탄들 중 빨간색이 아니면서 행이 가장 큰 칸을 의미하며, 만약 행이 가장 큰 폭탄이 여러 개라면 그 중 열이 가장 작은 칸을 의미합니다.
    # (3) 만약 (2)번 조건까지 동일한 폭탄 묶음이 여러 개라면, 그 중 폭탄 묶음의 기준점 중 가장 열이 작은 폭탄 묶음을 선택합니다.
    global EMPTY_GROUP

    target_bomb_group = []
    target_priority = EMPTY_GROUP

    for r in range(N):
        for c in range(N):
            # 기준점이란, 해당 폭탄 묶음을 이루고 있는 폭탄들 중 빨간색이 아니면서 행이 가장 큰 칸을 의미
            if 1 <= land[r][c]:
                bomb_group, priority = find_bomb_group_priority(r, c)
                if target_priority < priority:
                    target_priority = priority
                    target_bomb_group = bomb_group
    return target_priority, target_bomb_group

def set_off_bomb_group(target_bomb_group):
    global land, EMPTY

    for r, c in target_bomb_group:
        land[r][c] = EMPTY

def apply_gravity():
    global N, land, EMPTY

    result = [[EMPTY] * N for _ in range(N)]
    for c in range(N):
        r_idx = N - 1
        for r in range(N - 1, -1, -1):
            if land[r][c] == EMPTY: continue
            if land[r][c] == ROCK:
                r_idx = r
            result[r_idx][c] = land[r][c]
            r_idx -= 1
    land = result

def rotate_counter_clockwise_90_deg():
    global N, land, EMPTY

    result = [[EMPTY] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            result[N - 1 - c][r] = land[r][c]
    land = result

def simulate():
    global answer, EMPTY_GROUP

    # 1
    # 현재 격자에서 크기가 가장 큰 폭탄 묶음을 찾습니다.
    target, target_bomb_group = find_target_bomb_group()
    # 위의 과정을 더 이상 폭탄 묶음이 존재하지 않을 때까지 반복
    if target == EMPTY_GROUP:
        return False

    # 2
    # 선택된 폭탄 묶음에 해당되는 폭탄들을 전부 제거
    # 한 round 마다, 폭탄 묶음이 터지면서 폭탄 묶음을 이루고 있는 폭탄의 개수를 C라 했을 때 C * C 만큼의 점수를 얻게 됩니다.
    # 이러한 상황에서 더 이상 폭탄이 터지지 않을 때 까지 얻게되는 총 점수를 구해야
    C = len(target_bomb_group)
    answer += (C * C)
    set_off_bomb_group(target_bomb_group)
    apply_gravity()

    # 3
    # 반시계 방향으로 90' 만큼 격자 판에 회전
    rotate_counter_clockwise_90_deg()

    # 4
    # 다시 중력이 작용하며, 이때 역시 돌은 절대로 떨어지지 않습니다.
    apply_gravity()
    return True

def main():
    global answer

    get_input()

    while True:
        if simulate() == False:
            break
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

# # answer
# 38
# 0
# 343
# 157
# 401

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    main()
    # ///////////////////////////////////////////////////////////////////////////////////
