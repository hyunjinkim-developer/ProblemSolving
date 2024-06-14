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

from collections import deque, defaultdict


answer = 0
t = -1, -1
pacman = (-1, -1)
grid = [] # 3-dimensional array contains monster's direction
eggs = deque() # (r, c, d)
dead = defaultdict(list) # key: location of dead monsters, value: time limit

m_dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)] # 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
p_dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상-좌-하-우


def print_grid(grid):
    for r in range(4):
        for c in range(4):
            print(grid[r][c], end='\t')
        print()
    print('-'*10)


def print_dict(dictionary):
    for key in dictionary.keys():
        print(key, ":", dictionary[key])

def get_input():
    global answer, t, pacman, grid, eggs, dead

    # Initialization
    answer = 0
    m, t = -1, -1
    pacman = (-1, -1)
    eggs = deque()  # (r, c, d)
    # 3-dimensional array contains monster's direction
    # grid = []
    # for row in range(4):
    #     grid_row = []
    #     for col in range(4):
    #         grid_row.append([])
    #     grid.append(grid_row)
    grid = [[ [] for c in range(4)]for r in range(4)]
    dead = defaultdict(list)  # key: location of dead monsters, value: time limit

    m, t = map(int, input().split())
    # Pacman location
    r, c = map(int, input().split())
    pacman = (r - 1, c - 1)
    # Monster location
    # 몬스터의 초기 위치와 팩맨의 초기 위치는 같을 수도 있습니다.
    for _ in range(m):
        # 방향 d는 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
        r, c, d = map(int, input().split())
        grid[r - 1][c - 1].append(d - 1) # direction index starts from 0


def in_range(r, c):
    return 0 <= r < 4 and 0 <= c < 4

def create_egg():
# 몬스터 복제 시도
    # 현재의 위치에서 자신과 같은 방향을 가진 몬스터를 복제
    # 복제된 몬스터는 아직은 부화되지 않은 상태로 움직이지 못합니다.
    # 복제된 몬스터는 현재 시점을 기준으로 각 몬스터와 동일한 방향을 지니게 되며,
    # 이후 이 알이 부화할 시 해당 방향을 지닌 채로 깨어나게 됩니다.
    global grid, eggs

    for r in range(4):
        for c in range(4):
            if len(grid[r][c]) == 0: continue
            for d in grid[r][c]:
                eggs.append((r, c, d))

    if DEBUG:
        print("create_egg:")
        print(eggs)


def monster_move():
    # 몬스터 이동
    global grid

    def movable(nr, nc):
        # 격자를 벗어나는 방향일 경우
        if not in_range(nr, nc): return False
        # 움직이려는 칸에 몬스터 시체가 있거나
        if (nr, nc) in dead.keys(): return False
        # 팩맨이 있는 경우거나
        if (nr, nc) == pacman: return False
        return True

    def move(r, c, d):
        global m_dirs, dead, pacman
        nr, nc, nd = -1, -1, -1

        # 현재 자신이 가진 방향대로 한 칸 이동
        cur_dr, cur_dc = m_dirs[d]
        r_cur_d, c_cur_d = r + cur_dr, c + cur_dc
        if movable(r_cur_d, c_cur_d):
            return r_cur_d, c_cur_d, d
        else:
        # 반시계 방향으로 45도를 회전한 뒤 해당 방향으로 갈 수 있는지 판단
            for i in range(1, 8):
                nd = (d + i) % 8
                dr, dc = m_dirs[nd]
                nr, nc = r + dr, c + dc
                if not movable(nr, nc): continue
                return nr, nc, nd
        # 만약 8 방향을 다 돌았는데도 불구하고, 모두 움직일 수 없었다면 해당 몬스터는 움직이지 않습니다.
        return r, c, d

    moved_grid = [[ [] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            if len(grid[r][c]) == 0: continue
            for d in grid[r][c]:
                nr, nc, nd = move(r, c, d)
                moved_grid[nr][nc].append(nd)

                # if DEBUG:
                #     print(f"{r, c, d} -> {nr, nc, nd}")
    grid = moved_grid

    if DEBUG:
        print("monster move:", '*'*10)
        print_grid(grid)


def pacman_move():
    # 팩맨 이동
    global pacman, p_dirs, grid, dead
    paths = defaultdict(list)  # key: dead, value: paths [(r1, c1), (r2, c2), (r3, c3)], ... ]
    r, c = pacman

    # 총 3칸을 이동, 각 이동마다 상하좌우의 선택지
    def bfs(dead_count, path, r, c):
        nonlocal paths

        if len(path) == 3:
            # if DEBUG:
            #     print(dead_count, path, r, c)

            # path is the same object, keep changing as recursively run bfs()
            paths[dead_count].append(path.copy())
            return

        for idx, (dr, dc) in enumerate(p_dirs): # 상-좌-하-우
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc]: continue

            visited[nr][nc] = True
            path.append(idx)
            dead_count += len(grid[nr][nc])

            bfs(dead_count, path, nr, nc)

            visited[nr][nc] = False
            path.pop()
            dead_count -= len(grid[nr][nc])

    # 팩맨은 알은 먹지 않으며,
    # 움직이기 전에 함께 있었던 몬스터도 먹지 않습니다.
    visited = [[False] * 4 for _ in range(4)]
    visited[r][c] = True # pacman location
    for idx, (dr, dc) in enumerate(p_dirs): # 상-좌-하-우
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        if visited[nr][nc]: continue

        visited[nr][nc] = True
        dead_count, path = len(grid[nr][nc]), [idx]

        bfs(dead_count, path, nr, nc)

        visited[nr][nc] = False

    if DEBUG:
        print("pacman paths: ", "*"*10)
        print_dict(paths)


    # 몬스터를 가장 많이 먹을 수 있는 방향으로 움직이게
    max_dead = max(paths.keys())
    # 상-좌-하-우의 우선순위를 가지며
        # 우선순위가 높은 순서대로 배열하면 "상상상 - 상상좌 - 상상하 - 상상우 - 상좌상 - 상좌좌 - 상좌하 - ..."
    max_dead_available_paths = paths[max_dead]
    def custom_sort(item):
        d1, d2, d3 = item
        return d1, d2, d3
    max_dead_paths = sorted(max_dead_available_paths, key=custom_sort)[0]
    if DEBUG:
        print("max dead paths:")
        # print(max_dead_available_paths)
        print(max_dead_paths)

    # 이동하는 칸(과정)에 있는 몬스터는 모두 먹어치운 뒤, 그 자리에 몬스터의 시체를 남깁니다.
    new_r, new_c = r, c
    for d in max_dead_paths:
        dr, dc = p_dirs[d]
        new_r, new_c = new_r + dr, new_c + dc
        # 그 자리에 몬스터의 시체를 남깁니다.
        dead_count = len(grid[new_r][new_c])
        for _ in range(dead_count):
            dead[(new_r, new_c)].append(2)
        # 이동하는 칸(과정)에 있는 몬스터는 모두 먹어치움
        grid[new_r][new_c] = []
    # 팩맨의 위치 저장
    pacman = (new_r, new_c)

    if DEBUG:
        print("몬스터를 먹어 치움:")
        print_dict(dead)
        print_grid(grid)


def destroy():
    # 몬스터 시체 소멸
    # 몬스터의 시체는 총 2턴동안만 유지
    global dead

    spots_cleaned = []
    for key in dead.keys():
        dead_monsters = dead[key] # before removing dead monsters
        dead_removed = [] # after removing dead monsters
        for prev_time_limit in dead_monsters:
            time_limit = prev_time_limit - 1
            # Current monster is completely destroyed
            if 0 < time_limit:
                dead_removed.append(time_limit) # pop with index
        # All monsters are completely destroyed
        if len(dead_removed) == 0:
            spots_cleaned.append(key)
        else:
            dead[key] = dead_removed
    # Clean spots where's no debris of dead monsters
    for r, c in spots_cleaned:
        dead.pop((r, c))


    if DEBUG:
        print("destroy dead monsters:", "*"*10)
        print_dict(dead)


def egg_to_monster():
    # 몬스터 복제 완성
    # 처음 복제가 된 몬스터의 방향을 지닌 채로 알 형태였던 몬스터가 부화
    global eggs, grid

    while eggs:
        r, c, d = eggs.popleft()
        grid[r][c].append(d)

    if DEBUG:
        print("egg to monster:", "*"*10)
        print_grid(grid)


def count_survivors(answer):
    global grid

    for r in range(4):
        for c in range(4):
            answer += len(grid[r][c])
    return answer


def solution():
    # t개의 턴이 지난 이후 격자에 살아남은 몬스터는 총 몇 마리인지 출력
    global t, answer

    for turn in range(t):
        if DEBUG:
            print(f"turn: {turn}", "="*20)
            if turn == 2:
                break

        # 몬스터 복제 시도
        create_egg()

        # 몬스터 이동
        monster_move()

        # 팩맨 이동
        pacman_move()

        # 몬스터 시체 소멸
        destroy()

        # 몬스터 복제 완성
        egg_to_monster()

    # Count survived monsters
    answer = count_survivors(answer)
    print(answer)
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
DEBUG = False
# answer
# 10
# 6
# 8


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    get_input()

    if DEBUG:
        if test_case == 1:
            print(pacman)
            print_grid(grid)
            print(f"test case: {test_case}", "="*50)
            solution()

    solution()
    # ///////////////////////////////////////////////////////////////////////////////////
