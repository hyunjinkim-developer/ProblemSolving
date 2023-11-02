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

N, M, P, C, D = -1, -1, -1, -1, -1
ground = list()
Rudolph = (-1, -1)
Santas = dict()
freeze = dict()

def print_matrix(matrix):
    for i in range(N):
        print(matrix[i][:N])

def get_input():
    global N, M, P, C, D
    global ground, Rudolph, Santas

    # ground size, turns, the number of santas, power of the rudolph, power of santas
    N, M, P, C, D = map(int, input().split())
    ground = [[0] * N for _ in range(N)]

    # Initial location of Rudolph
    Rudolph = tuple(map(int, input().split()))

    for _ in range(P):
        idx, r, c = map(int, input().split())
        ground[r - 1][c - 1] = idx
        Santas[idx] = (r, c, 0) # current location, socre

def find_distance(Santa, Rudolph):
    santa_r, santa_c = Santa
    rudolph_r, rudolph_c = Rudolph
    return (rudolph_r - santa_r) ** 2 + (rudolph_c - santa_c) ** 2

def find_target_santa():
    global Santas, Rudolph

    availables = dict()
    for idx, (x, y, score) in Santas.items():
        # 게임에서 탈락하지 않은 산타 중 가장 가까운 산타를 선택해야 합니다.
        if x == -1 and y == -1: continue

        availables[idx] = (find_distance((x, y), Rudolph), x, y)
    # 루돌프는 가장 가까운 산타를 향해 1칸 돌진합니다.
    # 만약 가장 가까운 산타가 2명 이상이라면, r 좌표가 큰 산타를 향해 돌진합니다.
    # r이 동일한 경우, c 좌표가 큰 산타를 향해 돌진합니다.
    # 루돌프는 기절한 산타를 돌진 대상으로 선택할 수 있습니다.
    def custom_sort(item):
        distance, santa_r, santa_c = item
        return distance, santa_r * -1, santa_c * -1
    sort_availables = sorted(availables.items(), key=lambda item: custom_sort(item[1]))

    distance, target_r, target_c = sort_availables[0][1]
    return (target_r, target_c)

def find_rudolph_next_move(santa_location):
    global Rudolph, N
    rudolph_r, rudolph_c = Rudolph
    next_r, next_c = -1, -1
    distance = (N ** 2) * 3 # intialize distance

    # dr, dc : upper left to clockwise
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for dr, dc, in directions:
        nr, nc = rudolph_r + dr, rudolph_c + dc
        new_distance_difference = find_distance(santa_location, (nr, nc))
        if distance > new_distance_difference:
            distance = new_distance_difference
            next_r, next_c = nr, nc
    return (next_r, next_c)

def rudolph_move():
    global Rudolph

    # Find target santa
    target = find_target_santa()

    # Find next rudolph locaion
    next_rudolph_location = find_rudolph_next_move(target)
    Rudolph = next_rudolph_location

    # 루돌프가 움직여서 충돌이 일어난 경우, 해당 산타는 C만큼의 점수를 얻게 됩니다.
    # 이와 동시에 산타는 루돌프가 이동해온 방향으로 C 칸 만큼 밀려나게 됩니다.

def in_range(r, c):
    global N
    return 1 <= r <= N and 1 <= c <= N

def find_santa_next_move(r, c):
    global Rudolph, ground

    current_distance_to_rudolph = find_distance((r, c), Rudolph)
    # 산타는 상하좌우로 인접한 4방향 중 한 곳으로 움직일 수 있습니다.
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    availables = list()
    for idx, (dr, dc) in enumerate(directions):
        nr, nc = r + dr, c + dc

        # 산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없습니다.
        if not in_range(nr, nc): continue
        if ground[nr - 1][nc - 1] != 0: continue

        # 움직일 수 있는 칸이 있더라도 만약 루돌프로부터 가까워질 수 있는 방법이 없다면 산타는 움직이지 않습니다.
        new_distance = find_distance((nr, nc), Rudolph)
        if new_distance > current_distance_to_rudolph: continue

        # 움직일 수 있는 칸이 없다면 산타는 움직이지 않습니다.
        availables.append([new_distance, idx, nr, nc])

    if len(availables) == 0:
        return (r, c)
    else:
        # 이때 가장 가까워질 수 있는 방향이 여러 개라면, 상우하좌 우선순위에 맞춰 움직입니다.
        def custom_sort(item):
            return item[0], item[1]
        sort_availables = sorted(availables, key=custom_sort)
        new_r, new_c = sort_availables[0][2], sort_availables[0][3]
        return (new_r, new_c)

def santas_move():
    global Santas, D, Rudolph, ground
    rudolph_r, rudolph_c = Rudolph

    for idx, (r, c, score) in Santas.items():
        # 기절했거나 이미 게임에서 탈락한 산타는 움직일 수 없습니다.
        if r == -1 and c == -1: continue
        if idx in freeze.keys(): continue

        # Find sanda's new location
        new_r, new_c = find_santa_next_move(r, c)

        # Collide with Rudolph
        # 산타와 루돌프가 같은 칸에 있게 되면 충돌이 발생합니다.
        if new_r == rudolph_r and new_c == rudolph_c:
            # 산타가 움직여서 충돌이 일어난 경우, 해당 산타는 D만큼의 점수를 얻게 됩니다.
            score += D
            # 이와 동시에 산타는 자신이 이동해온 반대 방향으로 D 칸 만큼 밀려나게 됩니다.
            diff_r, diff_c = r - rudolph_r, c - rudolph_c
            new_r, new_c = rudolph_r + (diff_r * D), rudolph_c + (diff_c * D)
            # 만약 밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락됩니다.
            if not in_range(new_r, new_c):
                new_r, new_c = -1, -1
            # 만약 밀려난 칸에 다른 산타가 있는 경우 상호작용이 발생합니다.

        # Update Santas and ground
        ground[r - 1][c - 1] = 0
        if not (new_r == -1 and new_c == -1):
            ground[new_r -1][new_c - 1] = idx
        Santas[idx] = (new_r, new_c, score)

    print(Santas)










# # Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    if test_case == 2:
        break
    print(f"test case: {test_case}")

    # get input
    get_input()

    for turn in range(1, M + 1):
        if turn == 2:
            break
        print(f"turn: {turn}")

        rudolph_move()
        print_matrix(ground)
        print(Rudolph)

        santas_move()
        # 만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료됩니다.
        # 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여합니다.
        alive = 0
        for idx, (r, c, score) in Santas.items():
            # 탈락한 산타들
            if r == -1 and c == -1: continue
            alive += 1
            score += 1
            Santas[idx] = (r, c, score)
        if alive == len(Santas):
            break
        print_matrix(ground)
        print(Santas)
        print(freeze)

    # 게임이 끝났을 때 각 산타가 얻은 최종 점수를 1번부터 P번까지 순서대로 공백을 사이에 두고 출력합니다.
    for idx, (r, c, score) in Santas.items():
        print(score, end=" ")

    # ///////////////////////////////////////////////////////////////////////////////////
