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


R, C = 0, 0
K = 0
rockets = dict()
planet = []
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # from up in clockwise
answer = 0

def print_dict(dictionary):
    for i in range(len(dictionary)):
        print(f"{i} : {dictionary[i]}")
    print("-"*10)

def print_list(planet):
    global R, C

    for r in range(R):
        for c in range(C):
            print(planet[r][c], end="\t")
        print()

def get_input():
    global R, C, K, rockets, planet, answer

    # Initialize
    R, C = 0, 0
    K = 0
    planet = []
    answer = 0

    R, C, K = map(int, input().split())
    for i in range(K):
        # exit_dir : 숫자 0,1,2,3은 북, 동, 남, 서쪽
        start_col, exit_dir = map(int, input().split())
        rockets[i] = tuple((start_col - 1, exit_dir)) # Input start_columns starts from 1
    planet = [[-1] * C for _ in range(R)]


def in_range(r, c):
    global R, C
    return r < R and 0 <= c < C

def move_robot_to_the_bottom(start_r, start_c, exit_d):
    # Move robot which located in the center of the rocket
    # to the biggest column
    global planet, R, C, dirs, rockets
    # If there's no adjacent rocket
    dest_r = start_r + 1 # lowest location from the target robot

    # Initialize visited
    visited = [[False] * C for _ in range(R)]
    def mark_visited(start_r, start_c):
        nonlocal visited
        visited[start_r][start_c] = True
        for dr, dc in dirs:
            nr, nc = start_r + dr, start_c + dc
            visited[nr][nc] = True
    mark_visited(start_r, start_c)

    # Initialize queue
    q = deque()
    exit_dr, exit_dc = dirs[exit_d]
    start_exit_r, start_exit_c = start_r + exit_dr, start_c + exit_dc
    q.append((start_exit_r, start_exit_c))
    # Move robot recursively to find the biggest column
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C): continue
            if visited[nr][nc]: continue
            if planet[nr][nc] == -1: continue # planet is vacent

            # Find adjacent rocket number with planet
            adj_rocket_no = planet[nr][nc]
            (adj_center_r, adj_center_c), adj_exit_d = rockets[adj_rocket_no]
            dest_r = max(dest_r, adj_center_r + 1)
            mark_visited(adj_center_r, adj_center_c)

            # Find exit of the rocket with rockets
            exit_dr, exit_dc = dirs[adj_exit_d]
            adj_exit_r, adj_exit_c = adj_center_r + exit_dr, adj_center_c + exit_dc
            q.append((adj_exit_r, adj_exit_c))

    return dest_r

def clear_planet():
    global planet
    planet = [[-1] * C for _ in range(R)]

def move_rocket(start_r, start_c, exit_d):
    def movable(center_r, center_c):
        global planet, C, dirs

        if not in_range(center_r, center_c): return False
        if 0 <= center_r < R and planet[center_r][center_c] != -1: return False
        for dr, dc in dirs:
            nr, nc = center_r + dr, center_c + dc
            if not in_range(nr, nc): return False
            if 0 <= nr < R and planet[nr][nc] != -1: return False
        return True

    # 1) Move south
    if movable(start_r + 1, start_c):
        return start_r + 1, start_c, exit_d

    # 2) Move West -> Rotate counterclockwise -> Move South
    if movable(start_r, start_c - 1) and movable(start_r + 1, start_c - 1):
        return start_r + 1, start_c - 1, (exit_d - 1) % 4

    # 3) Move East -> Rotate clockwise -> Move South
    if movable(start_r, start_c + 1) and movable(start_r + 1, start_c + 1):
        return start_r + 1, start_c + 1, (exit_d + 1) % 4

    # Cant' move in 1), 2), 3)
    return start_r, start_c, exit_d

def drop_rocket(rocket_no):
    global rockets, planet, dirs, answer

    start_c, exit_d = rockets[rocket_no]
    center_r, center_c = -1, -1 # Rocket's center location

    # Move rockets recursively until no more ways to move
    prev_r, prev_c, prev_d = -2, start_c, exit_d # Initialize center location: (start_r, -2)
    while True:
        center_r, center_c, exit_d = move_rocket(prev_r, prev_c, prev_d)
        if center_r == prev_r and center_c == prev_c:
            break
        prev_r, prev_c, prev_d = center_r, center_c, exit_d

    # If the center is located outside the planet
    if center_r - 1 < 0:
        clear_planet()
        # Save center location and direction
        rockets[rocket_no] = ((-100, center_c), exit_d)
        return

    # Save center location and direction
    rockets[rocket_no] = ((center_r, center_c), exit_d)
    # Save rocket's location on planet
    planet[center_r][center_c] = rocket_no
    for dr, dc in dirs:
        nr, nc = center_r + dr, center_c + dc
        planet[nr][nc] = rocket_no

    # Move robot inside the rocket to the biggest column
    c = move_robot_to_the_bottom(center_r, center_c, exit_d)
    answer += (c + 1)


def solution():
    global rockets, answer

    get_input()
    for rocket_no in range(K):
        drop_rocket(rocket_no)
    print(answer)





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
# answer
# 50
# 38
# 29
# 37


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    solution()
    # ///////////////////////////////////////////////////////////////////////////////////
