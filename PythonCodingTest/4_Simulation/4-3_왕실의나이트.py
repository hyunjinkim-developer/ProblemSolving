# Solution 1:
def in_range(r, c):
    return 1 <= r <= 8 and 1 <= c <= 8

def main():
    answer = 0

    convert_columns = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    # from upper left in clockwise
    directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

    pos = input()
    c, r = convert_columns[pos[0]], int(pos[1])
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        answer += 1

    print(answer)


"""
# Solution 2: Sample solution
def main():
    input_data = input()
    row = int(input_data[1])
    # Convert column name from alphabet to number using ord()
    # ord() : returns the number representing the unicode code of a specified character
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if 1 <= next_row and next_row <= 8 and 1 <= next_column and next_column <= 8:
            result += 1

    print(result)
"""


if __name__ == "__main__":
    main()