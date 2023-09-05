count = 0
def recursive_function():
	global count
	count += 1
	print("Call recursive function: {}".format(count))

	recursive_function()

recursive_function()
