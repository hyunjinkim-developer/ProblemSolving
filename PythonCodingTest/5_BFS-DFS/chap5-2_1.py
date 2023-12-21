""" 
Queue in Python
Use deque in collections library
Pros: 
- Much faster input, output than list 
- Much simpler than queue library
- list(deque) to turn deque into list
"""
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# Print in input order
print(queue)

# Reverse order of elements
queue.reverse() 
print(queue)
