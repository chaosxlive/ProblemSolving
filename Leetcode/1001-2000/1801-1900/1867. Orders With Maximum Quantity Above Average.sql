-- https://leetcode.com/problems/orders-with-maximum-quantity-above-average/

-- Create table If Not Exists OrdersDetails (order_id int, product_id int, quantity int)
-- Truncate table OrdersDetails
-- insert into OrdersDetails (order_id, product_id, quantity) values ('1', '1', '12')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('1', '2', '10')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('1', '3', '15')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('2', '1', '8')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('2', '4', '4')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('2', '5', '6')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('3', '3', '5')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('3', '4', '18')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('4', '5', '2')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('4', '6', '8')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('5', '7', '9')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('5', '8', '9')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('3', '9', '20')
-- insert into OrdersDetails (order_id, product_id, quantity) values ('2', '9', '4')

SELECT
    order_id
FROM
    (
        SELECT
            order_id,
            MAX(quantity) AS max_quantity
        FROM
            OrdersDetails
        GROUP BY
            order_id
    ) AS M,
    (
        SELECT
            MAX(avg_quantity) AS max_quantity
        FROM
            (
                SELECT
                    AVG(quantity) AS avg_quantity
                FROM
                    OrdersDetails
                GROUP BY
                    order_id
            ) AS Q
    ) AS MQ
WHERE
    M.max_quantity > MQ.max_quantity
