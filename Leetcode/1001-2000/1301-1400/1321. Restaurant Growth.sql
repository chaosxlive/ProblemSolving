-- https://leetcode.com/problems/restaurant-growth/

-- Create table If Not Exists Customer (customer_id int, name varchar(20), visited_on date, amount int)
-- Truncate table Customer
-- insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-01', '100')
-- insert into Customer (customer_id, name, visited_on, amount) values ('2', 'Daniel', '2019-01-02', '110')
-- insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-03', '120')
-- insert into Customer (customer_id, name, visited_on, amount) values ('4', 'Khaled', '2019-01-04', '130')
-- insert into Customer (customer_id, name, visited_on, amount) values ('5', 'Winston', '2019-01-05', '110')
-- insert into Customer (customer_id, name, visited_on, amount) values ('6', 'Elvis', '2019-01-06', '140')
-- insert into Customer (customer_id, name, visited_on, amount) values ('7', 'Anna', '2019-01-07', '150')
-- insert into Customer (customer_id, name, visited_on, amount) values ('8', 'Maria', '2019-01-08', '80')
-- insert into Customer (customer_id, name, visited_on, amount) values ('9', 'Jaze', '2019-01-09', '110')
-- insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-10', '130')
-- insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-10', '150')

SELECT
    C2.visited_on,
    SUM(C1.amount) AS amount,
    ROUND(SUM(C1.amount) / 7, 2) AS average_amount
FROM
    Customer AS C1,
    (
        SELECT DISTINCT
            visited_on
        FROM
            Customer
        WHERE
            DATE_ADD(visited_on, INTERVAL -6 DAY) IN (
                SELECT
                    visited_on
                FROM
                    Customer
            )
    ) AS C2
WHERE
    C1.visited_on BETWEEN DATE_ADD(C2.visited_on, INTERVAL -6 DAY) AND C2.visited_on
GROUP BY
    C2.visited_on
ORDER BY
    visited_on ASC