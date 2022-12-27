-- https://leetcode.com/problems/number-of-calls-between-two-persons/

-- Create table If Not Exists Calls (from_id int, to_id int, duration int)
-- Truncate table Calls
-- insert into Calls (from_id, to_id, duration) values ('1', '2', '59')
-- insert into Calls (from_id, to_id, duration) values ('2', '1', '11')
-- insert into Calls (from_id, to_id, duration) values ('1', '3', '20')
-- insert into Calls (from_id, to_id, duration) values ('3', '4', '100')
-- insert into Calls (from_id, to_id, duration) values ('3', '4', '200')
-- insert into Calls (from_id, to_id, duration) values ('3', '4', '200')
-- insert into Calls (from_id, to_id, duration) values ('4', '3', '499')

SELECT
    CASE
        WHEN
            from_id < to_id
        THEN
            from_id
        ELSE
            to_id
    END AS person1,
    CASE
        WHEN
            from_id > to_id
        THEN
            from_id
        ELSE
            to_id
    END AS person2,
    COUNT(duration) AS call_count,
    SUM(duration) AS total_duration
FROM
    Calls
GROUP BY
    person1,
    person2
