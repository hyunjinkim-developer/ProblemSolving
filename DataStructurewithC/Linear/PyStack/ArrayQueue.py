class ArrayQueue:
	"""FIFO queue implementation using a Python list as underlying storage."""
	DEFAULT_CAPACITY = 10

	def __init__(self):
		"""Creat an empty queue."""
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY


Q = ArrayQueue()
print(Q._data)
