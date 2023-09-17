# Linked list with 3-rows 2 dimensional array
graph = [[] for _ in range(3)]

# Save nodes
# Node 46_permutations
graph[0].append((1, 7))
graph[0].append((2, 5))

# Node 1
graph[1].append((0, 7))

# Node 2
graph[2].append((0, 5))

print(graph)
