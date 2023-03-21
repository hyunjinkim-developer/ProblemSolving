n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_biggest = data[n - 1]
second_biggest = data[n - 2]

# Add first biggest number count times
count = int(m / (k + 1)) * k 
count += m % (k + 1)

result = 0
result += (count) * first_biggest 
result += (m - count) * second_biggest

print(result)
