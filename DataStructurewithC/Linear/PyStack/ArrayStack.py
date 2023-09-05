class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass

class ArrayStack:
	"""LIFO Stack implementation using a Python list as underlying storage."""

	def __init__(self):
		"""Create an empty stack."""
		self._data = []

	def __len__(self):
		"""Return the number of elements in the stack."""
		return len(self._data) 

	def is_empty(self):
		"""Return True if the stack is empty."""
		return len(self._data) == 0
	
	def push(self, e):
		"""Add element e to the top of the stack."""
		self._data.append(e)

	def top(self):
		"""Return (but do not remove) the element at the top of the stack.

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data[-1]

	def pop(self):
		"""Remove and return the element from the top of the stack (i.e., LIFO).

		Raise Empty exception if the stack is empty
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data.pop()
		 
S = ArrayStack() 
print(S.len())
T = []
print(len(T))
"""
S.push(5)
S.push(3)
print(len(S))
print(S.is_empty())
print(S.top())
S.pop()
S.pop()
print(len(S))
print(S.is_empty())
"""
"""
S.push(7)
print(len(S))
print(S.top())
print(S.pop())
#print(S.pop())
"""
"""
# Using basic python function 
stack = []
stack.append(5)
stack.append(10)
print(stack.pop())
print(stack[-1])
print(len(stack))
"""

