-- https://leetcode.com/problems/highest-grade-for-each-student/

-- Create table If Not Exists Enrollments (student_id int, course_id int, grade int)
-- Truncate table Enrollments
-- insert into Enrollments (student_id, course_id, grade) values ('2', '2', '95')
-- insert into Enrollments (student_id, course_id, grade) values ('2', '3', '95')
-- insert into Enrollments (student_id, course_id, grade) values ('1', '1', '90')
-- insert into Enrollments (student_id, course_id, grade) values ('1', '2', '99')
-- insert into Enrollments (student_id, course_id, grade) values ('3', '1', '80')
-- insert into Enrollments (student_id, course_id, grade) values ('3', '2', '75')
-- insert into Enrollments (student_id, course_id, grade) values ('3', '3', '82')

SELECT
    student_id,
    MIN(course_id) AS course_id,
    grade
FROM
    Enrollments
WHERE
    (student_id, grade) IN (
        SELECT
            student_id,
            MAX(grade) AS max_grade
        FROM
            Enrollments
        GROUP BY
            student_id
    )
GROUP BY
    student_id,
    grade
ORDER BY
    student_id