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
c, d, e = 1.0, 2.5_BFS-DFS, 3.4_Simulation
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# ! Remove before submission
import sys
sys.stdin = open("input.txt", "r")


import collections
import copy
# global variables
global N, M, K


# User defined functions
# Getting inputs
def get_input():
    N, M, K = map(int, input().split())

    maze = collections.deque()
    for r in range(N):
        maze.append(list(map(int, input().split())))

    players_position = collections.deque()
    for _ in range(M):
        players_position.append(list(map(int, input().split())))

    exit_position = collections.deque(map(int, input().split()))
    return N, M, K, maze, players_position, exit_position


# Find the shortest path
def find_shortest_path(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

# Move every participant to exit direction
def move(maze, player_position, exit_position, moved_distance):
    current_shortest_path = find_shortest_path(exit_position, player_position)

    available_positions = collections.deque()
    movable_direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
    # Find movable positions
    for index, (r_gap, c_gap) in enumerate(movable_direction):
        moved_r_pos = player_position[0] + r_gap
        moved_c_pos = player_position[1] + c_gap
        # Check whether moved position located in maze and
        if 1 <= moved_r_pos <= N and 1 <= moved_c_pos <= N:
            # Blocked by walls
            if maze[moved_r_pos - 1][moved_c_pos - 1] != 0:
                continue
            else: # Not blocked by walls
                moved_shortest_path = find_shortest_path(exit_position, [moved_r_pos, moved_c_pos])
                # Only movable when shortest path get shorter than current position
                if current_shortest_path > moved_shortest_path:
                    available_positions.append(index) # save index of movable direction

    # If there is several movable positions
    if len(available_positions) > 1:
        new_position = [-1, -1]
        # priority: Up/ Down > Left/ Right
        for idx in available_positions:
            if idx == 0 or idx == 1: # Up or Down
               new_position[0] = player_position[0] + movable_direction[idx][0]
               new_position[1] = player_position[1] + movable_direction[idx][1]
        # more than 2 movable positions available with only Left and Right
        if new_position == [-1, -1]:
            idx = available_positions[0]
            new_position[0] = player_position[0] + movable_direction[idx][0]
            new_position[1] = player_position[1] + movable_direction[id][1]
        player_position[0] = new_position[0]
        player_position[1] = new_position[1]
        moved_distance += 1

    elif len(available_positions) == 1:
        idx = available_positions[0]
        player_position[0] = player_position[0] + movable_direction[idx][0]
        player_position[1] = player_position[1] + movable_direction[idx][1]
        moved_distance += 1

    return player_position, moved_distance

# Find the upper_left_corner
def find_upper_left_corner(maze, player, exit_position):
    upper_left_corner = [0, 0]
    square_length = 0

    # player and exit in diagonal position
    if abs(exit_position[0] - player[0]) == abs(exit_position[1] - player[1]):
        square_length = abs(exit_position[0] - player[0])
        upper_left_corner = min(exit_position[0], player[0]), min(exit_position[1], player[1])
    else:
        # Locating player and exit in the same spot is not available,
        # because the player already escaped in the move() state

        # player and exit is in the row
        if exit_position[0] == player[0]:
            square_length = abs(exit_position[1] - player[1])
            new_row = player[0] - square_length
            if new_row < 1:
                new_row = 1
            new_col = min(exit_position[1], player[1])
            upper_left_corner[0], upper_left_corner[1] = new_row, new_col

        # player and exit is in the column
        elif exit_position[1] == player[1]:
            square_length = abs(exit_position[0] - player[0])
            new_row = min(exit_position[0], player[0])
            new_col = player[1] - square_length
            if new_col < 1:
                new_col = 1
            upper_left_corner[0], upper_left_corner[1] = new_row, new_col

        # player and exit are not in the same line
        else:
            square_length = max(abs(exit_position[0] - player[0]), abs(exit_position[1] - player[1]))
            # upper left position
            ul_row = max(exit_position[0], player[0]) - square_length
            ul_col = max(exit_position[1], player[1]) - square_length
            if ul_row < 1:
                ul_row = 1
            if ul_col < 1:
                ul_col = 1
            # lower right position
            lr_row = max(exit_position[0], player[0])
            lr_col = max(exit_position[1], player[1])

            if ul_row + square_length <= N and ul_col + square_length <= N:
                upper_left_corner[0], upper_left_corner[1] = ul_row, ul_col
            elif 1 <= lr_row - square_length and 1 <= lr_col - square_length:
                upper_left_corner[0], upper_left_corner[1] = lr_row - square_length, lr_col- square_length
            # if the samllest square exceeds maze, return upper_left_corner in [-1, -1]
            else:
                upper_left_corner[0], upper_left_corner[1] = -1, -1

    return upper_left_corner, square_length + 1

# Sort with customized function
# sort upper left corner with lower row, then lower column
def sort_upper_left_corner(element):
    return element[0], element[1]

# Find the smallest square
def find_smallest_square(maze, players_position, exit_position):
    # Find the smallest square in each player's location
    smallest_squares = collections.defaultdict(list)
    for player in players_position:
        upper_left_corner, square_length = find_upper_left_corner(maze, player, exit_position)
        # Check whether upper left corner is inside the maze
        if 1 <= upper_left_corner[0] <= N and 1 <= upper_left_corner[1] <= N:
            smallest_squares[square_length].append(upper_left_corner)

    if len(smallest_squares) > 0:
        smallest_square_length = min(smallest_squares.keys())
        # If there are several available squares with the smallest square length
        if len(smallest_squares[smallest_square_length]) >= 2:
            # Find upper left corner with the smallest with the priority of row > column
            smallest_squares[smallest_square_length] = sorted(smallest_squares[smallest_square_length], key=lambda element: sort_upper_left_corner(element))
        return smallest_squares[smallest_square_length][0], smallest_square_length
    else: # the smallest square not found
        return list(), -1
def rotate_90_clockwise(upper_left_corner, square_length, maze, players_position, exit_position):
    square_row, square_col = upper_left_corner[0], upper_left_corner[1]

    # Rotate Maze
    rotated_target_maze = [[0] * square_length for _ in range(square_length)]
    # target_maze = [[0] * square_length] * square_length # shallow copy, not appropriate
    target_maze = list()
    # Get maze of target square
    # Decrease durability of walls
    # rotated_target_maze = list(map(list, zip(*target_maze[::-1])))
    for r in range(square_row - 1, square_row - 1 + square_length):
        new_row = list()
        for c in range(square_col - 1, square_col - 1 + square_length):
            if maze[r][c] != 0:
                maze[r][c] -= 1
            new_row.append(maze[r][c])
        target_maze.append(new_row)
    # Rotate target square 90 degree in clockwise
    for r in range(square_length):
        for c in range(square_length):
            rotated_target_maze[c][square_length - 1 - r] = target_maze[r][c]
    # Convert original maze with rotated target square
    for r in range(square_row - 1, square_row - 1 + square_length):
        maze[r][square_col - 1:square_col - 1 + square_length] = rotated_target_maze[r - (square_row - 1)]

    # Rotate players inside the smallest square
    for player in players_position:
        # the player within the smallest square
        if square_row <= player[0] <= square_row + (square_length - 1) and square_col <= player[1] <= square_col + (square_length - 1):
            new_row = player[1] - square_col + square_row
            new_col = (square_length - 1) - (player[0] - square_row) + square_col
            player[0], player[1] = new_row, new_col

    # Rotate exit position
    if square_row <= exit_position[0] <= square_row + (square_length - 1) and square_col <= exit_position[1] <= square_col + (square_length - 1):
        new_row = exit_position[1] - square_col + square_row
        new_col = (square_length - 1) - (exit_position[0] - square_row) + square_col
        exit_position[0], exit_position[1] = new_row, new_col

    return maze, players_position, exit_position

def rotate(maze, players_position, exit_position):
    # Find the smallest square
    upper_left_corner, square_length = find_smallest_square(maze, players_position, exit_position)

    # Found the smallest square
    if len(upper_left_corner) != 0:
        # Rotate 90 degree in clockwise
        maze, players_position, exit_position = rotate_90_clockwise(upper_left_corner, square_length, maze, players_position, exit_position)

    return maze, players_position, exit_position

def solution(maze, players_position, exit_position):
    # Total moved distances of all players
    moved_distance = 0

    # For each second
    for t in range(1, K + 1):
        # Move
        for idx, current_player_position in enumerate(players_position):
            players_position[idx], moved_distance = move(maze, current_player_position, exit_position, moved_distance)
        # Escaped
        for player in players_position.copy():
            # To compare two mutables, data structure should be the same
            if collections.deque(player) == exit_position:
                players_position.remove(player)
        # Terminate when all players have escaped
        if len(players_position) == 0:
            break

        # Rotate
        maze, players_position, exit_position = rotate(maze, players_position, exit_position)

    return exit_position, moved_distance

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # Get inputs
    N, M, K, maze, players_position, exit_position = get_input()

    # Solution for each test case
    exit_position, moved_distance = solution(maze, players_position, exit_position)

    # Answer
    print(moved_distance)
    print(exit_position[0], exit_position[1])

    # ///////////////////////////////////////////////////////////////////////////////////

