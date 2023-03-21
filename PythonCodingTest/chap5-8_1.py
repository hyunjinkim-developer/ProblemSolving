# Define DFS(Depth Fist Search) method
def dfs(graph, v, visited):
	# Set current node as visited
	visited[v] = True
	print(v,end=' ')

	# Visit adjacent nodes recursively
	for i in graph[v]:
			if not visited[i]:
				dfs(graph, i, visited)

# Save adjacent nodes in 2 dimensional list
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 8],
	[1, 7],
]

# Set list for visited edges
visited = [False] * 9

# Call BFS method
dfs(graph, 1, visited)
