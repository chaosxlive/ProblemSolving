-- https://leetcode.com/problems/fix-names-in-a-table/
-- Write your MySQL query statement below

-- Create table If Not Exists Users (user_id int, name varchar(40))
-- Truncate table Users
-- insert into Users (user_id, name) values ('1', 'aLice')
-- insert into Users (user_id, name) values ('2', 'bOB')

SELECT
    user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)),
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM
    Users
ORDER BY
    user_id