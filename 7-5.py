# Binary search with Iteration

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # Found
        if array[mid] == target:
            return mid
        # Target is bigger than mid
        elif array[mid] > target:
            end = mid - 1
        # Target is smaller than mid
        elif array[mid] < target:
            start = mid + 1
    return None

# Enter N: what is in the house
n = int(input())
array = list(map(int, input().split()))
array.sort()

# Enter M: what customer wants
m = int(input())
x = list(map(int, input().split()))

# Check every element exists
for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')