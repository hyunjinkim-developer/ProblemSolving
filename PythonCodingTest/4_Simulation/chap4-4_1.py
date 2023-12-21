n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]

y, x, direction = map(int, input().split())
# Current position is already visited
visited[x][y] = 1

_map = []
for i in range(n):
	_map.append(list(map(int, input().split())))

# Set direction
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# Turn left
def turn_left():
	global direction
	direction -= 1
	if direction == -1:
		direction = 3

# Start simulation
count = 1
turn_time = 0
while True:
	turn_left()
	new_x = x + dx[direction]
	new_y = y + dy[direction]
	# Move when new location is not visitied and is not water
	if visited[new_y][new_x] == 0 and _map[new_y][new_x] == 0:
		visited[new_y][new_x] = 1
		y = new_y
		x = new_x
		count += 1
		turn_time = 0
		continue
	
	else:
		turn_time += 1

	# Cannot move in every direction
	if turn_time == 4:
		new_y = y - dy[direction]
		new_x = x - dx[direction]
		# Can move back(b/c it's land) in current direction
		if _map[new_y][new_x] == 0:
			y = new_y
			x = new_x
		# Cannot move back because it is water
		else: 
			break
		turn_time = 0

print(count)
