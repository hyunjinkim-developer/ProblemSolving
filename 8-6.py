# Enter the number of food storage and food in each storage
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100
# Bottom up dynamic Programming
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])