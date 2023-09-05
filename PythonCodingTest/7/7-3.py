# Binary search with iteration

def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2

		# Found target
		if array[mid] == target:
			return mid

		# Target is smaller than mid
		elif array[mid] > target:
			end = mid - 1
		# Target is bigger than mid
		else:
			start = mid + 1

	return None # Target does not exist


# Enter n: the number of elements, target: target string
n, target = list(map(int, input().split()))
# Enter all elements
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
	print('The target does not exist.')
else:
	print(result + 1)
