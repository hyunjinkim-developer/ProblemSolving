N = 0

def in_range(r, c):
    global N
    return 1 <= r <= N and 1 <= c <= N

def main():
    global N

    N = int(input())

    directions = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
    }

    r, c = 1, 1
    itinerary = list(input().split())
    for next_move in itinerary:
        dr, dc = directions[next_move]
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        r, c = nr, nc
    print(r, c)

if __name__ == "__main__":
    main()