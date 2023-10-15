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
import copy

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



# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")


N, M, H, K = 0, 0, 0, 0
runner_list, runner_direction = list(), list()
seeker, seeker_locations = (0, 0), list()
trees = list()
total_score = 0


# For debugging
def print_matrix(target_list, target_direction):
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    for idx, element in enumerate(target_list):
        x, y = element
        d = target_direction[idx]
        matrix[x][y] = d

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            print(matrix[x][y], end=" ")
        print()

def find_direction_goinginward(seeker_location):
    # x: row, y: col
    # Up, Right, Down, Left
    direction_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Going outward
    # 1, 1, 2, 2, 3, 3, ..., N - 2, N - 2, N - 1, N - 1, N - 1
    d_idx = 0
    dx, dy = -1, 0
    for i in range(1, N):  # [1, N - 1]
        for count in range(1, 2 * i + 1):
            seeker_location.append((dx, dy))
            if count % i == 0:
                d_idx += 1
                dx, dy = direction_list[d_idx % 4]

    for _ in range(1, N):  # [1, N - 1]
        dx, dy = direction_list[d_idx % 4]
        seeker_location.append((dx, dy))
    return seeker_location

def find_direction_goingoutward(seeker_location):
    outward_location = list()
    for idx in range(len(seeker_location) - 1, -1, -1):
        dx, dy = seeker_location[idx]
        # Change direction
        outward_location.append((dx * -1, dy * -1))
    seeker_location.extend(outward_location)
    return seeker_location

def find_seeker_locations(N):
    seeker_locations = list()
    # turn > 2 * N - 1 : Going inward
    # Going inward
    seeker_locations = find_direction_goinginward(seeker_locations)
    # Going inward -> Outward
    seeker_locations = find_direction_goingoutward(seeker_locations)
    return seeker_locations

def get_input():
    global N, M, H, K
    global runner_list, runner_direction
    global trees
    global seeker, seeker_locations

    # Get input
    N, M, H, K = map(int, input().split())
    runner_list = list()
    runner_direction = list()
    trees = [[False] * (N + 1) for _ in range(N + 1)]
    seeker = (N // 2 + 1, N // 2 + 1)
    seeker_locations = list()
    # Save hiders
    for _ in range(M):
        x, y, d = map(int, input().split())
        # runner_list.append((x, y, d))
        runner_list.append((x, y))
        runner_direction.append(d)
    # Save trees
    for _ in range(H):
        x, y = map(int, input().split())
        trees[x][y] = True

    # Find seeker's locations
    seeker_locations = find_seeker_locations(N)


def distance_to_seeker(x1, y1):
    # 도망자의 위치가 (x1, y1), 술래의 위치가 (x2, y2)라 했을 때
    # 두 사람간의 거리는 |x1 - x2| + |y1 - y2|로 정의
    x2, y2 = seeker[0], seeker[1]
    return abs(x1 - x2) + abs(y1 - y2)

def in_range(y, x):
    return 1 <= y <= N and 1 <= x <= N

def runner_move(x, y, d):
    direction_dict = {1: (0, 1), 2: (1, 0), -1: (0, -1), -2: (-1, 0)}

    # Find new location
    direction = direction_dict[d]
    nx, ny = x + direction[0], y + direction[1]
    # 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우
    if not in_range(nx, ny):
        # 먼저 방향을 반대로 틀어줍니다.
        d *= -1
        direction = direction_dict[d]
        nx, ny = x + direction[0], y + direction[1]

    # 움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동합니다.
    # 해당 칸에 나무가 있어도 괜찮습니다.
    if not(nx == seeker[0] and ny == seeker[1]):
        return nx, ny, d
    # 움직이려는 칸에 술래가 있는 경우라면 움직이지 않습니다.
    else:
        return x, y, d



def run():
    global runner_list, runner_direction

    print("before move")
    print(runner_list)
    print(runner_direction)

    for idx, runner in enumerate(runner_list.copy()):
        x, y = runner
        d = runner_direction[idx]

        # 현재 술래와의 거리가 3 이하인 도망자만 움직입니다.
        if distance_to_seeker(x, y) > 3: continue

        x, y, d = runner_move(x, y, d)
        runner_list[idx] = (x, y)
        runner_direction[idx] = d
        if runner == (2, 4):
            print(x, y, d)
            print(runner_list)
            print(runner_direction)

    print("after move")
    print(runner_list)
    print(runner_direction)
def find_seeker_next_move(turn):
    global seeker, seeker_locations

    # seeker's move repeats every 2 * (2 * (N - 1) + 1) turn
    turn %= (2 * (N ** 2) - 2)

    # Next location
    x, y = seeker
    dx, dy = seeker_locations[turn]
    # Next direction
    next_turn = (turn + 1) % (2 * (N ** 2) - 2)
    d = seeker_locations[next_turn]
    return x + dx, y + dy, d


def seek(turn):
    global seeker, runner_list, runner_direction
    score = 0

    # Find seeker's next location and direction
    x, y, d, = find_seeker_next_move(turn)
    seeker = (x, y)

    # Seek
    # 이동 직후 술래는 턴을 넘기기 전에 시야 내에 있는 도망자를 잡게 됩니다.
    # 술래의 시야는 현재 바라보고 있는 방향을 기준으로 현재 칸을 포함하여 총 3칸입니다
    for i in range(3):
        dx, dy = d
        nx, ny = x + dx * i, y + dy * i
        # 만약 나무가 놓여 있는 칸이라면, 해당 칸에 있는 도망자는 나무에 가려져 보이지 않게 됩니다.
        if (nx, ny) in runner_list and trees[nx][ny] == False:
            score += 1
            # 잡힌 도망자는 사라지게 되고
            indexes = []
            for idx, (x, y) in enumerate(runner_list.copy()):
                if (nx, ny) == (x, y):
                    runner_list.remove((x, y))
                    indexes.append(idx)
            for i in sorted(indexes, reverse=True):
                del runner_direction[i]
            # runner_list.remove((nx, ny))
            # runner_direction.pop((nx, ny))

    print("seeker")
    print(runner_list, runner_direction)
    print(x, y, d)
    ground = [[0] * (N + 1) for _ in range(N + 1)]
    ground[x][y] = 1
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            print(ground[x][y], end=" ")
        print()
    print("score", score)
    print("----------------")

    return (turn + 1) * score


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # print(f"test case: {test_case}", "="*15)

    # Get input
    get_input()

    # Hide and seek for K turns
    total_score = 0
    for turn in range(0, K):
        # 도망자 이동
        run()

        # 술래 이동
        total_score += seek(turn)

        print("total score", total_score)
        print(runner_list)
        print_matrix(runner_list, runner_direction)

        if turn == 1:
            break
    if test_case == 1:
        break

    print(total_score)

    collections.Counter
    collections.defaultdict


    # ///////////////////////////////////////////////////////////////////////////////////
