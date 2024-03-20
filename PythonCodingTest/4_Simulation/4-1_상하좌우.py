# Solution 1:
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


"""
# Solution 2: Sample solution
def main():
    N = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > N or ny > N: continue

        x, y = nx, ny

    print(x, y)
"""

if __name__ == "__main__":
    main()