# Input
n, m = map(int, input().split())

data = [] # map
temp = [[0] * m for _ in range(n)] # Map after walls installed
for _ in range(n):
    data.append(list(map(int, input().split())))

# 4_Simulation direction
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
# Spread virus using DFS
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # Spread virus in U, D, L, R
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# Count safe zone
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# Using DFS, Count safe zone every installation
def dfs(count):
    global result
    # 3 walls already installed
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # Spread virus
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # Count max of safe zone
        result = max(result, get_score())
        return
    # Install new walls
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                # Set wall
                data[i][j] = 1
                count += 1
                dfs(count)
                # Remove wall
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)