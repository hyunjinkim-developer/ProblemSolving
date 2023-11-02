-- Report for every three line segments whether they can form a triangle.

SELECT *, IF(x < y + z and y < x + z and z < x + y, "Yes", "No") AS triangle
FROM Triangle