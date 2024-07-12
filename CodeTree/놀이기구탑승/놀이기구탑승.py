"""
# 이 문제의 포인트
* 3), 4)의 경우 각각, r ASC, c ASC 기준의 sorting 이므로
    한 번에 sorting 하고 가장 우선 순위가 높은 자리에 학생을 배치
* 마지막 학생의 경우
    빈 자리가 1개 밖에 남지 않았기 때문에
    2), 3), 4)의 과정을 거칠 필요가 없다
* 주변에 빈 공간이 없는 경우
    주변에 빈 공간이 없는 자리들을 따로 저장해서
    그 중에 3), 4) 우선 순위에 따라 학생이 앉을 자리를 지정하면 된다.
"""

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

from collections import defaultdict

n = 0
student_no = list()
close_friends = dict()
land = []
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # from up in clockwise

def get_input():
    global n, student_no, close_friends, land

    # Initialization
    n = 0
    student_no = list()
    close_friends = dict()
    land = []

    n = int(input())
    # 각 학생별로 좋아하는 학생이 정확히 4명씩 정해져
    for _ in range(n * n):
        # n0는 지금 턴에 탑승하는 학생의 번호
        # n0는 서로 겹치지 않음
        # n1, n2, n3, n4는 n0 학생이 좋아하는 학생의 번호 (n0은 제외됨)
        n0, n1, n2, n3, n4 = map(int, input().split())
        student_no.append(n0)
        close_friends[n0] = [n1, n2, n3, n4]
    # land
    land = [[0] * n for _ in range(n)]


    if DEBUG:
        print("Get input:", "*"*30)
        print(student_no)
        print(close_friends)
        print_list(land)

def print_list(array):
    global n
    for r in range(n):
        for c in range(n):
            print(array[r][c], end='\t')
        print()
    print('-'*10)

def in_range(r, c):
    global n
    return 0 <= r < n and 0 <= c < n


def find_location_with_many_friends(id):
    global land, dirs, close_friends
    location_with_many_friends = defaultdict(list)

    for r in range(n):
        for c in range(n):
            # ! 항상 '비어있는 칸으로만 이동'
            if land[r][c] != 0: continue

            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc): continue

                friend_id = land[nr][nc]
                if friend_id in close_friends[id]:
                    count += 1
            location_with_many_friends[count].append((r, c))
    max_count = max(location_with_many_friends.keys())

    if DEBUG:
        print(f"Find locaiton with many friends", "*"*30)
        print(location_with_many_friends[max_count])

    return location_with_many_friends[max_count]



def find_spacious_location(max_friends_locations):
# 상하좌우 비어있는 칸의 수가 가장 많은 위치로
    global n, land, dirs
    count_vacant_location = defaultdict(list)

    not_vacant_location = list()
    for r, c in max_friends_locations:
        count = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # ! 이때 '격자를 벗어나는 칸은 비어있는 칸으로 간주하지 않습니다'
            if not in_range(nr, nc): continue
            if land[nr][nc] != 0: continue # 주변 칸이 비어 있지 않은 경우
            count += 1
            count_vacant_location[count].append((r, c))
        if count == 0:
            not_vacant_location.append((r, c))
    if len(count_vacant_location) == 0:

        if DEBUG:
            print(f"Find_spacious_location", "*" * 30)
            print("not vacant", "*"*5)
            print(not_vacant_location)

        return not_vacant_location
    else:
        max_count = max(count_vacant_location.keys())

        if DEBUG:
            print(f"Find_spacious_location", "*" * 30)
            print(count_vacant_location[max_count])

        return count_vacant_location[max_count]


def calculate_total_score():
    global n, land, dirs, close_friends
    total_score = 0

    score_table = {0: 0,
                   1: 1,
                   2: 10,
                   3: 100,
                   4: 1000}
    for r in range(n):
        for c in range(n):
            id = land[r][c]
            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc): continue
                adj_student_id = land[nr][nc]
                if adj_student_id in close_friends[id]:
                    count += 1
            total_score += score_table[count]
    return total_score


def solution():
    global student_no, land
    # 입력으로 주어진 순서대로
    # 음 조건에 따라 가장 우선순위가 높은 칸으로 탑승
    # ! 항상 '비어있는 칸으로만 이동'

    for idx, id in enumerate(student_no):
        # 1)
        # 격자를 벗어나지 않는 4방향으로 인접한 칸 중
        # 좋아하는 친구의 수가 가장 많은 위치로
        max_friends_locations = find_location_with_many_friends(id)

        # 마지막 학생은 남은 자리가 한 개이므로 2), 3), 4) 없이 바로 배치
        if idx == len(student_no) - 1:
            target_r, target_c = max_friends_locations[0]
            land[target_r][target_c] = id

        else:
            # 2)
            # 만약 1번 조건을 만족하는 칸의 위치가 여러 곳
            # 비어있는 칸의 수가 가장 많은 위치로
            # ! 이때 '격자를 벗어나는 칸은 비어있는 칸으로 간주하지 않습니다'
            max_vacant_locations = find_spacious_location(max_friends_locations)

            # 3)
            # 만약 2번 조건까지 동일한 위치가 여러 곳
            # 그 중 행 번호가 가장 작은 위치로
            # 4)
            # 만약 3번 조건까지 동일한 위치가 여러 곳
            # 열 번호가 가장 작은 위치로
            def custom_sort(item):
                r, c = item
                return r, c
            sorted_locations = sorted(max_vacant_locations, key=custom_sort)
            target_r, target_c = sorted_locations[0]
            land[target_r][target_c] = id

        if DEBUG:
            print("Sorted", "*"*30)
            print(sorted_locations)
            print(f"Locate student {id} completeds", "*"*30)
            print_list(land)


    # 최종 점수는 모든 학생들이 탑승한 이후,
    # 각 학생마다의 점수를 합한 점수가 됩니다.
    # 각 학생의 점수는 해당 학생의 인접한 곳에 앉아 있는 좋아하는 친구의 수로 결정
    answer = calculate_total_score()
    return answer

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
# Answer
# 175
# 170
# 270

# DEBUG = True
DEBUG = False # For submission

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    get_input()

    if DEBUG:
        print(f"test case: {test_case}", "="*30)
        print(solution())

    # ///////////////////////////////////////////////////////////////////////////////////
    if not DEBUG:
        answer = solution()
        print("#%d:" % test_case, answer)