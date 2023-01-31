# Use deque for BFS(Breath First Search)
from collections import deque

# Define BFS method
def bfs(graph, start, visited):
	queue = deque([start])
	# Set current node as visited
	visited[start] = True
	
	while queue: # Repeat until queue is empty
		# Pop one node from deque
		v = queue.popleft()
		print(v, end=' ')
		# Insert adjacent nodes of current node
		for i in graph[v]:
			if not visited[i]: # if the node is not visited yet
				queue.append(i)
				visited[i] = True


# Save connection of nodes into 2 dimensional list
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# Check visited nodes
visited = [False] * 9

bfs(graph, 1, visited)
