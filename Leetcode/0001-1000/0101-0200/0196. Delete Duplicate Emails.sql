-- https://leetcode.com/problems/delete-duplicate-emails/
-- Write your MySQL query statement below

-- Create table If Not Exists Person (Id int, Email varchar(255))
-- Truncate table Person
-- insert into Person (id, email) values ('1', 'john@example.com')
-- insert into Person (id, email) values ('2', 'bob@example.com')
-- insert into Person (id, email) values ('3', 'john@example.com')

DELETE 
    p1 
FROM 
    Person as p1, Person as p2
WHERE
    p1.id > p2.id AND p1.email = p2.email