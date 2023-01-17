n, k = map(int, input().split())
result = 0

while n >= k: 	
	# n is bigger than k and not a common multiple of k, repeat subtracting one to turn n into common multiple of k
	while n % k != 0: 
		n -= 1
		result += 1

	# if n is bigger than k, keep dividing
	n //= k 
	result += 1

# if n is no bigger than k, keep subtract one until only 1 left
while n > 1:
	n -= 1
	result += 1

print(result)

