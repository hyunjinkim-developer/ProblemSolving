n, m = map(int, input().split())
result = 0

for i in range(n):
	data = list(map(int, input().split()))

	# Find the smallest number among the same row
	min_value = 10001
	for number in data:
		min_value = min(min_value, number)

	# Find the biggest number among the smallest numbers above
	result = max(result, min_value)

print(result)	
