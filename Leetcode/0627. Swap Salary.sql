-- https://leetcode.com/problems/swap-salary/
-- Write your MySQL query statement below

-- create table if not exists salary(id int, name varchar(100), sex char(1), salary int)
-- Truncate table salary
-- insert into salary (id, name, sex, salary) values ('1', 'A', 'm', '2500')
-- insert into salary (id, name, sex, salary) values ('2', 'B', 'f', '1500')
-- insert into salary (id, name, sex, salary) values ('3', 'C', 'm', '5500')
-- insert into salary (id, name, sex, salary) values ('4', 'D', 'f', '500')

UPDATE
    salary
SET
    sex = CASE WHEN sex='m' THEN 'f' ELSE 'm' END