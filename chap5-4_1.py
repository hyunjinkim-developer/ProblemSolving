def recursive_function(i):
	# Stopping condition: Quit after 100 times
	if i == 100:
		return
	
	print("From {}th recursive function, call {}th recursive function".format(i, i+1))
	recursive_function(i + 1)

	print("Terminate {}th function".format(i))

recursive_function(1)
