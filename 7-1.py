# Sequential Search

def sequential_search(n, target, array):
	for i in range(n):
		if array[i] == target:
			return i + 1 # return index(starting from 1) of current element

print("Enter the number of elements and a string to find with space in between." )
input_data = input().split()
n = int(input_data[0]) # # of elements
target = input_data[1] # a string to find

print("Enter strings with space in between.")
array = input().split()

print(sequential_search(n, target, array))
