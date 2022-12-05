-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
-- Write your MySQL query statement below

-- Create table If Not Exists Teacher (teacher_id int, subject_id int, dept_id int)
-- Truncate table Teacher
-- insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '2', '3')
-- insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '2', '4')
-- insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '3', '3')
-- insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '1', '1')
-- insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '2', '1')
-- insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '3', '1')
-- insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '4', '1')

SELECT
    teacher_id, 
    COUNT(DISTINCT subject_id) as cnt
FROM
    Teacher
GROUP BY
    teacher_id