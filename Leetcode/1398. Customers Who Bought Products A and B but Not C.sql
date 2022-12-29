-- https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/

-- Create table If Not Exists Customers (customer_id int, customer_name varchar(30))
-- Create table If Not Exists Orders (order_id int, customer_id int, product_name varchar(30))
-- Truncate table Customers
-- insert into Customers (customer_id, customer_name) values ('1', 'Daniel')
-- insert into Customers (customer_id, customer_name) values ('2', 'Diana')
-- insert into Customers (customer_id, customer_name) values ('3', 'Elizabeth')
-- insert into Customers (customer_id, customer_name) values ('4', 'Jhon')
-- Truncate table Orders
-- insert into Orders (order_id, customer_id, product_name) values ('10', '1', 'A')
-- insert into Orders (order_id, customer_id, product_name) values ('20', '1', 'B')
-- insert into Orders (order_id, customer_id, product_name) values ('30', '1', 'D')
-- insert into Orders (order_id, customer_id, product_name) values ('40', '1', 'C')
-- insert into Orders (order_id, customer_id, product_name) values ('50', '2', 'A')
-- insert into Orders (order_id, customer_id, product_name) values ('60', '3', 'A')
-- insert into Orders (order_id, customer_id, product_name) values ('70', '3', 'B')
-- insert into Orders (order_id, customer_id, product_name) values ('80', '3', 'D')
-- insert into Orders (order_id, customer_id, product_name) values ('90', '4', 'C')
-- https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/

-- Create table If Not Exists Customers (customer_id int, customer_name varchar(30))
-- Create table If Not Exists Orders (order_id int, customer_id int, product_name varchar(30))
-- Truncate table Customers
-- insert into Customers (customer_id, customer_name) values ('1', 'Daniel')
-- insert into Customers (customer_id, customer_name) values ('2', 'Diana')
-- insert into Customers (customer_id, customer_name) values ('3', 'Elizabeth')
-- insert into Customers (customer_id, customer_name) values ('4', 'Jhon')
-- Truncate table Orders
-- insert into Orders (order_id, customer_id, product_name) values ('10', '1', 'A')
-- insert into Orders (order_id, customer_id, product_name) values ('20', '1', 'B')
-- insert into Orders (order_id, customer_id, product_name) values ('30', '1', 'D')
-- insert into Orders (order_id, customer_id, product_name) values ('40', '1', 'C')
-- insert into Orders (order_id, customer_id, product_name) values ('50', '2', 'A')
-- insert into Orders (order_id, customer_id, product_name) values ('60', '3', 'A')
-- insert into Orders (order_id, customer_id, product_name) values ('70', '3', 'B')
-- insert into Orders (order_id, customer_id, product_name) values ('80', '3', 'D')
-- insert into Orders (order_id, customer_id, product_name) values ('90', '4', 'C')

SELECT
    Customers.customer_id AS customer_id,
    Customers.customer_name AS customer_name
FROM
    (
        SELECT
            *
        FROM
            Orders
        WHERE
            (customer_id, 'A') IN (
                SELECT
                    customer_id,
                    product_name
                FROM
                    Orders
            )

            AND

            (customer_id, 'B') IN (
                SELECT
                    customer_id,
                    product_name
                FROM
                    Orders
            )
            
            AND

            (customer_id, 'C') NOT IN (
                SELECT
                    customer_id,
                    product_name
                FROM
                    Orders
            )
        GROUP BY
            customer_id
    ) AS t1
LEFT JOIN
    Customers
ON
    Customers.customer_id = t1.customer_id
ORDER BY
    customer_id