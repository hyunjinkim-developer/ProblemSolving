"""
Problem:
https://www.testdome.com/questions/python/binary-search-tree/94862
"""

"""
# Solution 1:

import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
  left_node = root.left
  right_node = root.right
  if root.value == value:
      return True
  else:
    if value < root.value:
      if left_node == None: 
        return False
      else: 
        return contains(left_node, value)
    else:
      if right_node == None:
        return False
      else:
        return contains(right_node, value)

        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3_Greedy, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3_Greedy))
"""

"""
# Solution 2:

import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
  left_node = root.left
  right_node = root.right
  if root.value == value:
      return True
  elif value < root.value:
   if left_node == None: 
     return False
   else: 
     return contains(left_node, value)
  else:
   if right_node == None:
     return False
   else:
     return contains(right_node, value)

        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3_Greedy, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3_Greedy))
"""