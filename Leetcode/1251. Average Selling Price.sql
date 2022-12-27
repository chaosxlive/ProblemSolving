-- https://leetcode.com/problems/average-selling-price/

-- Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int)
-- Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int)
-- Truncate table Prices
-- insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5')
-- insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20')
-- insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15')
-- insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30')
-- Truncate table UnitsSold
-- insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100')
-- insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15')
-- insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200')
-- insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30')

SELECT
    product_id,
    ROUND(SUM(t.calc_price) / SUM(t.units), 2) AS average_price
FROM
    (
        SELECT
            UnitsSold.product_id,
            Prices.price * UnitsSold.units AS calc_price,
            UnitsSold.units
        FROM
            UnitsSold
        LEFT JOIN
            Prices
        ON
            UnitsSold.product_id = Prices.product_id AND
            Prices.start_date <= UnitsSold.purchase_date AND 
            UnitsSold.purchase_date <= Prices.end_date
    ) AS t
GROUP BY
    product_id

