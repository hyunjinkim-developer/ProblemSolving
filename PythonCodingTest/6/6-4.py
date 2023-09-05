# Quick sort
array = [ 5 , 7 , 9 , 0 , 3 , 1 , 6 , 2 , 4 , 8 ]

def quick_sort(array, start, end):
	if start >= end:
		return

	# Index
	pivot = start
	left = start + 1
	right = end

	while left <= right:
		# Repeat until finding datum bigger than pivot
		while left <= end and array[left] <= array[pivot]:
			left += 1
		# Repeat until finding datum smaller than pivot
		while right > start and array[right] >= array[pivot]:
			right -= 1
		# If left is bigger than right, swap pivot with smaller datum
		if left > right:
			array[right], array[pivot] = array[pivot], array[right]
		else:
			array[left], array[right] = array[right], array[left]
	# Sort each left and right part of pivot
	quick_sort(array, start, right - 1)
	quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
