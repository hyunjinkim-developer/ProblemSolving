"""
# 문제의 Point
* Roll dice in given direction
    Data structure to save dice's bottom, L, R, U, D side for each rolling
    - dice_bottom := int
    - dice := dictionary key: "L", "R", "U", "D", value: number of each side based on dice_bottom
* Count adjacent locations that has the same board score as dice_bottom
    Use BFS algorithm implementing with deque()
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

total_score = 0

n, m = 0, 0
board = []
r, c = 0, 0 # dice location
dice = dict()
dice_bottom = -1

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # from up in clockwise

def print_list(board):
    global n

    for r in range(n):
        for c in range(n):
            print(board[r][c], end='\t')
        print()
    print('-'*10)


def get_input():
    global n, m, board, dice_bottom, dice, total_score

    # Initialization
    total_score = 0
    n, m = 0, 0
    board = []
    dice_bottom = 6 # bottom of the dice
    dice = {"U": 5, "D": 2, "L": 4,"R": 3} # up, down, left, right of the dice

    n, m = map(int, input().split())
    for _ in range(n):
        board.append(list(map(int, input().split())))


def in_range(r, c):
    global n
    return 0 <= r < n and 0 <= c < n


def roll_dice(direction):
    global dice, dice_bottom
    new_dice_bottom = -1

    # Check movable_direction
    # if next position is located outside the ground
    #   move into opposite direction
    def movable_direction(direction):
        global r, c
        if direction == "R":
            if in_range(r, c + 1):
                r, c = r, c + 1
                return "R"
            else:
                r, c = r, c - 1
                return "L"
        elif direction == "L":
            if in_range(r, c - 1):
                r, c = r, c - 1
                return "L"
            else:
                r, c = r, c + 1
                return "R"
        elif direction == "U":
            if in_range(r - 1, c):
                r, c = r - 1, c
                return "U"
            else:
                r, c = r + 1, c
                return "D"
        elif direction == "D":
            if in_range(r + 1, c):
                r, c = r + 1, c
                return "D"
            else:
                r, c = r - 1, c
                return "U"
    moved_direction = movable_direction(direction)
    if DEBUG:
        print(f"moved_direction: {direction}")

    # Roll dice 1 step
    if moved_direction == "R":
        new_dice_bottom = dice["R"]
        dice["R"] = 7 - dice_bottom
        dice["L"] = dice_bottom
    elif moved_direction == "L":
        new_dice_bottom = dice["L"]
        dice["R"] = dice_bottom
        dice["L"] = 7 - dice_bottom
    elif moved_direction == "U":
        new_dice_bottom = dice["U"]
        dice["U"] = 7 - dice_bottom
        dice["D"] = dice_bottom
    elif moved_direction == "D":
        new_dice_bottom = dice["D"]
        dice["U"] = dice_bottom
        dice["D"] = 7 - dice_bottom

    if DEBUG:
        print("Roll dice", "*"*10)
        print(f"location -> {r, c}")
        print(f"bottom: {dice_bottom} -> {new_dice_bottom}")
        print(dice)

    # Save dice_bottom after the dice rolled for 1 step
    dice_bottom = new_dice_bottom
    return moved_direction


def add_score(r, c):
    # Get score where the dice is on
    # Find the number of adjacent location with the same score
    global n, board, dirs

    target_score = board[r][c]
    count = 1 # Count includes current location

    visited = [[False] * n for _ in range(n)]
    visited[r][c] = True

    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if board[nr][nc] != target_score: continue
            if visited[nr][nc]: continue

            count += 1
            visited[nr][nc] = True
            q.append((nr, nc))

    if DEBUG:
        print("Add score", "*"*10)
        print(f"count: {count}")
        print_list(board)
    return target_score * count


def find_direction(r, c, direction):
    global board, dice_bottom

    if DEBUG:
        print(f"Find next direction:", "*"*5)
        print(f"prev_dir: {direction}/ board: {board[r][c]}/ dice_bottom: {dice_bottom}")

    def find_next_direction(direction, clockwise):
        direction_list = ["U", "R", "D", "L"]
        direction_idx = -1
        for direction_idx, d in enumerate(direction_list):
            if direction == d:
                break

        if clockwise:
            return direction_list[(direction_idx + 1) % 4]
        else:
            return direction_list[(direction_idx - 1) % 4]

    board_score = board[r][c]
    # if board < bottom of the dice
    #   rotate 90 degree in clockwise
    if board_score < dice_bottom:
        return find_next_direction(direction, clockwise=True)
    # if bottom of the dice < board
    #   rotate 90 degree in counter-clockwise
    elif board_score > dice_bottom:
        return find_next_direction(direction, clockwise=False)
    # if bottom of the dice == board
    #   same as previous direction
    else:
        return direction


def solution():
    global m, r, c, dice_bottom, total_score

    if DEBUG:
        global r, c
        print(f"previous r, c: {r, c}")


    # First turn
    # dice on (0, 0), move to right
    if DEBUG:
        print("First turn", "*"*10)
    r, c = 0, 0
    direction = roll_dice("R")

    # Add score
    total_score += add_score(r, c)

    for _ in range(1, m):
        if DEBUG:
            print("="*20)

        # Find next direction
        #   based on comparison between board score and dice bottom
        next_direction = find_direction(r, c, direction)
        if DEBUG:
            print(f"next direction: {next_direction}")
        # Roll dice in movable direction
        #   next direction can be different from moved direction
        #   if the next location is out of board
        moved_direction = roll_dice(next_direction)

        # Get score
        total_score += add_score(r, c)

        # Update direction
        direction = moved_direction

    return total_score


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

DEBUG = False # For submission
# DEBUG = True

# Answer
# 44
# 4836
# 30
# 40


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    get_input()

    if DEBUG:
        print(f"test case: {test_case}", "="*30)
        print(solution())

        if test_case == 1:
            break

    # ///////////////////////////////////////////////////////////////////////////////////
    # Samsung Coding Test style output
    answer = solution()
    print("#%d:" % test_case, answer)
