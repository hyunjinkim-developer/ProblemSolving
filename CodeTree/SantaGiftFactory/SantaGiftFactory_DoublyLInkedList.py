# Data Structure
# gifts_dict[gift_id] : [weight, prev_id, next_id, belt_idx]
# belt_dict[belt_idx]: [start_gift_id, end_gift_id]
# Why did I choose this DS?
# Q: [1, 10^5]
# N: [1, 10^5]
# M: [1, 10]
# time limitation: 1s

# if belt_idx is not saved for each gift,
# find_box() would cost O(Q * N) which could be 10^10 in worst case (time out)
# with belt_idx, searching each gift would cost O(1)

# Saving belt_idx requires computing power in damage_belt()
# if the belt is damaged: O(1)
# if the belt is not damaged:
#   change belt_idx for the number of gifts in the belt
# However, M can be at most 10 and damaged belt cannot be recovered
#   Therefore, in the worst case can be only O(N * M) (approximately 10^6)
#   N/M * (1 + 2 + 3 + ... + M) move all gifts until when only one belt working)

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
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''


def print_belts():
    for belt_num in range(M):
        print(belt_num, ":", belt_dict[belt_num])

def build_factory(command):
    N = command[0]
    M = command[1]

    # for each box (id, weight)
    id_list = command[2: 2 + N]
    weight_list = command[2 + N:]
    boxes = list(zip(id_list, weight_list))

    boxes_per_belt = N // M
    idx = 0
    for belt_idx in range(M):
        # Save start box id of each belt
        start_id, weight = boxes[idx]
        belt_dict[belt_idx].append(start_id)

        prev_id = -1
        # For each belt
        belt = boxes[idx: idx + boxes_per_belt]
        for gift_idx, gift in enumerate(belt):
            id, weight = gift

            # gifts_dict[id]: [weight, prev_id, next_id, belt_idx]
            # first box: prev_id := -1
            # end box: next_id := -1
            # Save weight
            gifts_dict[id].append(weight)
            # Save prev_id
            gifts_dict[id].append(prev_id)
            # Save next_id
            if gift_idx == boxes_per_belt - 1:
                gifts_dict[id].append(-1)
            else:
                next_id, weight = belt[gift_idx + 1]
                gifts_dict[id].append(next_id)
            # Save belt_idx
            gifts_dict[id].append(belt_idx)

            # Update previous id
            prev_id = id

        idx += boxes_per_belt
        # Save end box id of each belt
        end_id, weight = boxes[idx - 1]
        belt_dict[belt_idx].append(end_id)

    return N, M, gifts_dict, belt_dict

def unload_box(w_max):
    unload_weights = 0

    for belt_num in range(M):
        # if the belt is damaged
        if len(belt_dict[belt_num]) == 0: continue

        # 각 벨트의 맨 앞에 있는 선물
        first_gift_id, end_gift_id = belt_dict[belt_num]
        weight, prev_id, next_id, _ = gifts_dict[first_gift_id]

        # 해당 선물의 무게가 w_max 이하라면 하차를 진행
        if weight <= w_max:
            unload_weights += weight
            gifts_dict.pop(first_gift_id)
            # If there's no gift left
            if first_gift_id == end_gift_id:
                belt_dict[belt_num] = list()
            else:
                # Update belt_dict
                belt_dict[belt_num][0] = next_id
                # Update next gift's prev_id
                gifts_dict[next_id][1] = -1
        # 그렇지 않다면 해당 선물을 벨트 맨 뒤로 보냅니다.
        else:
            # If there's more than one gift
            if first_gift_id != end_gift_id:
                # Update gifts_dict
                # Update next gift's prev_id
                gifts_dict[next_id][1] = -1
                # 선물을 벨트 맨 뒤로 보냅니다
                # 기존에 맨 뒤에 있던 선물
                previous_last_gift_id = belt_dict[belt_num][1]
                gifts_dict[previous_last_gift_id][2] = first_gift_id
                # 맨 앞에 있던 선물이 맨 뒤로 이동
                gifts_dict[first_gift_id][1] = previous_last_gift_id
                gifts_dict[first_gift_id][2] = -1

                # Update belt_dict
                belt_dict[belt_num][0] = next_id
                belt_dict[belt_num][1] = first_gift_id

    # print unload boxes' weight
    print(unload_weights)

def remove_box(r_id):
    if r_id in gifts_dict:
        # 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면,
        # 해당 벨트에서 상자를 제거하고
        # 이에 따라 뒤에 있던 상자들은 앞으로 한 칸씩 내려오게 됩니다.
        _, prev_id, next_id, _ = gifts_dict[r_id]
        # if r_id is the first gift of the belt, no need to move gifts behind
        if prev_id == -1:
            gifts_dict[next_id][1] = -1
            # Find belt number index
            belt_num_idx = -1
            for belt_idx in range(M):
                # the belt had been damaged
                if len(belt_dict[belt_idx]) == 0: continue
                if belt_dict[belt_idx][0] == r_id:
                    belt_num_idx = belt_idx
                    break
            # Update belt_dict
            belt_dict[belt_num_idx][0] = next_id
        # If r_id is the last gift of the belt, no need to move gifts behind
        elif next_id == -1:
            gifts_dict[prev_id][2] = -1
            # Find belt number index
            belt_num_idx = -1
            for belt_idx in range(M):
                # the belt had been damaged
                if len(belt_dict[belt_idx]) == 0: continue
                if belt_dict[belt_idx][1] == r_id:
                    belt_num_idx = belt_idx
                    break
            # Update belt_dict
            belt_dict[belt_num_idx][1] = prev_id
        else:
            # Update prev_id gift's next_id
            gifts_dict[prev_id][2] = next_id
            # Update next_id gift's prev_id
            gifts_dict[next_id][1] = prev_id
        # Remove r_id gift
        gifts_dict.pop(r_id)

        # 상자가 있는 경우 r_id값을,
        return print(r_id)
    else:
        # 없다면 -1을 출력
        return print(-1)

def find_box(f_id):
    # 상자가 놓여있는 벨트가 있다면 해당 벨트의 번호를 출력하고,
    if f_id in gifts_dict:
        belt_idx = gifts_dict[f_id][3]

        # 상자가 있는 경우, 해당 상자 위에 있는 모든 상자를 전부 앞으로 가져옵니다.
        # 가져올 시 순서는 그대로 유지가 되어야 함에 유의합니다.
        first_gift_id, end_gift_id = belt_dict[belt_idx]
        _, prev_id, next_id, _ = gifts_dict[f_id]

        # If f_id is the first gift of the belt, no need to move gifts behind
        if first_gift_id != f_id:
            # f_id become the first gift of the belt
            gifts_dict[f_id][1] = -1
            gifts_dict[end_gift_id][2] = first_gift_id
            # Update not moving gifts
            gifts_dict[first_gift_id][1] = end_gift_id
            gifts_dict[prev_id][2] = -1
            # Update belt_dict
            belt_dict[belt_idx][0] = f_id
            belt_dict[belt_idx][1] = prev_id

        # 벨트의 번호를 출력
        return print(belt_idx + 1)  # belt number starts from 1

    # 상자가 놓여있는 벨트가 없다면 -1을 출력
    else:
        return print(-1)

def damage_belt(b_num):
    b_num_idx = b_num - 1
    # b_num 벨트가 이미 망가져 있었다면 -1을 출력
    if len(belt_dict[b_num_idx]) == 0:
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
            new_belt_idx = (b_num_idx + i) % M
            if len(belt_dict[new_belt_idx]) != 0:
                break

        # Move all gifts in b_num_idx to new_belt_idx
        # Update belt_idx into new belt index from gifts_dict
        current_gift_id, _ = belt_dict[b_num_idx]
        while current_gift_id != -1:
            gifts_dict[current_gift_id][3] = new_belt_idx
            # Move to next gift
            current_gift_id = gifts_dict[current_gift_id][2]
        # Update gifts_dict prev_id, next_id
        start_gift_id, end_gift_id = belt_dict[b_num_idx]
        dst_start_gift_id, dst_end_gift_id = belt_dict[new_belt_idx]
        # Update gifts_dict
        gifts_dict[dst_end_gift_id][2] = start_gift_id
        gifts_dict[start_gift_id][1] = dst_end_gift_id
        # Update belt_dict
        belt_dict[b_num_idx] = list()
        belt_dict[new_belt_idx][0] = dst_start_gift_id
        belt_dict[new_belt_idx][1] = end_gift_id

        # 정상적으로 고장을 처리했다는 뜻으로 b_num 값을 출력
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

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    global Q, N, M
    global gifts_dict, belt_dict
    gifts_dict = collections.defaultdict(list)
    belt_dict = collections.defaultdict(list)

    # Get input
    Q = int(input())
    for i in range(Q):
        command = list(map(int, input().split()))
        # build_factory
        if command[0] == 100:
            N, M, gifts_dict, belt_dict = build_factory(command[1:])
        # unload_box
        elif command[0] == 200:
            w_max = command[1]
            unload_box(w_max)
        # remove_box
        elif command[0] == 300:
            r_id = command[1]
            remove_box(r_id)
        # find_box
        elif command[0] == 400:
            f_id = command[1]
            find_box(f_id)
        # damage_belt
        elif command[0] == 500:
            b_num = command[1]
            damage_belt(b_num)
    # ///////////////////////////////////////////////////////////////////////////////////
