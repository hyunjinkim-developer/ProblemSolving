input_data = input()
result = 0

row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1 # column starts from 1

# Directions knight can move
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

for step in steps:
	next_row = row + step[0]
	next_col = col + step[1]

	# Count only when next move is within board
	if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
		result += 1

print(result)
