# Solution 1:

# * 예술 점수 계산
# a와 그룹 b의 조화로움은
# (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
# x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
# => 서로 다른 변이 맞닿아있을 때마다
# (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
# 을 계산해서 더하기

from collections import defaultdict

total_art_points = 0
n = 0
paint = []

group = []
group_count = dict()
visited = []

drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

#debug
def print_matrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c], end='\t')
        print()
    print("-"*10)


def get_input():
    # 3 ≤ n ≤ 29

    global total_art_points, n, paint

    # Initialization
    total_art_points = 0
    n = 0
    paint = []

    n = int(input())
    for r in range(n):
        data = list(map(int, input().split()))
        paint.append(data)


def in_range(r, c):
    global n
    return 0 <= r < n and 0 <= c < n


def DFS(r, c, target_color, group_no):
    global paint, group, group_count, visited, drs, dcs

    # Base case for DFS
    if paint[r][c] != target_color:
        return

    visited[r][c] = True
    group[r][c] = group_no
    group_count[group_no] += 1

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        if visited[nr][nc]: continue
        DFS(nr, nc, target_color, group_no)

def make_group():
    global paint, group, group_count, visited

    # Initialization
    group_no = 0
    group = [[0] * n for _ in range(n)]
    group_count = defaultdict(int)
    visited = [[False] * n for _ in range(n)]

    # Traverse paint with DFSs
    for r in range(n):
        for c in range(n):
            if visited[r][c] == True: continue
            target_color = paint[r][c]
            group_no += 1
            DFS(r, c, target_color, group_no)

def calculate_art_points():
    art_points = 0
    global n, paint, group, group_count, visited, drs, dcs

    make_group()

    # # 예술 점수는 모든 그룹 쌍의 조화로움의 합으로 정의
    # a와 그룹 b의 조화로움은
    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
    # x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
    # => 서로 다른 변이 맞닿아있을 때마다
    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
    # 을 계산해서 더하기
    count_point = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            count_point[r][c] = True

            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc): continue
                if count_point[nr][nc]: continue

                if group[r][c] != group[nr][nc]:
                    g1, g2 = group[r][c], group[nr][nc]
                    art_points += (group_count[g1] + group_count[g2]) * paint[r][c] * paint[nr][nc]
    return art_points


def copy_cross(original, copied):
    global n

    mid_idx = n // 2
    for i in range(n):
        copied[i][mid_idx] = original[i][mid_idx]
        copied[mid_idx][i] = original[mid_idx][i]
    return copied

def split_others(original, copied):
    global n

    mid_idx = n // 2
    sub_paint_len = (n - 1) // 2
    others_starting_idx = [(0, 0), (0, mid_idx + 1), (mid_idx + 1, 0), (mid_idx + 1, mid_idx + 1)]

    for start_r, start_c in others_starting_idx:
        sub_paint = [[0] * sub_paint_len for _ in range(sub_paint_len)]
        for r in range(sub_paint_len):
            for c in range(sub_paint_len):
                nr, nc = start_r + r, start_c + c
                sub_paint[r][c] = original[nr][nc]
        copied.append(sub_paint)
    return copied

def split_paint():
    global n, paint

    cross = [[0] * n for _ in range(n)]
    cross = copy_cross(paint, cross)

    others = []
    split_others(paint, others)

    return cross, others

def rotate_cross(cross):
    # 십자 모양의 경우 통째로 반시계 방향으로 90' 회전
    global n

    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            result[n - 1 - c][r] = cross[r][c]

    return result

# 십자 모양을 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90'씩 회전
def rotate_others(others):

    def rotate_clockwise_90_degree(matrix):
        len_ = len(matrix)
        result = [[0] * len_ for _ in range(len_)]

        for r in range(len_):
            for c in range(len_):
                result[c][len_ - 1 - r] = matrix[r][c]
        return result

    result_others = []
    for i in range(4):
        rotated_sub_paint = rotate_clockwise_90_degree(others[i])
        result_others.append(rotated_sub_paint)
    return result_others

def join_paint(cross, others):
    global n, paint

    def join_others(sub_paint_list):
        global n, paint

        mid_idx = n // 2
        sub_paint_len = (n - 1) // 2
        others_starting_idx = [(0, 0), (0, mid_idx + 1), (mid_idx + 1, 0), (mid_idx + 1, mid_idx + 1)]
        for sub_paint_idx, (start_r, start_c) in enumerate(others_starting_idx):
            sub_paint = sub_paint_list[sub_paint_idx]
            for r in range(sub_paint_len):
                for c in range(sub_paint_len):
                    nr, nc = start_r + r, start_c + c
                    paint[nr][nc] = sub_paint[r][c]

    copy_cross(cross, paint)
    join_others(others)

def rotate_paint():
    cross, others = split_paint()

    # 십자 모양의 경우 통째로 반시계 방향으로 90' 회전
    cross = rotate_cross(cross)

    # 십자 모양을 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90'씩 회전
    others = rotate_others(others)

    join_paint(cross, others)



def main():
    global total_art_points

    get_input()

    # 초기 예술 점수 계산
    total_art_points += calculate_art_points()

    # 3번 회전
    for _ in range(3):
        # 그림에 대한 회전
        rotate_paint()

        # 회전 후 예술 점수 계산
        art_points = calculate_art_points()

        # 예술 점수 합산
        total_art_points += art_points
    print(total_art_points) # answer


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

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    main()
    # ///////////////////////////////////////////////////////////////////////////////////
