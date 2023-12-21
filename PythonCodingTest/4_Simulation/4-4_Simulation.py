N, M = 0, 0

def in_range(r, c):
    global N, M
    return 0 <= r < N and 0 <= c < M

def main():
    answer = 0
    global N, M

    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    current_direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    d_r, d_c = current_direction[d]
    map_ = list()
    for r in range(N):
        map_.append(list(map(int, input().split())))

    # Set visited as value of 2
    map_[r][c] = 2

    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    count = 0
    while True:
        # Turn left
        for idx, dir in enumerate(dirs):
            dir_r, dir_c = dir
            if d_r == dir_r and d_c == dir_c:
                d_r, d_c = dirs[(idx + 1) % 4]
                break

        nr, nc = r + d_r, c + d_c
        print(nr, nc)
        if not in_range(nr, nc): continue

        if map_[nr][nc] == 0:
            r, c = nr, nc
            map_[nr][nc] = 2
            answer += 1
            count = 0
            continue
        if map_[nr][nc] == 2 or map_[nr][nc] == 1:
            count += 1

        if count == 4:
            r, c = r + (nr * -1), c + (nc * -1)
            if map_[r][c] == 1:
                break
            answer += 1

    print(answer)

if __name__ == "__main__":
    main()