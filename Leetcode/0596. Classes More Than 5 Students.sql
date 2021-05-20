-- https://leetcode.com/problems/classes-more-than-5-students/
-- Write your MySQL query statement below

-- Create table If Not Exists courses (student varchar(255), class varchar(255))
-- Truncate table courses
-- insert into courses (student, class) values ('A', 'Math')
-- insert into courses (student, class) values ('B', 'English')
-- insert into courses (student, class) values ('C', 'Math')
-- insert into courses (student, class) values ('D', 'Biology')
-- insert into courses (student, class) values ('E', 'Math')
-- insert into courses (student, class) values ('F', 'Computer')
-- insert into courses (student, class) values ('G', 'Math')
-- insert into courses (student, class) values ('H', 'Math')
-- insert into courses (student, class) values ('I', 'Math')

SELECT 
    `class`
FROM
    courses
GROUP BY
    `class`
HAVING
    COUNT(DiSTINCT `student`) >= 5