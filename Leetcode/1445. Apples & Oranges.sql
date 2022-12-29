-- https://leetcode.com/problems/apples-oranges/

-- Create table If Not Exists Sales (sale_date date, fruit ENUM('apples', 'oranges'), sold_num int)
-- Truncate table Sales
-- insert into Sales (sale_date, fruit, sold_num) values ('2020-05-01', 'apples', '10')
-- insert into Sales (sale_date, fruit, sold_num) values ('2020-05-01', 'oranges', '8')
-- insert into Sales (sale_date, fruit, sold_num) values ('2020-05-02', 'apples', '15')
-- insert into Sales (sale_date, fruit, sold_num) values ('2020-05-02', 'oranges', '15')
-- insert into Sales (sale_date, fruit, sold_num) values ('2020-05-03', 'apples', '20')
-- insert into Sales (sale_date, fruit, sold_num) values ('2020-05-03', 'oranges', '0')
-- insert into Sales (sale_date, fruit, sold_num) values ('2020-05-04', 'apples', '15')
-- insert into Sales (sale_date, fruit, sold_num) values ('2020-05-04', 'oranges', '16')

SELECT
    AppleSales.sale_date,
    AppleSales.sold_num - OrangeSales.sold_num AS diff
FROM
    (
        SELECT
            *
        FROM
            Sales
        WHERE
            fruit = 'apples'
    ) AS AppleSales
LEFT JOIN
    (
        SELECT
            *
        FROM
            Sales
        WHERE
            fruit = 'oranges'
    ) AS OrangeSales
ON
    AppleSales.sale_date = OrangeSales.sale_date
ORDER BY
    AppleSales.sale_date