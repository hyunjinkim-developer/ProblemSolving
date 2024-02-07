# Data Structure
# "belts" holds each belt's boxes in 2-dimensional deque
# "belts_dict" holds box id as key and belt number of each box as value


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


def print_belts():
    for belt in belts:
        print(belt)

def build_factory(command):
    N = command[0]
    M = command[1]
    belts = collections.deque()

    # for each box (id, weight)
    id_list = command[2: 2 + N]
    weight_list = command[2 + N:]
    boxes = list(zip(id_list, weight_list))

    boxes_per_belt = N // M
    idx = 0
    for belt_idx in range(M):
        # belt = collections.deque(boxes[idx: idx + boxes_per_belt]) # When not using belts_dict
        belt = collections.deque()
        for box in boxes[idx: idx + boxes_per_belt]:
            id, weight = box
            belt.append(box)
            # Save as dictionary id: belt_idx
            # to find box efficiently in find_box()
            belts_dict[id] = belt_idx
        idx += boxes_per_belt
        belts.append(belt)
    return N, M, belts

def unload_box(w_max):
    unload_weights = 0

    for belt in belts:
        # if the belt is damaged
        if len(belt) == 0: continue

        id, weight = belt[0]
        # 각 벨트의 맨 앞에 있는 선물
        # 해당 선물의 무게가 w_max 이하라면 하차를 진행
        if weight <= w_max:
            unload_weights += weight
            belt.popleft()
            # Remove box from belts_dict
            del belts_dict[id]
        # 그렇지 않다면 해당 선물을 벨트 맨 뒤로 보냅니다.
        else:
            box = belt[0]
            # del belt[0] # same as.popleft() # the same as the code above
            belt.popleft()
            belt.append(box)

    # print unload boxes' weight
    print(unload_weights)


# 상자가 있는 경우 r_id값을,
# 없다면 -1을 출력
def remove_box(r_id):
    for idx, belt in enumerate(belts):
        for box in belt:
            id, weight = box

            # 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면,
            # 해당 벨트에서 상자를 제거하고
            # 이에 따라 뒤에 있던 상자들은 앞으로 한 칸씩 내려오게 됩니다.
            if id == r_id:
                belt.remove(box)
                # Remove box from belts_dict
                del belts_dict[id]
                return print(id)

    return print(-1)

def find_box(f_id):
    # 상자가 놓여있는 벨트가 있다면 해당 벨트의 번호를 출력하고,
    if f_id in belts_dict:
        belt_idx = belts_dict[f_id]
        for box_idx, box in enumerate(belts[belt_idx]):
            id, weight = box

            # 상자가 있는 경우, 해당 상자 위에 있는 모든 상자를 전부 앞으로 가져옵니다.
            # 가져올 시 순서는 그대로 유지가 되어야 함에 유의합니다.
            # Slicing deque: move_front = collections.deque()
            # move_front =  itertools.isslice(iterable, start, stop[, step])
            if id == f_id:
                belt_list = list(belts[belt_idx])
                not_moving = belt_list[:box_idx]
                move_front = belt_list[box_idx:]
                move_front.extend(not_moving)
                belts[belt_idx] = collections.deque(move_front)

                # 벨트의 번호를 출력
                return print(belt_idx + 1)  # belt number starts from 1
    # 상자가 놓여있는 벨트가 없다면 -1을 출력
    else:
        return print(-1)

def damage_belt(b_num):
    belt_idx = b_num - 1
    # b_num 벨트가 이미 망가져 있었다면 -1을 출력
    if len(belts[belt_idx]) == 0:
        print(-1)
        return
    # b_num 벨트가 망가져 있지 않았다면
    else:
        #  b_num 벨트의 바로 오른쪽 벨트부터 순서대로 보며
        #  아직 고장이 나지 않은 최초의 벨트 위로 b_num 벨트에 놓여 있던 상자들을 아래에서부터 순서대로 하나씩 옮겨줍니다.
        #  만약 m번 벨트까지 봤는데도 고장나지 않은 벨트가 없다면 다시 1번부터 순서대로 벨트를 확인

        # 옮길 벨트 찾기
        new_belt_idx = -1
        for i in range(1, M):
            new_belt_idx = (belt_idx + i) % M
            if len(belts[new_belt_idx]) != 0:
                break

        # Move gifts to new_belt_idx
        # belts[new_belt_idx].extend(belts[b_num_idx]) # when not using belts_dict
        for box in belts[belt_idx]:
            id, weight = box
            belts[new_belt_idx].append(box)
            # Update belt index
            belts_dict[id] = new_belt_idx
        belts[belt_idx] = collections.deque()

        # 그렇지 않았다면 정상적으로 고장을 처리했다는 뜻으로 b_num 값을 출력
        print(b_num)
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


import collections
# import itertools

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # print(f"test case:{test_case}", "="*15)

    global Q, N, M
    global belts, belts_dict
    belts_dict = dict()

    # Get input
    Q = int(input())
    for i in range(Q):
        command = list(map(int, input().split()))
        # build_factory
        if command[0] == 100:
            N, M, belts = build_factory(command[1:])
        # unload_box
        elif command[0] == 200:
            w_max = command[1]
            # print(f"Unload box: {w_max}", '-' * 5_BFS-DFS)
            unload_box(w_max)
        # remove_box
        elif command[0] == 300:
            r_id = command[1]
            # print(f"remove_box: {r_id}", "-" * 5_BFS-DFS)
            remove_box(r_id)
        # find_box
        elif command[0] == 400:
            f_id = command[1]
            # print(f"find_box: {f_id}", "-" * 5_BFS-DFS)
            find_box(f_id)
        # damage_belt
        elif command[0] == 500:
            b_num = command[1]
            # print(f"damage_belt: {b_num}", "-"*5_BFS-DFS)
            damage_belt(b_num)
    # ///////////////////////////////////////////////////////////////////////////////////
