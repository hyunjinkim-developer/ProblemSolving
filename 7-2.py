# Binary serach implemented in Recursive function

def binary_search (array, target, start, end):
	if start > end:
		return None
	
	mid = (start + end) // 2 # Take the floor, quotient operator

	if array[mid] == target:
		return mid

	# Target is smaller than mid
	elif array[mid] > target:
		return binary_search(array, target, start, mid - 1)
	# Target is bigger than mid
	else:
		return binary_search(array, target, mid + 1, end)


# Enter n (the number of elemnts) and the target string
n, target = list(map(int, input().split()))
# Enter all strings
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
	print("The string does not exist.")
else:
	print(result + 1)
