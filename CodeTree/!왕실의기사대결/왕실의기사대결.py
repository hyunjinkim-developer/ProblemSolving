"""
# 이 문제의 포인트
* collections.deque()를 활용한 BFS
    * 1) 명령으로 주어진 방향으로 이동했을 때 인접한 위치에 기사가 있다면 recursive하게 이동해서 (삼성 빈출 유형)
        - 해당 방향으로 이동이 가능한지를 확인함과 동시에
        - 이동해야 하는 기사들의 id를 저장
      2) 이동 가능한 기사들을 실제 이동하면서 이동한 위치, 체력 정보를 업데이트
    * 벽을 만나면 recursive한 모든 이동이 일어나지 않는다고 하였는데
        벽 :=
        - land 값이 2이거나,
        - land를 벗어나는 경우 라고 했기 때문에
        land = [[0 for _ in range(L + 1] for _ in range(L + 1)]로 정의해서
        주어진 land의 바깥을 둘러서 2로 정의
    * 해당 위치에 기사가 존재하는지 알기 위해서
        knights_map (2-dimensional array)의 (r, c)의 위치에 존재하는 id번호를 저장
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

L = 0
land = []
# 1이라면 함정을 의미합니다.
TRAP = 1
# 2라면 벽을 의미합니다.
WALL = 2
knights = dict()
knights_original_hp = dict()
knights_map = []
orders = []
# d는 0, 1, 2, 3 중에 하나이며 각각 위쪽, 오른쪽, 아래쪽, 왼쪽 방향을 의미
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def print_land():
    global L, land
    for r in range(L + 2):
        for c in range(L + 2):
            print(land[r][c], end='\t')
        print()
    print("-"*10)

def print_map():
    global L, knights_map
    for r in range(1, L + 1):
        for c in range(1, L + 1):
            print(knights_map[r][c], end='\t')
        print()
    print("-"*10)

def print_knights():
    global knights
    keys = sorted(knights.keys())
    for k in keys:
        print(f"{k}:", knights[k])

def get_input():
    global L, land, knights, knights_original_hp, knights_map, orders

    # Initialization
    L, land = 0, []
    knights = dict()
    knights_original_hp = dict()
    knights_map = []
    orders = []

    L, N, Q = map(int, input().split())

    # land
        # 0이라면 빈칸을 의미합니다.
        # 1이라면 함정을 의미합니다.
        # 2라면 벽을 의미합니다.
        # 체스판 밖도 벽으로 간주
    # Make wall around given land
    land.append([2] * (L + 2))
    for _ in range(L):
        # 체스판의 왼쪽 상단은 (1,1)로 시작
        row = [2]
        row.extend(list(map(int, input().split())))
        row.append(2)
        land.append(row)
    land.append([2] * (L + 2))

    # knights
    knights_map = [[0] * (L + 1) for _ in range(L + 1)]
    # 1번 기사부터 N번 기사
    for id in range(1, N + 1):
        # (r,c,h,w,k) 순으로 주어지며,
            # 이는 기사의 처음 위치는 (r,c)를 좌측 상단 꼭지점으로 하며
            # 세로 길이가 h, 가로 길이가 w인 직사각형 형태를 띄고 있으며
            # 초기 체력이 k라는 것을 의미
        r, c, h, w, k = map(int, input().split())
        info = dict()
        loc = list()
        for dr in range(h):
            nr = r + dr
            for dc in range(w):
                nc = c + dc
                loc.append((nr, nc))
                knights_map[nr][nc] = id
        info["loc"] = loc
        info["hp"] = k
        knights[id] = info
        # Save original hp to calculate tatal damage of survivors
        knights_original_hp[id] = k

    # orders
    for _ in range(Q):
        # (i,d) 형태로 주어지며
            # 이는 i번 기사에게 방향 d로 한 칸 이동하라는 명령
            #  i는 1 이상 N 이하의 값을 갖으며, 이미 사라진 기사 번호가 주어질 수도 있음에 유의합니다.
            # d는 0, 1, 2, 3 중에 하나이며 각각 위쪽, 오른쪽, 아래쪽, 왼쪽 방향을 의미
        i, d = map(int, input().split())
        orders.append((i, d))

    if DEBUG:
        # print_land()
        print("knights:")
        print_knights()
        print_map()
        print(f"orders: {orders}")


def find_movable_knights(knight_id, d):
    # 명령을 받은 기사가 이동 가능한지 확인
    # 이동 가능한 경우 연쇄적으로 이동해야 하는 기사들의 id 저장

    # 또, 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 됩니다.
    global knights, dirs, land, WALL, knights_map
    dr, dc = dirs[d]

    # Debugging Technique
    DEBUG_find_movable_knights = False and DEBUG

    q = deque()
    q.append(knight_id)
    knights_to_move = set()
    while q:
        id = q.popleft()
        # 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 됩니다.
        if id not in knights.keys(): continue

        loc = knights[id]["loc"]
        for (r, c) in loc:
            # 왕에게 명령을 받은 기사는 상하좌우 중 하나로 한 칸 이동
            nr, nc = r + dr, c + dc

            if DEBUG_find_movable_knights:
                print(nr, nc)

            # 만약 기사가 이동하려는 방향의 끝에 벽(체스판 밖도 벽으로 간주)이 있다면
            # 모든 기사는 이동할 수 없게 됩니다.
            if land[nr][nc] == WALL:
                if DEBUG:
                    print("no movable knights", "*"*10)
                if DEBUG_find_movable_knights:
                    print("벽", nr, nc)
                return []
            if knights_map[nr][nc] == 0:
                if DEBUG_find_movable_knights:
                    print("빈자리", nr, nc)
                continue
            if knights_map[nr][nc] == id:
                if DEBUG_find_movable_knights:
                    print("같은거", nr, nc)
                continue

            q.append(knights_map[nr][nc])
            if DEBUG_find_movable_knights:
                print("인접 id", knights_map[nr][nc], ":", nr, nc)
                print(q)
        knights_to_move.add(id)

        if DEBUG_find_movable_knights:
            print('-'*10)

    if DEBUG:
        print(f"find_movable_knights: {knights_to_move}", "="*10)

    return knights_to_move


def move_knights(d, attacker_id, movable_knights):
    global dirs, knights, L, knights_map, land

    if len(movable_knights) == 0:
        return

    # 움직일 수 있는 기사가 존재하는 경우
    dr, dc = dirs[d]
    new_knights_map = [[0 for _ in range(L + 1)] for _ in range(L + 1)]
    # * 단, 명령을 받은 기사는 피해를 입지 않으며,
    attacker_loc = knights[attacker_id]["loc"]
    for idx, (r, c) in enumerate(attacker_loc):
        nr, nc = r + dr, c + dc
        attacker_loc[idx] = (nr, nc)

        # Update knights_map
        new_knights_map[nr][nc] = attacker_id
    knights[attacker_id]["loc"] = attacker_loc

    # 각 기사들은 해당 기사가 이동한 곳에서 w×h 직사각형 내에 놓여 있는 함정의 수만큼만 피해를 입게
    # 각 기사마다 피해를 받은 만큼 체력이 깎이게 되며, 현재 체력 이상의 대미지를 받을 경우 기사는 체스판에서 사라지게 됩니다.
    dead_knights = []
    for id in movable_knights:
        if id == attacker_id: continue

        loc = knights[id]["loc"]
        hp = knights[id]["hp"]
        for idx, (r, c) in enumerate(loc):
            nr, nc = r + dr, c + dc
            loc[idx] = (nr, nc)
            # Update knights_map
            new_knights_map[nr][nc] = id

            # * 밀렸더라도 밀쳐진 위치에 함정이 전혀 없다면 그 기사는 피해를 전혀 입지 않게 됨에 유의
            if land[nr][nc] == TRAP:
                hp -= 1
        knights[id]["loc"] = loc
        knights[id]["hp"] = hp
        if hp <= 0:
            dead_knights.append(id)

    # Remove dead knights
    for id in dead_knights:
        loc = knights[id]["loc"]
        for r, c in loc:
            new_knights_map[r][c] = 0
        knights.pop(id)

    # Replace knights_map
    # Save knights that are not moved
    for id in knights.keys():
        if id not in movable_knights:
            loc = knights[id]["loc"]
            for r, c in loc:
                new_knights_map[r][c] = knights_map[r][c]
    knights_map = new_knights_map

    if DEBUG:
        print("move knights:", "*"*10)
        print_knights()
        print_map()


def calculate_total_damage():
    global knights, knights_original_hp
    total_damage = 0

    for id in knights.keys():
        hp = knights[id]["hp"]
        total_damage += (knights_original_hp[id] - hp)
    return total_damage

def solution():
    global orders

    for turn, (knight_id, d) in enumerate(orders):
        if DEBUG:
            print(f"turn: {turn}", "=" * 10)
            # if turn == 2:
            #     break


        # (1) 기사 이동
        movable_knights = find_movable_knights(knight_id, d)

        # (2) 대결 대미지
        move_knights(d, knight_id, movable_knights)

    # Q 번의 대결이 모두 끝난 후
    # 생존한 기사들이 총 받은 대미지의 합을 출력하는 프로그램을 작성
    print(calculate_total_damage())

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
# Answer
# 3

DEBUG = False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    get_input()


    # if DEBUG:
    #     print(f"test case: {test_case}", "="*50)
    #     solution()

    solution()
    # ///////////////////////////////////////////////////////////////////////////////////
