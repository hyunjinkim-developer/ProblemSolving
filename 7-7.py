# Use set data structure

# Enter N: what is in the house
n = int(input())
array = set(map(int, input().split()))

# Enter M: what customer wants
m = int(input())
x = list(map(int, input().split()))

# Check every requested element
for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')