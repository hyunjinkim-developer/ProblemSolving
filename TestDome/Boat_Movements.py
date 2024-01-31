"""
Problem: https://www.testdome.com/tests/python-online-test/45
"""

def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    answer = False

    # left, right, up, down
    dirs = [(0, -1), (0, 1), (-2, 0), (2, 0)]

    def in_range(r, c):
        return 0 <= r < len(game_matrix) and 0 <= c < len(game_matrix[0])

    r, c = from_row, from_column
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        if game_matrix[nr][nc] == False: continue
        if dc == 0 and game_matrix[r + (dr // 2)][nc] == False: continue

        if nr == to_row and nc == to_column:
            answer = True
            break
    return answer


if __name__ == "__main__":
    game_matrix = [
        [False, False, True, True, False],
        [False, False, True, False, False],
        [False, False, True, True, False],
        [False, True, False, True, False],
        [False, False, True, False, False]
    ]

    print(can_travel_to(game_matrix, 2, 2, 0, 2))
    print(can_travel_to(game_matrix, 2, 2, 2, 1))
    print(can_travel_to(game_matrix, 2, 2, 2, 3))
    print(can_travel_to(game_matrix, 2, 2, 4, 2))