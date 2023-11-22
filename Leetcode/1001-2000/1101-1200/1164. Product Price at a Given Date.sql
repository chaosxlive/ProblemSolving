-- https://leetcode.com/problems/product-price-at-a-given-date/

-- Create table If Not Exists Products (product_id int, new_price int, change_date date)
-- Truncate table Products
-- insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14')
-- insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14')
-- insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15')
-- insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16')
-- insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17')
-- insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18')

SELECT DISTINCT
    Products.product_id,
    CASE
        WHEN
            P.value_date IS NULL
        THEN
            10
        ELSE
            Products.new_price
    END AS price
FROM
    Products
LEFT JOIN
    (
        SELECT
            Products.product_id,
            MAX(Products.change_date) AS value_date
        FROM
            Products
        WHERE
            Products.change_date <= '2019-08-16'
        GROUP BY
            Products.product_id
    ) AS P
ON
    Products.product_id = P.product_id
WHERE
    Products.change_date = P.value_date
    OR
    P.value_date IS NULL