"""
# 문제의 Point
* 문제 잘 읽기!
    '1~3 과정 중 n번 칸 위치에 사람이 위치하면 그 즉시 내리게 됩니다.'라는 조건을 놓쳐서 불필요한 디버깅 시간을 들여야했다.
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

from collections import deque

n, k = 0, 0
moving_walkway = deque()
candidates = dict()
candidate_id = 1
candidates_location = list()

def get_input():
    global n, k, moving_walkway, candidates, candidate_id, candidates_location
    # Initialization
    n, k = 0, 0
    moving_walkway = deque()
    candidates = dict()
    candidate_id = 0

    # 무빙워크의 길이 n,
    # 실험을 종료하게 하는 안정성이 0인 판의 개수 k
    n, k = map(int, input().split())
    # candidates_location
    candidates_location = [-1 for _ in range(2 * n)]

    # 무빙워크 각각의 칸의 안정성
    moving_walkway.extend(deque(map(int, input().split())))

    if DEBUG:
        print("get input:", "*"*10)
        print(f"n: {n}, k: {k}")
        print(moving_walkway)


def rotate_moving_walkway():
    # 2n-1번 칸은 한 번 회전할 때 2n번째 칸의 위치로 이동하게 되고 2n번째 칸은 1번째 칸의 위치로 이동
    # 각 사람은 1번 칸에 올라서서 n번 칸에서 내리게
    global n, moving_walkway, candidates, candidates_location

    moving_walkway.rotate(1)
    for key, location in candidates.items():
        candidates[key] = (location + 1) % (n * 2)
    last_location = candidates_location.pop()
    new_candidates_location = [last_location]
    new_candidates_location.extend(candidates_location)
    candidates_location = new_candidates_location

    # 1~3 과정 중 n번 칸 위치에 사람이 위치하면 그 즉시 내리게 됩니다.
    get_off_moving_walkway()

    if DEBUG:
        print("rotate moving walkway:", "*"*10)
        print(moving_walkway)
        print("candidates:")
        print(candidates)
        print("locations:")
        print(candidates_location)


def move_candidate():
    # 가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한 칸 이동할 수 있으면 이동합니다.
    # 앞선 칸에 사람이 이미 있거나 앞선 칸의 안정성이 0인 경우에는 이동하지 않습니다.
    global candidates, n, candidates_location, moving_walkway

    if len(candidates) == 0:
        return

    # 가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한 칸 이동할 수 있으면 이동합니다.
    candidates_id = sorted(candidates.keys())
    for id in candidates_id:
        location = candidates[id]
        # 앞선 칸에 사람이 이미 있거나 앞선 칸의 안정성이 0인 경우에는 이동하지 않습니다.
        next_location = (location + 1) % (2 * n)
        if candidates_location[next_location] != -1: continue
        if moving_walkway[next_location] == 0: continue

        # Movable
        candidates[id] = next_location
        candidates_location[location] = -1
        candidates_location[next_location] = id
        # 사람이 어떤 칸에 올라가거나 이동하면 그 칸의 안정성은 즉시 1만큼 감소하게 되며
        moving_walkway[next_location] -= 1

        # 1~3 과정 중 n번 칸 위치에 사람이 위치하면 그 즉시 내리게 됩니다.
        if next_location == n - 1:
            get_off_moving_walkway()

    if DEBUG:
        print("move candidate:", "*"*10)
        print("candidates:")
        print(candidates)
        print("locations:")
        print(candidates_location)
        print("moving walkway:")
        print(moving_walkway)


def add_candidate():
    # 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한 명 더 올립니다.
    global moving_walkway, candidates, candidate_id, candidates_location

    # 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한 명 더 올립니다.
    if candidates_location[0] == -1 and moving_walkway[0] != 0:
        candidate_id += 1
        candidates[candidate_id] = 0
        candidates_location[0] = candidate_id
        moving_walkway[0] -= 1

    if DEBUG:
        print("add candidate:", "*"*10)
        print("candidates:")
        print(candidates)
        print("locations:")
        print(candidates_location)
        print("moving walkway:")
        print(moving_walkway)


def get_off_moving_walkway():
    global n, candidates_location, moving_walkway

    candidate_id_to_get_off = candidates_location[n - 1]
    if candidate_id_to_get_off != -1:
        candidates.pop(candidate_id_to_get_off)
        candidates_location[n - 1] = -1

    if DEBUG:
        print("get off moving walkway:", "*"*10)
        print("candidates:")
        print(candidates)
        print("locations:")
        print(candidates_location)


def count_reliability():
    # 각 칸의 안정성은 시간에 지남에 따라 다시 상승하지 않습니다.
    # 안정성이 0인 칸이 k개 이상이라면 과정을 종료합니다. 그렇지 않다면 다시 위의 과정을 반복합니다.
    global moving_walkway
    count = 0

    for reliability in moving_walkway:
        if reliability == 0:
            count += 1
    return count

def solution():
    global k
    global DEBUG

    # Debugging purpose
    DEBUG_SOL = False
    DEBUG_exp_no = 25

    experiment_no = 1
    while True:
        if DEBUG and DEBUG_SOL:
            print(f"experiment: {experiment_no}", "="*40)
            DEBUG = False
            if experiment_no <= DEBUG_exp_no:
                DEBUG = True

        # 1. 무빙워크가 한 칸 회전합니다.
        rotate_moving_walkway()

        # 2. 가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한 칸 이동할 수 있으면 이동합니다.
        #    만약 앞선 칸에 사람이 이미 있거나 앞선 칸의 안정성이 0인 경우에는 이동하지 않습니다.
        move_candidate()

        # 3. 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한 명 더 올립니다.
        add_candidate()

        # 안정성이 0인 칸이 k개 이상이라면 과정을 종료합니다. 그렇지 않다면 다시 위의 과정을 반복합니다.
        count = count_reliability()
        if k <= count:
            break

        if DEBUG and DEBUG_SOL:
            if experiment_no == DEBUG_exp_no:
                break

        experiment_no += 1
    # 무빙워크가 종료될 때 몇 번째 실험 중이었는지를 출력
    return experiment_no



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
# 133
# 3
# 2


# DEBUG = True
DEBUG = False # For submission


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    get_input()

    # ///////////////////////////////////////////////////////////////////////////////////
    if DEBUG:
        if test_case == 2:
            break

        print(f"test case: {test_case}", "="*30)
        answer = solution()
    # ///////////////////////////////////////////////////////////////////////////////////
    if not DEBUG:
        answer = solution()
    print("#%d:" % test_case, answer)