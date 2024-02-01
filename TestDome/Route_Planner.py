"""
Problem: https://www.testdome.com/questions/python/route-planner/94861
"""

from collections import deque
from copy import deepcopy


def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    # from up in clockwise
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def in_range(r, c):
        return 0 <= r < len(map_matrix) and 0 <= c < len(map_matrix[0])

    # Handling exceptions of various starts, and destinations
    if map_matrix[from_row][from_column] == False or map_matrix[to_row][to_column] == False:
        return False

    # Initiate starting location
    que = deque([(from_row, from_column)])
    visited = deepcopy(map_matrix)
    visited[from_row][from_column] = False

    while que:
        r, c = que.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc): continue
            if visited[nr][nc] == False: continue

            print(nr, nc)
            if nr == to_row and nc == to_column:
                return True
            else:
                que.append((nr, nc))
                visited[nr][nc] = False
    return False


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))
    print(route_exists(0, 0, 1, 1, map_matrix))