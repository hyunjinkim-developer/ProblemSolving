"""
Problem: https://www.acmicpc.net/problem/16234
- 1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100
- 0 ≤ A[r][c] ≤ 100
- 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.
"""
from collections import deque
import math

N, L, R = 0, 0, 0
map_matrix = list()
ROW, COL = 0, 0

#debug
DEBUG = False
def print_matrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c], end='\t')
        print()
    print("-"*10)

def get_input():
    global N, L, R, map_matrix
    global ROW, COL

    # Initialization
    N, L, R = 0, 0, 0
    map_matrix = list()

    N, L, R = map(int, input().split())
    for r in range(N):
        map_matrix.append(list(map(int, input().split())))
    ROW, COL = len(map_matrix), len(map_matrix[0])

def BFS(start_r, start_c, visited):
    global L, R
    global map_matrix, ROW, COL

    # From up clockwise
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def in_range(r, c):
        return 0 <= r < ROW and 0 <= c < COL

    union_locations = [(start_r, start_c)]
    union_population = map_matrix[start_r][start_c]
    country_count = 1

    que = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    while que:
        r, c = que.popleft()
        current_population = map_matrix[r][c]

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc] == True: continue

            new_population = map_matrix[nr][nc]
            if L <= abs(current_population - new_population) <= R:
                que.append((nr, nc))
                visited[nr][nc] = True

                union_locations.append((nr, nc))
                union_population += new_population
                country_count += 1

    union_avg_population = math.floor(union_population / country_count)
    return visited, union_locations, union_avg_population

def move_population():
    global L, R
    global map_matrix, ROW, COL

    visited = [[False] * COL for _ in range(ROW)]
    union_count = 0
    unions = list()
    for r in range(ROW):
        for c in range(COL):
            if visited[r][c] == False:
                visited, union_locations, union_avg_population = BFS(r, c, visited)
                union_count += 1
                # Any union moved
                if 1 < len(union_locations):
                    unions.append((union_avg_population, union_locations))

    for union_avg_population, union_locations in unions:
        for r, c in union_locations:
            map_matrix[r][c] = union_avg_population

    if union_count == (ROW * COL):
        return False
    else:
        return True

def main():
    get_input()

    days_opened = 0
    movable = True
    while movable:
        movable = move_population()
        if movable:
            days_opened += 1
    return days_opened

# if __name__ == "__main__":
#     test_case_count = int(input())
#     for test_case in range(1, test_case_count + 1):
#         print(f"test case: {test_case}", "=" * 30)
#         print(main())

# For submission
if __name__ == "__main__":
    print(main())