n = int(input())
plans = input().split()
x, y = 1, 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
move_types = ['L', 'R', 'U', 'D']
move_types_count = len(move_types)

# Check every plan
for plan in plans:
	# Find move type of each plan
	for i in range(move_types_count):
		# Move
		if plan == move_types[i]:
			new_x = x + dx[i]
			new_y = y + dy[i]
		
			# If new position exceeds the map, ignore it
			if new_x < 1 or new_y < 1 or new_x > n or new_y > n:
				continue
		
			x, y = new_x, new_y

print(x, y)
