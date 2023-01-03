-- https://leetcode.com/problems/find-cutoff-score-for-each-school/

-- Create table If Not Exists Schools (school_id int, capacity int)
-- Create table If Not Exists Exam (score int, student_count int)
-- Truncate table Schools
-- insert into Schools (school_id, capacity) values ('11', '151')
-- insert into Schools (school_id, capacity) values ('5', '48')
-- insert into Schools (school_id, capacity) values ('9', '9')
-- insert into Schools (school_id, capacity) values ('10', '99')
-- Truncate table Exam
-- insert into Exam (score, student_count) values ('975', '10')
-- insert into Exam (score, student_count) values ('966', '60')
-- insert into Exam (score, student_count) values ('844', '76')
-- insert into Exam (score, student_count) values ('749', '76')
-- insert into Exam (score, student_count) values ('744', '100')

SELECT
    Schools.school_id,
    IFNULL(S.score, -1) AS score
FROM
    Schools
LEFT JOIN
    (
        SELECT
            Schools.school_id,
            MIN(Exam.score) AS score
        FROM
            Schools,
            Exam
        WHERE
            Schools.capacity >= Exam.student_count
        GROUP BY
            Schools.school_id
    ) AS S
ON
    Schools.school_id = S.school_id