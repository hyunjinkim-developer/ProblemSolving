# BFS using deque library
from collections import deque

# Input
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input())))

# Up, Down, Right, Left
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

# BFS(Breadth First Search)
def bfs(row, col):
	queue = deque()
	queue.append((row, col))
	while queue: # Repeat until deque is empty
		row, col = queue.popleft()
		# Check up, down, right, left of current position
		for i in range(4):
			n_row = row + d_row[i]
			n_col = col + d_col[i]
			# Going outside of the map
			if n_row < 0 or n_col < 0 or n_row >= n or n_col >= m:
				continue
			# When current position is a wall
			if graph[n_row][n_col] == 0:
				continue
			# Count as shortest distance when first visiting current position
			if graph[n_row][n_col] == 1:
				graph[n_row][n_col] = graph[row][col] + 1
				queue.append((n_row, n_col))
	# return shortest distance
	return graph[n - 1][m - 1]

print(bfs(0, 0))
