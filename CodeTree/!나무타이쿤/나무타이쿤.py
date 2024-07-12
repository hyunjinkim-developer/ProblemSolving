"""
# 문제의 Point
* 문제를 잘 읽기!
    - move_nutrients()에서
        - 문제 조건에 따른 풀이
        0 0 0 0 0                   0 0 0 0 0
        0 0 0 0 0                   * 0 0 0 0
        0 0 0 0 0    이동 방향:2(↗)    0 0 0 0 0
        0 0 0 0 0    이동 칸수: 3      0 0 0 0 0
        0 0 * 0 0                   0 0 0 0 0
        '격자의 모든 행,열은 각각 끝과 끝이 연결되어
        격자 바깥으로 나가면 마치 지구가 둥근것처럼 반대편으로 돌아옵니다.'
        라는 부분이 뭘 의미하는지, 문제에 주어진 예제를 잘 읽었다면 굉장히 간단한 문제였음

* (직관적으로 떠오르는) '격자 바깥으로 나가면 마치 지구가 둥근것처럼 반대편으로 돌아옵니다.'의 이동 방식 구현하기!
        - !!! 직관적이 이동방식에 따른 풀이
        0 0 0 0 0                         0 0 0 0 0
        0 0 0 0 *                         0 0 0 0 0
        0 0 0 0 0     ↗ 방향, 9움직인다면     0 0 0 0 0
        0 0 0 0 0                         0 0 0 0 0
        0 0 0 0 0                         0 * 0 0 0
            * 가로, 세로로 이동하는 경우
                nr = (r + (dr * steps)) % n
                nc = (c + (dc * steps)) % n
            * 대각선으로 이동하는 경우
                * 같은 대각선 위에 움직이는 원소들 간의 관계 파악
                * -> 같은 대각선에서 몇 번 움직일 수 있는지(available_steps) 파악
                - 오른쪽 아래 방향 대각선
                    같은 대각선에 위치하면 r - c 값이 일정하다
                * 0 0 0 0
                0 * 0 0 0 -4
                0 0 * 0 0 -3
                0 0 0 * 0 -2
                0 0 0 0 * -1
                 4 3 2 1 0

                - 오른쪽 위 방향 대각선
                    같은 대각선에 위치하면 r + c 값이 일정하다
                  0 1 2 3 4
                0 0 0 0 * 5
                0 0 0 * 0 6
                0 0 * 0 0 7
                0 * 0 0 0 8
                * 0 0 0 0

                * 실제 움직여야하는 횟수 파악
                    steps %= available_steps

                * 실제 이동
                    * land의 안에서 이동할 수 있는 경우
                        nr, nc = r + (dr * steps), c + (dc * steps)

                    * 중요! land의 범위 안에서 이동할 수 없는 경우
                        !! 1) 최대 범위 파악 (range_r, range_c)
                            land의 범위를 넘어서 이동하는 경우
                            같은 방향으로 이동했을 때 도착하게 되는 반대편의 위치 파악
                            !!! 움직이는 방향에 따라 도착하게 되는 반대 편의 위치가 달라짐에 유의
                            0 0 0 0 0                    0 0 0 0 0
                            0 0 0 0 *                    0 0 0 0 0
                            0 0 0 0 0     ↗ 방향 이라면     0 0 0 0 0
                            0 0 0 0 0                    0 0 0 0 0
                            0 0 0 0 0                    0 0 0 0 0
                                                         *  이 위치 파악
                        ! 2) 범위를 넘어서 주어진 방향으로 계속 이동할 때 좌표 파악 (diff_r, diff_c)
                            (1, 4)에서 ↗ 방향으로, 9만큼 움직인다면
                            available_steps은 1 이므로
                            0 0 0 0 0                    0 0 0 0 0 * 이 위치(nr, nc)로 이동하게 될 것
                            0 0 0 0 *                    0 0 0 0 0
                            0 0 0 0 0     ↗ 방향 이라면     0 0 0 0 0
                            0 0 0 0 0                    0 0 0 0 0
                            0 0 0 0 0                    0 0 0 0 0
                            diff_r, diff_c = nr - r, nc - c
                        ! 3) 실제 이동하게 되는 위치 파악
                            nr, nc = range_r + diff_r, range_c + diff_c
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

n = 0
land = []
move_rules = []
# 이동 방향의 경우 0번부터 7번까지 → ↗ ↑ ↖ ← ↙ ↓ ↘
move_rules_dirs = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
diagonal_dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)] # from upper left in clockwise
nutrients_loc = []

def get_input():
    global n, land, move_rules, nutrients_loc

    # Initialization
    n = 0
    land = []
    move_rules = []
    nutrients_loc = []

    n, m = map(int, input().split())
    # 리브로수의 높이
    for _ in range(n):
        land.append(list(map(int, input().split())))
    # 각 년도의 이동 규칙
    for _ in range(m):
        # 이동 방향 d: d는 0번부터 7번까지 각각 → ↗ ↑ ↖ ← ↙ ↓ ↘
        # 이동 칸 수 p
        d, p = map(int, input().split())
        move_rules.append((d - 1, p))


def print_list(array):
    global n
    for r in range(n):
        for c in range(n):
            print(array[r][c], end='\t')
        print()
    print('-'*5)


def in_range(r, c):
    global n
    return 0 <= r < n and 0 <= c < n


"""
# 직관적으로 diagonal 하게 움직이는 경우
# 0 0 0 0 0                         0 0 0 0 0
# 0 0 0 0 *                         0 0 0 0 0
# 0 0 0 0 0     ↗ 방향, 7움직인다면     0 0 0 * 0
# 0 0 0 0 0                         0 0 0 0 0
# 0 0 0 0 0                         0 0 0 0 0

def move_nutrients(direction, steps):
    global n, nutrients_loc, move_rules_dirs

    # 이동 방향의 경우 0번부터 7번까지 → ↗ ↑ ↖ ← ↙ ↓ ↘
    dr, dc = move_rules_dirs[direction]

    DEBUG_move_nutrients = False
    if DEBUG:
        print(f"Move_nutrients", "*"*10)
        print(f"direction: {dr, dc}/ steps: {steps}")

    for idx, (r, c) in enumerate(nutrients_loc):
        # 격자의 모든 행,열은 각각 끝과 끝이 연결
        # 격자 바깥으로 나가면 마치 지구가 둥근것처럼 반대편으로 돌아옵
        # 가로, 세로로 움직이는 경우
        if direction in [0, 2, 4, 6]:
            nr, nc = r + (dr * steps), c + (dc * steps)
            nr %= n
            nc %= n
        # 대각선으로 움직이는 경우
        else:
            # ↗, ↙
            # r + c is the same if in the same diagonal line
            if direction in [1, 5]:
                available_steps = n - (abs((n - 1) - (r + c)))
                steps %= available_steps
                if DEBUG & DEBUG_move_nutrients:
                    print(f"available steps: {available_steps}/ steps: {steps}", "*"*5)

                nr, nc = r + (dr * steps), c + (dc * steps)
                if DEBUG & DEBUG_move_nutrients:
                    if in_range(nr, nc):
                        print(f"moved: {nr, nc}")

                if not in_range(nr, nc):
                    if DEBUG & DEBUG_move_nutrients:
                        print("out of range", "*" * 5)
                    # Set max range of r, c
                    # ↗
                    if direction == 1:
                        range_r = r + available_steps
                        range_c = c - available_steps
                    # ↙
                    if direction == 5:
                        range_r = r - available_steps
                        range_c = c + available_steps
                    # Find difference of r, c
                    diff_r = nr - r
                    diff_c = nc - c
                    # Move into right position
                    nr, nc = range_r + diff_r, range_c + diff_c
                    if DEBUG & DEBUG_move_nutrients:
                        print(f"range: {range_r, range_c}")
                        print(f"diff: {diff_r, diff_c}")
            # ↖, ↘
            # r - c is the same if in the same diagonal line
            if direction in [3, 7]:
                available_steps = n - abs(r - c)
                steps %= available_steps
                if DEBUG & DEBUG_move_nutrients:
                    print(f"available steps: {available_steps}/ steps: {steps}", "*"*5)

                nr, nc = r + (dr * steps), c + (dc * steps)
                if DEBUG & DEBUG_move_nutrients:
                    if in_range(nr, nc):
                        print(f"moved: {nr, nc}")

                if not in_range(nr, nc):
                    if DEBUG & DEBUG_move_nutrients:
                        print("out of range", "*"*5)
                    # Set max range of r, c
                    # ↖
                    if direction == 3:
                        range_r = r + available_steps
                        range_c = c + available_steps
                    # ↘
                    if direction == 7:
                        range_r = r - available_steps
                        range_c = c - available_steps
                    # Find difference of r, c
                    diff_r = nr - r
                    diff_c = nc - c
                    # Move into right position
                    nr, nc = range_r + diff_r, range_c + diff_c
                    if DEBUG & DEBUG_move_nutrients:
                        print(f"range: {range_r, range_c}")
                        print(f"diff: {diff_r, diff_c}")
        # Save moved position
        nutrients_loc[idx] = (nr, nc)
        if DEBUG:
            print(f"r, c: {r, c} -> nr, nc: {nr, nc}")

    if DEBUG:
        print("moved nutrients location:", "*"*5)
        print(nutrients_loc)
"""

def move_nutrients(direction, steps):
    global n, nutrients_loc, move_rules_dirs

    # 이동 방향의 경우 0번부터 7번까지 → ↗ ↑ ↖ ← ↙ ↓ ↘
    dr, dc = move_rules_dirs[direction]

    DEBUG_move_nutrients = False
    if DEBUG:
        print(f"Move_nutrients", "*"*10)
        print(f"direction: {dr, dc}/ steps: {steps}")

    for idx, (r, c) in enumerate(nutrients_loc):
        # 격자의 모든 행,열은 각각 끝과 끝이 연결
        # 격자 바깥으로 나가면 마치 지구가 둥근것처럼 반대편으로 돌아옵
        nr = (r + (dr * steps)) % n
        nc = (c + (dc * steps)) % n
        # Save moved position
        nutrients_loc[idx] = (nr, nc)
        if DEBUG:
            print(f"r, c: {r, c} -> nr, nc: {nr, nc}")

    if DEBUG:
        print("moved nutrients location:", "*"*5)
        print(nutrients_loc)



def give_nutrients(r, c, grow_length):
    global land
    land[r][c] += grow_length

def count_diagonal(r, c):
    global land, diagonal_dirs
    count = 0

    for dr, dc in diagonal_dirs:
        nr, nc = r + dr, c + dc
        # '!대각선으로 인접한 방향이 격자를 벗어나는 경우에는 세지 않습니다.'
        if not in_range(nr, nc): continue

        # 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 '높이 1 이상의 리브로수'의 개수 만큼 높이가 증가
        if 1 <= land[nr][nc]:
            count += 1
    return count


def buy_nutrients():
    global n, land, nutrients_loc
    new_nutrients_loc = []

    for r in range(n):
        for c in range(n):
            # 특수 영양제를 투입한 리브로수를 제외
            if (r, c) in nutrients_loc: continue
            # 높이가 2 이상인 리브로수는
            if 2 <= land[r][c]:
                # 높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고,
                land[r][c] -= 2
                # 해당 위치에 특수 영양제를 올려둡
                new_nutrients_loc.append((r, c))
    if DEBUG:
        print(f"Buy_nutrients", "*"*10)
        print_list(land)
        print(new_nutrients_loc)
    # Save new_nutrients_loc
    nutrients_loc = new_nutrients_loc


def count_total_length():
    # m년 이후 남아있는 리브로수의 총 높이의 합을 출력
    global n, land
    total_length = 0

    for r in range(n):
        for c in range(n):
            total_length += land[r][c]
    return total_length



def solution():
    global n, nutrients_loc, move_rules
    if DEBUG:
        global land

    # Initialize nutrients_loc
    # 초기 특수 영양제는 n x n 격자의 좌하단의 4개의 칸에 주어집
    for r in range(n - 1, n - 3, -1):
        for c in range(2):
            nutrients_loc.append((r, c))
    if DEBUG:
        print(f"Initialize nutrients_loc:", "*"*30)
        print(nutrients_loc)

    for d, p in move_rules:
        if DEBUG:
            print(f"Move rules: {d, p}", "="*10)

        # 1)
        # 특수 영양제를 이동 규칙에 따라 이동
        move_nutrients(d, p)

        # 2)
        # 특수 영양제를 이동 시킨 후 해당 땅에 특수 영양제를 투입
        #   1 x 1 땅에 있는 리브로수의 높이를 1 증가
        #   해당 땅에 씨앗만 있는 경우(land가 0인 경우)에는 높이 1의 리브로수를 만들어
        for r, c in nutrients_loc:
            give_nutrients(r, c, 1)
        if DEBUG:
            print(f"Give_nutrients", "*"*10)
            print_list(land)


        # 3)
        # 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 '높이 1 이상의 리브로수'의 개수 만큼 높이가 증가
        for r, c in nutrients_loc:
            count = count_diagonal(r, c)
            give_nutrients(r, c, count)
        if DEBUG:
            print(f"Count_diagonal, Give_nutrients", "*" * 10)
            print_list(land)

        # 4)
        # 특수 영양제를 투입한 리브로수를 제외
        # 높이가 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고,
        # 해당 위치에 특수 영양제를 올려둡
        buy_nutrients()


    # m년 이후 남아있는 리브로수의 총 높이의 합을 출력
    answer = count_total_length()
    return answer

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
# 32
# 65
# 377


# DEBUG = True
DEBUG = False # submission


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    get_input()

    if DEBUG:
        if test_case == 2:
            print(f"test case: {test_case}", "=" * 30)

            print("get input:", "*" * 30)
            print_list(land)
            print("move rules:", move_rules)

            print(solution())
    # ///////////////////////////////////////////////////////////////////////////////////
    if not DEBUG:
        answer = solution()
        print("#%d:" % test_case, answer)