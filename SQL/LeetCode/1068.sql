--  product_name, year, and price for each sale_id in the Sales table.

SELECT product_name, year, price
FROM Sales
LEFT JOIN Product ON Sales.product_id = Product.product_id