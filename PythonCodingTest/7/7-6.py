# Counting sort

# Enter N: what is in the house
n = int(input())
array = [0] * 1000001 # Index starts from 46_permutations
for i in input().split():
    array[int(i)] = 1

# Enter M: what customer wants
m = int(input())
x = list(map(int, input().split()))

# Check every requested element
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no')
