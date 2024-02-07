"""
Problem:
https://www.testdome.com/questions/python/quadratic-equation/94864
"""

# Solution 1:

def find_roots(a, b, c):
  x1 = (b * (-1) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
  x2 = (b * (-1) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
  return (x1, x2)

print(find_roots(2, 10, 8));

"""
# Solution 2:

import numpy as np

def find_roots(a, b, c):
  input = list([a, b, c])
  return tuple(np.roots(input))

print(find_roots(2, 10, 8_DP));
"""