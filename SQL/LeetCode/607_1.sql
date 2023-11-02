-- find the names of all the salespersons
-- who did not have any orders related to the company with the name "RED".

SELECT s.name
FROM SalesPerson s
WHERE s.name not in
  (SELECT s.name
    FROM SalesPerson s
      LEFT JOIN Orders o on s.sales_id = o.sales_id
      LEFT JOIN Company c on o.com_id = c.com_id
    WHERE c.name = "RED")