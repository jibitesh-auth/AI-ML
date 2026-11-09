USE prime;

SELECT * FROM customers;
SELECT * FROM orders;

CREATE VIEW view1 AS
SELECT customer_id, name FROM customers;

SELECT * FROM view1
WHERE name = 'Alice';

/*
CREATE VIEW view2 AS
SELECT *
FROM customers c
INNER JOIN orders o
ON c.cutomer_id = o.customer_id;
*/ 
-- Error: We can't print columns with same name in View

CREATE VIEW view2 AS
SELECT c.customer_id, c.name, o.order_id, o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

SELECT * FROM view2;

DROP VIEW view1;
