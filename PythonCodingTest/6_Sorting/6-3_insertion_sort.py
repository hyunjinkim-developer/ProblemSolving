# Insertion sort
# Time complexity:
# 	O(N ** 2)
#	Ω(N) (Time complexity at best, when most elements are already sorted)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	# Moving left
	for j in range(i, 0, -1):
		# Skip if a number on the left is bigger than the current number
		if array[j - 1] > array[j]:
			array[j], array[j - 1] = array[j - 1], array[j]
		# If a number on the left is smaller than current number
		else:
			break 
	
print(array)
