def in_range(r, c):
    return 1 <= r <= 8 and 1 <= c <= 8

def main():
    answer = 0

    convert_columns = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    # from upperleft in clockwise
    directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

    pos = input()
    c, r = convert_columns[pos[0]], int(pos[1])
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        answer += 1

    print(answer)

if __name__ == "__main__":
    main()