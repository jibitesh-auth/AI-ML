USE prime;

SELECT * FROM customers;
SELECT * FROM orders;

-- With WHERE --
SELECT *
FROM orders
WHERE amount > (
	SELECT AVG(amount)
    FROM orders
);

-- With SELECT --
SELECT name,
	(	SELECT COUNT(*)
		FROM orders o
        WHERE o.customer_id = c.customer_id
	) AS order_count
FROM customers c;

-- With From --
SELECT
	summary.customer_id,
    summary.avg_amount
FROM
	(	SELECT 
			customer_id,
			AVG(amount) AS avg_amount
		FROM orders
        GROUP BY customer_id
	) AS summary;
	
