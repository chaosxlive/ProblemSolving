-- https://leetcode.com/problems/duplicate-emails/
-- Write your MySQL query statement below

-- Create table If Not Exists Person (Id int, Email varchar(255))
-- Truncate table Person
-- insert into Person (Id, Email) values ('1', 'a@b.com')
-- insert into Person (Id, Email) values ('2', 'c@d.com')
-- insert into Person (Id, Email) values ('3', 'a@b.com')

SELECT
    `Email`
FROM
    (
        SELECT 
            `Email`, COUNT(`Email`) AS countEmail
        FROM
            Person
        GROUP BY
            `Email`
    ) AS EmailCounter
WHERE countEmail > 1