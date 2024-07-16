"""
* 상하좌우 인접한 2-dimensional array에서 같은 값을 갖고 있는 그룹 찾기, 각 그룹을 저장하기
- 1) 유효한(3개 이상) fragments 찾기
- 2) fragments 비우기
    * acquire_remain()로 implement
        - end condition: 새로운 위치의 remain_no가 주어진(이전 위치의) remain_no와 다른 경우
        - fragments의 수가 3개 이상인 경우만 저장 acquired_value로 인정됨
        - fragments를 비워야 하기 때문에 DFS로 Traversal을 하면서 fragments(같은 remain_no를 가진 그룹)의 위치를 저장히고
            fragments의 수가 3이상인 경우 spot_to_be_emptied로 저장한 뒤
            empty == True인 경우 한꺼번에 제거
        - 같은 위치를 다시 방문할 수 없기 때문에 visited로 방문한 위치인지 확인

* 시간이 급박할 때 안전하게 Debugging하는 방법
* detail! 잘 읽기!
    * 문제를 읽으면서 함수들의 실행 순서, 명세(input, output), 세부 조건을 정리해두면 유용함
    * 회전할 grid를 찾는 우선순위에서 열이 행보다 먼저
"""

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3_Greedy
c, d, e = 1.0, 2.5_BFS-DFS, 3_Greedy.4_Simulation
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

from collections import defaultdict, deque

K = 0
remains = []
wall = deque()
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # from up in clockwise

# Debug
def print_list(array):
    for r in range(5):
        for c in range(5):
            print(array[r][c], end='\t')
        print()
    print("-"*10)

def print_dict(dictionary):
    keys = sorted(dictionary.keys(), reverse=True)
    for key in keys:
        print(key, ":", dictionary[key])

def get_input():
    global K, remains, wall

    # Initialization
    K = 0
    remains = []
    wall = deque()

    K, M = map(int, input().split())
    for _ in range(5):
        remains.append(list(map(int, input().split())))
    wall.extend(list(map(int, input().split())))

    # if DEBUG:
    #     print(K, M)
    #     print_list(remains)
    #     print(wall)


def in_range(r, c):
    return 0 <= r < 5 and 0 <= c < 5


def explore():
    total_value = 0

    # 1) Select grid
    rotation_count, center_row, center_col = select_grid()
    # 획득할 유물이 있을 경우
    if rotation_count != -1 and center_row != -1 and center_col != -1:
        # 2) 유물 획득
        total_value = mining(rotation_count, center_row, center_col)
    return total_value


def select_grid():
    # Return selected rotation_count, center_row, center_col of 3 * 3 grid
    # If there's no remain to acquire, return -1, -1, -1
    selected_rotation_count, selected_center_row, selected_center_col = -1, -1, -1

    # Copy remains (When copy.deepcopy() not allowed)
    def copy_remains():
        global remains
        new_remains = [[0] * 5 for _ in range(5)]
        for r in range(5):
            for c in range(5):
                new_remains[r][c] = remains[r][c]
        return new_remains

    # Find 3 * 3 grid location
    find_grid = defaultdict(list)
    for r in range(3):
        for c in range(3):
            # Copy original remains
            rotated_remains = copy_remains()
            # Rotate 90 degrees at each time
            for rot_count in range(1, 4):
                rotated_remains = rotate_clockwise_90deg(rotated_remains, r, c)

                value, _ = acquire_remain(rotated_remains)
                if 3 <= value:
                    # Center of the rotation (r + 1, c + 1)
                    find_grid[value].append((rot_count, r + 1, c + 1))

                if DEBUG:
                    print(f"r, c, rot: {r, c, rot_count}", "*"*20)
                    print_list(rotated_remains)
                    print(value, "*"*10)

    # Find 3 * 3 grid with priority
    # (1) 유물 1차 획득 가치를 최대화
    # (2) 회전한 각도가 가장 작은
    # (3) 회전 중심 좌표의 열이 가장 작은 구간을,
    #       열이 같다면 행이 가장 작은 구간을 선택
    if find_grid:
        max_value = max(find_grid.keys())
        def custom_sort(item):
            rot_count, center_r, center_c = item
            return rot_count, center_c, center_r
        selected_rotation_count, selected_center_row, selected_center_col = sorted(find_grid[max_value], key=custom_sort)[0]
        if DEBUG:
            print("find_grid: ")
            print(max_value, sorted(find_grid[max_value], key=custom_sort))

    return selected_rotation_count, selected_center_row, selected_center_col

def rotate_clockwise_90deg(rotated_remains, start_r, start_c):
    # start_r, start_c : upper left corner of the grid
    # Rotate 3 * 3 grid
    rotated_grid = [[-1] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            # rotated_grid[c][(N - 1) - r]
            rotated_grid[c][2 - r] = rotated_remains[start_r + r][start_c + c]

    # Update rotated 3 * 3 grid to remains
    for r in range(3):
        for c in range(3):
            rotated_remains[start_r + r][start_c + c] = rotated_grid[r][c]
    return rotated_remains

def acquire_remain(remains, empty=False):
    # 상하좌우로 인접한 같은 종류의 유물 조각은 서로 연결
    # 3개 이상 연결된 경우, 조각이 모여 유물이 되고 사라집니다.
    # 유물의 가치는 모인 조각의 개수와 같습니다.
    acquired_value = 0

    def dfs(start_r, start_c, remains_no, fragments):
        global dirs
        nonlocal remains, visited, count, empty

        if remains[start_r][start_c] != remains_no:
            return

        visited[start_r][start_c] = True
        count += 1
        if empty == True:
            fragments.append((start_r, start_c))

        # if DEBUG:
        #     print(f"r, c: {r, c} / count: {count}")
        #     print_list(visited)
        #     print("*"*10)
        for dr, dc in dirs:
            nr, nc = start_r + dr, start_c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc]: continue
            dfs(nr,nc, remains_no, fragments)

    # Traverse to find fragments(a group of remains that have the same remains_no
    visited = [[False] * 5 for _ in range(5)]
    spot_to_be_emptied = []
    for r in range(5):
        for c in range(5):
            if visited[r][c]: continue

            remains_no = remains[r][c]
            count = 0
            fragments = []
            dfs(r, c, remains_no, fragments)
            if empty == True:
                if 3 <= len(fragments):
                    spot_to_be_emptied.extend(fragments)

            # # print dfs result
            # if DEBUG:
            #     print(r, c, ":", count)
            #     print_list(visited)
            #     print("*"*20)
            if 3 <= count:
                acquired_value += count

    # Empty fragments
    if empty == True:
        for r, c in spot_to_be_emptied:
            remains[r][c] = -1

    return acquired_value, remains

def fill_empty(remains):
    global wall

    for c in range(5):
        for r in range(4, -1, -1):
            if remains[r][c] == -1:
                fragment_to_fill = wall.popleft()
                remains[r][c] = fragment_to_fill
    return remains

def mining(rot_count, center_r, center_c):
    global remains
    total_value = 0

    # 1)
    # Convert remains with selected rotation count, center_row, center_c
    # Convert rotation point into upper left corner
    for _ in range(rot_count):
        remains = rotate_clockwise_90deg(remains, center_r - 1, center_c - 1)
    if DEBUG:
        print("mining: converted remains with selected gird")
        print_list(remains)

    # 2)
    # 유물 1차 획득
    acquired_value, remains = acquire_remain(remains, True)
    total_value += acquired_value
    if DEBUG:
        print(f"1st acquired value: {acquired_value}")
        print("emptied: ")
        print_list(remains)

    # 유물 1차 빈칸 채우기
    remains = fill_empty(remains)
    if DEBUG:
        print("filled:")
        print_list(remains)
        global wall
        print(wall)

    # 3)
    # 유물 연쇄 획득
    # 더 이상 조각이 3개 이상 연결되지 않아 유물이 될 수 없을 때까지 반복
    # (1) 유물 획득
    # (2) 유적 빈칸 채우기
    acquired_value = -1 # Initialize
    while True:
        acquired_value, remains = acquire_remain(remains, True)
        total_value += acquired_value
        if acquired_value == 0: break

        if DEBUG:
            print(f"acquired value: {acquired_value}", "-"*20)
            print("emptied: ")
            print_list(remains)

        remains = fill_empty(remains)
        if DEBUG:
            print("remains after filled")
            print_list(remains)
            # global wall
            print(wall)

    return total_value


def solution():
    global K

    # 탐사 진행 ~ 유물 연쇄 획득의 과정까지를 1턴
    for _ in range(K):
        if DEBUG:
            print("="*50)

        total_value = explore()
        # 탐사 진행 과정에서 어떠한 방법을 사용하더라도 유물을 획득할 수 없었다면 모든 탐사는 그 즉시 종료
        # 이 경우 얻을 수 있는 유물이 존재하지 않음으로, 종료되는 턴에 아무 값도 출력하지 않음에 유의
        if total_value == 0:
            return
        # 첫 번째 줄에 각 턴 마다 획득한 유물의 가치의 총합을 공백을 사이에 두고 출력
        print(total_value, end=" ")
    return



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
# answer
# 16
# 9 9 6 14 9
# 17
# 17 3


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    get_input()

    DEBUG = False
    if DEBUG:
        if test_case < T:
            print_list(remains)
            print(wall)
            print(f"test case: {test_case}", "="*30)
            solution()
            print()

    solution()
    print()
    # ///////////////////////////////////////////////////////////////////////////////////
