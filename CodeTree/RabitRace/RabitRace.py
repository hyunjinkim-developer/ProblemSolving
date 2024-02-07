# SWEA 모의 SW역량 테스트 baseline

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
import collections

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




'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''

def ready(command):
    N, M, P = command[0], command[1], command[2]
    # rabits_dict[id]: [distance, count, score, r, c, r + c]
    rabits_dict = collections.defaultdict(list)

    # Save id and distance
    id_distance_list = command[3:]
    for idx in range(0, len(id_distance_list), 2):
        id, distance = id_distance_list[idx], id_distance_list[idx + 1]
        rabits_dict[id].append(distance)

    # Save count, score, r, c, r + c
    for id, data in rabits_dict.items():
        # Save count
        data.append(0)
        # Save score
        data.append(0)
        # Save location
        # save r
        data.append(1)
        # save c
        data.append(1)
        # save r + c
        data.append(2)

    return N, M, P, rabits_dict

def in_range(r, c):
    return 1 <= r <= N and 1 <= c <= M

def move_up(cr, cc, distance):
    # Reduce distance when the rabit runs more than one circle
    new_distance = distance % ((N - 1) * 2)

    # move up: All the way up to top
    if new_distance >= (cr - 1):
        new_distance -= (cr - 1)
        cr = 1
    else: # move up
        cr -= new_distance
        new_distance = 0

    # move up -> down
    if new_distance <= (N - 1):
        cr += new_distance
    # move up -> down -> up
    else:
        new_distance -= (N - 1)
        cr = N - new_distance

    return cr, cc

def move_down(cr, cc, distance):
    # Reduce distance when the rabit runs more than one circle
    new_distance = distance % ((N - 1) * 2)

    # move down: All the way up to bottom
    if new_distance >= N - cr:
        new_distance -= N - cr
        cr = N
    else: # move down
        cr += new_distance
        new_distance = 0

    # move down -> up
    if new_distance <= (N - 1):
        cr -= new_distance
    # move down -> up -> down
    else:
        new_distance -= (N - 1)
        cr = 1 + new_distance

    return cr, cc

def move_left(cr, cc, distance):
    # Reduce distance when the rabit runs more than one circle
    new_distance = distance % ((M - 1) * 2)

    # move left: All the way up to left
    if new_distance >= (cc - 1):
        new_distance -= (cc - 1)
        cc = 1
    else:  # move left
        cc -= new_distance
        new_distance = 0

    # move left -> right
    if new_distance <= (M - 1):
        cc += new_distance
    # move left -> right -> left
    else:
        new_distance -= (M - 1)
        cc = M - new_distance

    return cr, cc
def move_right(cr, cc, distance):
    # Reduce distance when the rabit runs more than one circle
    new_distance = distance % ((M - 1) * 2)

    # move right: All the way up to right
    if new_distance >= M - cc:
        new_distance -= M - cc
        cc = M
    else:  # move right
        cc += new_distance
        new_distance = 0

    # move right -> left
    if new_distance <= (M - 1):
        cc -= new_distance
    # move right -> left -> right
    else:
        new_distance -= (M - 1)
        cc = 1 + new_distance

    return cr, cc

# # Time out: N and M can be [2, 10 ^5_BFS-DFS], distance can be [1, 10^9_ShortestPath]
# def find_available_locations(target_id):
#     # rabits_dict[id]: [distance, count, score, r, c, r + c]
#     # distance
#     distance = rabits_dict[target_id][0]
#     # current r, c
#     cr, cc = rabits_dict[target_id][3_Greedy], rabits_dict[target_id][4_Simulation]
#
#     new_location = list()
#     # 상하좌우
#     dr_list = [-1, 1, 0, 0]
#     dc_list = [0, 0, -1, 1]
#     for dr, dc in zip(dr_list, dc_list):
#         nr, nc = cr, cc
#         for _ in range(distance):
#             # 다음 칸이 격자를 벗어나게 된다면 방향을 반대로 바꿔 한 칸 이동
#             if not in_range(nr + dr, nc + dc):
#                 dr *= -1
#                 dc *= -1
#             nr += dr
#             nc += dc
#         new_location.append((nr, nc))
#     return new_location

def move(target_id):
    # rabits_dict[id]: [distance, count, score, r, c, r + c]
    # distance
    distance = rabits_dict[target_id][0]
    # current r, c
    cr, cc = rabits_dict[target_id][3], rabits_dict[target_id][4]

    new_location = list()
    # # Timeout
    # new_location = find_available_locations(target_id)
    # 상하좌우
    new_location.append(move_up(cr, cc, distance))
    new_location.append(move_down(cr, cc, distance))
    new_location.append(move_left(cr, cc, distance))
    new_location.append(move_right(cr, cc, distance))

    # Find target location
    def custom_sort(item):
        r, c = item[0], item[1]
        return (r + c) * -1, r * -1, c * -1
    sorted_new_location = sorted(new_location, key=custom_sort)
    target_r, target_c = sorted_new_location[0]

    # Update rabits_dict
    rabits_dict[target_id][3], rabits_dict[target_id][4] = target_r, target_c
    rabits_dict[target_id][5] = target_r + target_c

    # return score
    return target_r + target_c

def select_target():
    # 가장 우선순위가 높은 토끼 찾기
    def custom_sort(item):
        # rabits_dict[id]: [distance, count, score, r, c, r + c]
        # 현재까지의 총 점프 횟수가 적은 토끼,
        # 현재 서있는 행 번호 + 열 번호가 작은 토끼,
        # 행 번호가 작은 토끼,
        # 열 번호가 작은 토끼,
        # 고유번호가 작은 토끼
        # rabits_dict[id]: [distance, count, score, r + c, r, c]
        return item[1][1], item[1][5], item[1][3], item[1][4], item[0]
    sort_by_priority = sorted(rabits_dict.items(), key=custom_sort)
    target_id = sort_by_priority[0][0]

    # Update count
    rabits_dict[target_id][1] += 1

    return target_id

def add_S(selected_rabits, S):
    # 우선순위가 높은 토끼 뽑기
    def custom_sort(item):
        # rabits_dict[id]: [distance, count, score, r, c, r + c]
        # 현재 서있는 행 번호 + 열 번호가 큰 토끼,
        # 행 번호가 큰 토끼,
        # 열 번호가 큰 토끼,
        # 고유번호가 큰 토끼
        return item[1][5] * -1, item[1][3] * -1, item[1][4] * -1, item[0] * -1
    sort_by_priority = sorted(selected_rabits.items(), key=custom_sort)
    target_id = sort_by_priority[0][0]

    # 점수 S를 더해주게 됩니다.
    rabits_dict[target_id][2] += S

def race(command):
    K, S = command[0], command[1]

    selected_rabits = dict()
    for i in range(K):
        # 우선순위가 높은 토끼 뽑기
        target_id = select_target()
        selected_rabits[target_id] = rabits_dict[target_id]

        # 토끼 이동
        score = move(target_id)

        # 나머지 토끼 점수 합산
        for id in rabits_dict:
            if id == target_id: continue
            # Update score
            rabits_dict[id][2] += score

    # 우선순위가 높은 토끼를 골라 점수 S를 더해주게 됩니다.
    add_S(selected_rabits, S)

def change_distance(command):
    pid, L = command[0], command[1]
    # 고유번호가 pid 인 토끼의 이동거리를 L배 해줍니다.
    # rabits_dict[id]: [distance, count, score, r, c, r + c]
    rabits_dict[pid][0] *= L
    return rabits_dict

def select_best_rabit():
    # 가장 높은 점수를 출력합니다.
    # rabits_dict[id]: [distance, count, score, r, c, r + c]
    sort_by_score = sorted(rabits_dict.items(), key=lambda item: item[1][2] * -1)
    best_rabbit_id = sort_by_score[0][0]
    highest_score = rabits_dict[best_rabbit_id][2]

    return print(highest_score)


# # Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

import collections

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    global Q, N, M, P
    global rabits_dict

    Q = int(input())
    for i in range(1, Q + 1):
        command_line = list(map(int, input().split()))
        command = command_line[0]
        if command == 100:
            N, M, P, rabits_dict = ready(command_line[1:])
        elif command == 200:
            race(command_line[1:])
        elif command == 300:
            change_distance(command_line[1:])
        elif command == 400:
            select_best_rabit()

    # ///////////////////////////////////////////////////////////////////////////////////
