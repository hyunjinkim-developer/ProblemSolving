

def main():
    N, M = map(int, input().split())

    visited = [[0] * M for _ in range(N)]
    r, c, direction = map(int, input().split())
    # Current position is already visited
    visited[r][c] = 1

    map_ = []
    for i in range(N):
        map_.append(list(map(int, input().split())))

    # Set direction
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # Turn left
    def turn_left():
        nonlocal direction #
        direction -= 1
        if direction == -1:
            direction = 3


    count = 1
    turn_time = 0
    while True:
        turn_left()
        nr = r + dr[direction]
        nc = c + dc[direction]

        # Move when new location is not visited and is not water
        if visited[nr][nc] == 0 and map_[nr][nc] == 0:
            visited[nr][nc] = 1
            r, c = nr, nc
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1

        # Cannot move in every direction
        if turn_time == 4:
            nr = r - dr[direction]
            nc = c - dc[direction]
            # Can move back(b/c it's land) in current direction
            if map_[nr][nc] == 0:
                r, c = nr, nc
            # Cannot move back because it is water
            else:
                break
            turn_time = 0

    print(count)


if __name__ == "__main__":
    main()