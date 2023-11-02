-- find the names of all the salespersons
-- who did not have any orders related to the company with the name "RED".

SELECT name
FROM SalesPerson
WHERE name not in (SELECT name
                    FROM SalesPerson
                    WHERE sales_id in (SELECT sales_id
                                        FROM Orders
                                        RIGHT JOIN Company
                                        ON Orders.com_id = Company.com_id
                                        WHERE Company.name = "RED"))
