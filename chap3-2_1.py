n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_biggest = data[n - 1]
second_biggest = data[n - 2]

result = 0
while True:
	# Add biggest numbers k times
	for i in range(k):
		if m == 0: # if m is 0, stop adding
			break
		result += first_biggest 
		m -= 1
	
	# if m is 0
	if m == 0:
		break
	
	# Add second biggest number 
	result += second_biggest 
	m -= 1

print(result)

