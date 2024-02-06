n, k = map(int, input().split())
result = 0

# if n >= k,
while True:
	# Subtract 1, until n turn into common multiple of k
	target = n // k * k
	result += (n - target)
	n = target

	if n < k:
		break
	
	# Divide n with k 
	result += 1
	n = int(n / k)

result += (n - 1)
print(result)
