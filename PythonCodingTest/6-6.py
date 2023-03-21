# Counting sort

array = [ 7 , 5 , 9 , 0 , 3 , 1 , 6 , 2 , 9 , 1 , 4 , 8 , 0 , 5 , 2 ]

# Initialize list from min to max
count = [0] * (max(array) + 1)

for i in range(len(array)):
	count[array[i]] += 1

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end=' ')
