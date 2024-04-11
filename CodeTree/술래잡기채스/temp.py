TAGGER = (-2, -2)
BLANK = (-1, -1)

# 변수 선언 및 입력:

n = 4

board = [
    [(0, 0) for _ in range(n)]
    for _ in range(n)
]

# 문제에서 주어진 순서대로
# 방향을 정의합니다.
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

max_score = 0



# 방향 d는 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
d_to_direction = {0: (-1, 0),
                 1: (-1, -1),
                 2: (0, -1),
                 3: (1, -1),
                 4: (1, 0),
                 5: (1, 1),
                 6: (0, 1),
                 7: (-1, 1)}
def print_matrix(matrix):
    global BLANK, TAGGER
    for x in range(4):
        for y in range(4):
            if (matrix[x][y] == BLANK) or (matrix[x][y] == TAGGER):
                print(matrix[x][y], end='\t')
            else:
                idx, d = matrix[x][y]
                dir = d_to_direction[d]
                print(idx, dir, end='\t')
        print()

def print_dict(dictionary):
    global N
    for i in range(1, len(dictionary) + 1):
        print(i, dictionary[i])



def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 도둑말이 이동할 수 있는 곳인지를 판단합니다.
# 격자 안이면서, 술래가 없어야 합니다.
def thief_can_go(x, y):
    return in_range(x, y) and board[x][y] != TAGGER


def get_next(x, y, move_dir):
    # 45'씩 8번 회전해보면서 최초로 이동 가능한 곳으로 움직입니다.
    for rotate_num in range(8):
        adjusted_dir = (move_dir + rotate_num) % 8
        next_x, next_y = x + dxs[adjusted_dir], y + dys[adjusted_dir]
        if thief_can_go(next_x, next_y):
            return (next_x, next_y, adjusted_dir)


def move(target_num):
    def swap(x, y, nx, ny):
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

    for x in range(n):
        for y in range(n):
            piece_num, move_dir = board[x][y];
            if piece_num == target_num:
                # 이동해야할 위치와 바라보게 될 방향을 구합니다.
                next_x, next_y, next_dir = get_next(x, y, move_dir)
                # 현재 말의 방향을 바꿔준 뒤, 두 말의 위치를 교환합니다.
                board[x][y] = (piece_num, next_dir)
                swap(x, y, next_x, next_y)

                # d
                print(f"runner idx: {target_num}", "-" * 20)
                print_matrix(board)
                return


# 모든 도둑말들을 한번씩 움직입니다.
def move_all():
    for i in range(1, n * n + 1):
        move(i)


# 현재 술래말의 위치가 (x, y),
# 바라보고 있는 방향이 d이고
# 지금까지 얻은 점수가 score일때
# 탐색을 계속 진행하는 함수입니다.
def search_max_score(x, y, d, score):
    global max_score

    # 술래가 이동할 수 있는 곳인지를 판단합니다.
    # 격자 안이면서, 도둑말이 있어야만 합니다.
    def tagger_can_go(x, y):
        return in_range(x, y) and board[x][y] != BLANK

    def done(x, y, d):
        # 현재 위치에도 한 곳이라도 갈 수 있는지 확인합니다.
        # 존재한다면, 아직 게임은 끝나지 않았습니다.
        for dist in range(1, n + 1):
            nx, ny = x + dxs[d] * dist, y + dys[d] * dist
            if tagger_can_go(nx, ny):
                return False
        return True

    # 더 이상 움직일 곳이 없다면
    # 답을 갱신하고 퇴각합니다.
    if done(x, y, d):
        max_score = max(max_score, score)
        return

    # 현재 턴에 움직일 수 있는 곳을 전부 탐색합니다.
    for dist in range(1, n + 1):
        nx, ny = x + dxs[d] * dist, y + dys[d] * dist
        # 술래가 이동 할 수 없는 위치라면, 패스합니다.
        if not tagger_can_go(nx, ny):
            continue

        # 더 탐색을 진행한 이후, 초기 상태로 다시 만들기 위해
        # temp 배열에 현재 board 상태를 저장해놓습니다.
        temp = [
            [board[i][j] for j in range(n)]
            for i in range(n)
        ]

        # 해당 위치의 도둑말을 잡고
        extra_score, next_dir = board[nx][ny];
        board[nx][ny], board[x][y] = TAGGER, BLANK

        print(f"target {extra_score}/ total: {score + extra_score}", "*" * 50)  #d

        # 모든 도둑말을 움직입니다.
        move_all()
        # 그 다음 탐색을 진행합니다.
        search_max_score(nx, ny, next_dir, score + extra_score)

        # 퇴각시 다시 이전 board의 값을 넣어줍니다.
        for i in range(n):
            for j in range(n):
                board[i][j] = temp[i][j]


        # d
        print("=" * 20)
        print(f"score: {score}")
        print_matrix(board)
        print("\n\n")

# Comment below before submission
import sys
sys.stdin = open("input.txt", "r")

# test case answer
# 21
# 1
# 45

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    board = [
        [(0, 0) for _ in range(n)]
        for _ in range(n)
    ]
    max_score = 0

    for i in range(n):
        given_row = list(map(int, input().split()))
        for j in range(n):
            p, d = given_row[j * 2], given_row[j * 2 + 1]
            board[i][j] = (p, d - 1)

    if test_case == 3:
        # 처음 (0, 0) 도둑말을 잡고, 모든 도둑말이 이동한 다음에 시작합니다.
        init_score, init_dir = board[0][0]
        board[0][0] = TAGGER

        move_all()

        search_max_score(0, 0, init_dir, init_score)

        print(max_score)
    # ///////////////////////////////////////////////////////////////////////////////////


