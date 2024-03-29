-- https://leetcode.com/problems/consecutive-numbers/

-- Create table If Not Exists Logs (id int, num int)
-- Truncate table Logs
-- insert into Logs (id, num) values ('1', '1')
-- insert into Logs (id, num) values ('2', '1')
-- insert into Logs (id, num) values ('3', '1')
-- insert into Logs (id, num) values ('4', '2')
-- insert into Logs (id, num) values ('5', '1')
-- insert into Logs (id, num) values ('6', '2')
-- insert into Logs (id, num) values ('7', '2')

SELECT DISTINCT
    num AS ConsecutiveNums
FROM
    Logs
WHERE
    (id - 1, num) IN (
        SELECT
            *
        FROM
            Logs
    )
    AND
    (id + 1, num) IN (
        SELECT
            *
        FROM
            Logs
    )