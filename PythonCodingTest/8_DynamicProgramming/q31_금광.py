"""
Problem:
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다.
맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성
"""

"""
# Solution 1:
N, M = 0, 0

def print_matrix(matrix):
    global N, M

    for row in range(N):
        print(matrix[row][0: M])
    print("-"*10)

def get_input():
    global N, M
    N, M = map(int, input().split())
    gold_list = list(map(int, input().split()))
    mine = list()
    for row in range(N):
        start_idx = row * M
        mine.append(gold_list[start_idx: start_idx + M])
    return mine

def mine_gold(mine):
    global N, M

    dp_table = [[0] * M for _ in range(N)]
    for row in range(N):
        dp_table[row][0] = mine[row][0]

    dirs = [(-1, 1), (0, 1), (1, 1)]
    def in_range(row, col):
        return 0 <= row < N and 0 <= col < M

    for col in range(M):
        for row in range(N):
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if not in_range(nr, nc): continue
                dp_table[nr][nc] = max(dp_table[nr][nc], dp_table[row][col] + mine[nr][nc])
    # Find biggest gold among the last column
    # # Method 1:
    # max_mined_gold = 0
    # for row in range(N):
    #     max_mined_gold = max(max_gold, dp_table[row][M - 1])
    # Method 2:
    max_mined_gold = max([row[M - 1] for row in dp_table])
    return max_mined_gold

def main():
    global N, M
    mine = get_input()

    answer = mine_gold(mine)
    return answer
"""


# Solution 2: Sample Solution
N, M = 0, 0

def get_input():
    global N, M

    N, M = map(int, input().split())
    mine = list(map(int, input().split()))
    return mine

def mine_gold(mine):
    global N, M

    # Initialization
    dp_table = []
    index = 0
    for i in range(N):
        dp_table.append(mine[index: index + M])
        index += M

    for col in range(1, M):
        for row in range(N):
            # Coming from upper left
            if row == 0:
                upper_left = 0
            else:
                upper_left = dp_table[row - 1][col - 1]
            # Coming from lower left
            if row == N - 1:
                lower_lef = 0
            else:
                lower_left = dp_table[row + 1][col - 1]
            # Coming from left
            left = dp_table[row][col - 1]
            dp_table[row][col] = dp_table[row][col] + max(upper_left, lower_left, left)

    max_mined_gold = 0
    for row in range(N):
        max_mined_gold = max(max_mined_gold, dp_table[row][M - 1])
    return max_mined_gold

def main():
    mine = get_input()

    answer = mine_gold(mine)
    return answer



if __name__ == "__main__":
    T = int(input())
    for test_case_no in range(1, T + 1):
        print(f"test case {test_case_no} ", "-"*30)
        print(f"max gold: {main()}")