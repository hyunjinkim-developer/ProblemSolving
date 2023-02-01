# Input
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input())))

# DFS
# Travel a certain node and all adjacent nodes 
def dfs(row, col):
	# If current position is the outside of the map, terminal condition for recursive function
	if row <= -1 or row >= n or col <= -1 or col >= m:
		return False
	# Current node not visited
	if graph[row][col] == 0:
		graph[row][col] = 1 # visit current node
		# Visit available adjcent nodes
		dfs(row - 1, col) # Up
		dfs(row + 1, col) # Down
		dfs(row, col - 1) # Left
		dfs(row, col + 1) # Right
		return True
	return False

# Travel evercol node 
result = 0
for i in range(n):
	for j in range(m):
		# Start DFS from current position
		if dfs(i, j) == True:
			result += 1

print(result)
	
