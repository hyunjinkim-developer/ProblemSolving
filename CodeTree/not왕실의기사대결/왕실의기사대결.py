

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
from copy import deepcopy

L = 0
board = []
knights = dict()
hp = []
commands = []
# d는 0, 1, 2, 3 중에 하나이며 각각 위쪽, 오른쪽, 아래쪽, 왼쪽 방향을 의미
dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def print_knights():
    global L, knights, board

    map = [[0] * (L + 1) for _ in range(L + 1)]
    for idx, (blocks, k) in knights.items():
        for r, c in blocks:
            map[r][c] = (idx)

    for r in range(1, L + 1):
        for c in range(1, L + 1):
            if board[r][c] == 2:
                print("*", end='\t')
            else:
                print(map[r][c], end='\t')
        print()


def get_input():
    global L, board, knights, hp, commands

    # Initialization
    L = 0
    board = []
    knights = dict()
    hp = []
    commands = []

    L, N, Q = map(int, input().split())

    # 0이라면 빈칸/ 1이라면 함정/ 2라면 벽을 의미
    board = [[0] * (L + 1)] # for easier indexing
    for _ in range(L):
        data = deque(list(map(int, input().split())))
        data.appendleft(0)
        board.append(list(data))

    #  (r,c,h,w,k) 순으로 주어지며,
    #  체스판의 왼쪽 상단은 (1,1)로 시작
    #  처음 위치는 (r,c)를
    #  좌측 상단 꼭지점으로 하며 세로 길이가 h, 가로 길이가 w인 직사각형 형태를 띄고 있으며
    #  초기 체력이 k
    for i in range(1, N + 1):
        r, c, h, w, k = map(int, input().split())
        blocks = []
        for row in range(h):
            for col in range(w):
                location = (r + row, c + col)
                blocks.append(location)
        knights[i] = (blocks, k)
        hp.append(k)

    for _ in range(Q):
        knight_idx, direction = map(int, input().split())
        commands.append((knight_idx, direction))


def movable(blocks, direction):
    global L, board, knights, dirs

    def in_range(r, c):
        return 1 <= r <= L and 1 <= c <= L

    dr, dc = dirs[direction]
    for block in blocks:
        r, c = block
        nr, nc = r + dr, c + dc
        # 체스판 밖도 벽으로 간주
        if not in_range(nr, nc):
            return False
        if board[nr][nc] == 2:
            return False
    return True

def move_blocks(attacker, knights_to_move, direction):
    global board, knights, dirs
    dr, dc = dirs[direction]

    # knights_to_move.append(attacker)
    for knight_idx in knights_to_move:
        blocks, k = knights[knight_idx]
        new_blocks = []
        damage = 0
        for r, c in blocks:
            nr, nc = r + dr, c + dc
            new_blocks.append((nr, nc))
            if knight_idx != attacker and board[nr][nc] == 1:
                damage += 1

        if k - damage <= 0:
            knights.pop(knight_idx)
        else:
            knights[knight_idx] = (new_blocks, k - damage)


def find_move_knight(attacker, direction, knights_to_move):
    global knights, dirs

    current_blocks, current_k = knights[attacker]
    r, c = current_blocks[0]
    dr, dc = dirs[direction]
    moved_blocks = [(r + dr, c + dc) for r, c in current_blocks]
    checked_knights = 0
    if movable(moved_blocks, direction):
        print('h')
        if DEBUG == True:
            print(f"new loc: {moved_blocks}")  #d

        for k_idx in knights.keys():
            if k_idx == attacker: continue

            blocks, k = knights[k_idx]
            print(f"key: {k_idx} {blocks} {k}")  #d
            if set(moved_blocks).intersection(set(blocks)): # adjacent knight
                print(f'target: {k_idx}') #d
                if movable(blocks, direction):
                    knights_to_move.append(k_idx)
                    find_move_knight(k_idx, direction, knights_to_move)
                else:
                    return
            else:
                checked_knights += 1

    # No knights nearby
    if checked_knights == len(knights) - 1:
        knights_to_move.append(attacker)

def calculate_damage():
    global knights, hp
    answer = 0

    for knight_idx in knights.keys():
        blocks, k = knights[knight_idx]
        answer += (hp[knight_idx - 1] - k)

    return answer


def run_commands():
    global commands, knights

    for idx, (attacker, direction) in enumerate(commands):
        if DEBUG == True:
            if idx == 6:
                break
            print(f"command {idx}: {attacker, dirs[direction]}")  #d
        knights_to_move = []
        find_move_knight(attacker, direction, knights_to_move)
        if knights_to_move != []:
            knights_to_move.append(attacker)
            knights_to_move = list(set(knights_to_move))
        move_blocks(attacker, knights_to_move, direction)

        if DEBUG == True:
            print(f"knights to move: {knights_to_move}")
            print(f"command completed: {knights}")
            print_knights()
            print('-' * 20)


def main():
    get_input()
    run_commands()
    print(calculate_damage())

'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''

# # Comment below before submission
import sys
sys.stdin = open("input.txt", "r")
#debug
DEBUG = True

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # main()

    if DEBUG == True:
        print(f"test case: {test_case}", "=" * 30)
        if test_case == 3:
            main()
        else:
            get_input()
    # ///////////////////////////////////////////////////////////////////////////////////
