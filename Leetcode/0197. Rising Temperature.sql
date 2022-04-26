-- https://leetcode.com/problems/rising-temperature/
-- Write your MySQL query statement below

-- Create table If Not Exists Weather (id int, recordDate date, temperature int)
-- Truncate table Weather
-- insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')
-- insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')
-- insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')
-- insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')

SELECT
    Weather.id
FROM
    Weather, Weather as Weather2
WHERE
    DATEDIFF(Weather.recordDate, Weather2.recordDate) = 1
    AND
    Weather.temperature > Weather2.temperature