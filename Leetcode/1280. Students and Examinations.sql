-- https://leetcode.com/problems/students-and-examinations/

-- Create table If Not Exists Students (student_id int, student_name varchar(20))
-- Create table If Not Exists Subjects (subject_name varchar(20))
-- Create table If Not Exists Examinations (student_id int, subject_name varchar(20))
-- Truncate table Students
-- insert into Students (student_id, student_name) values ('1', 'Alice')
-- insert into Students (student_id, student_name) values ('2', 'Bob')
-- insert into Students (student_id, student_name) values ('13', 'John')
-- insert into Students (student_id, student_name) values ('6', 'Alex')
-- Truncate table Subjects
-- insert into Subjects (subject_name) values ('Math')
-- insert into Subjects (subject_name) values ('Physics')
-- insert into Subjects (subject_name) values ('Programming')
-- Truncate table Examinations
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')
-- insert into Examinations (student_id, subject_name) values ('1', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('1', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('2', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('1', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')
-- insert into Examinations (student_id, subject_name) values ('13', 'Math')
-- insert into Examinations (student_id, subject_name) values ('13', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('13', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('2', 'Math')
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')

SELECT
    Students.student_id,
    Students.student_name,
    Subjects.subject_name,
    IF(t.cnt > 0, t.cnt, 0) AS attended_exams
FROM
    Students
CROSS JOIN
    Subjects
LEFT JOIN
    (
        SELECT
            student_id,
            subject_name,
            COUNT(*) AS cnt
        FROM
            Examinations
        GROUP BY
            student_id,
            subject_name
    ) AS t
ON
    t.student_id = Students.student_id
    AND
    t.subject_name = Subjects.subject_name
ORDER BY
    Students.student_id,
    Subjects.subject_name