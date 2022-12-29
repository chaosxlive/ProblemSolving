-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/

-- Create table If Not Exists Users (user_id int, user_name varchar(20))
-- Create table If Not Exists Register (contest_id int, user_id int)
-- Truncate table Users
-- insert into Users (user_id, user_name) values ('6', 'Alice')
-- insert into Users (user_id, user_name) values ('2', 'Bob')
-- insert into Users (user_id, user_name) values ('7', 'Alex')
-- Truncate table Register
-- insert into Register (contest_id, user_id) values ('215', '6')
-- insert into Register (contest_id, user_id) values ('209', '2')
-- insert into Register (contest_id, user_id) values ('208', '2')
-- insert into Register (contest_id, user_id) values ('210', '6')
-- insert into Register (contest_id, user_id) values ('208', '6')
-- insert into Register (contest_id, user_id) values ('209', '7')
-- insert into Register (contest_id, user_id) values ('209', '6')
-- insert into Register (contest_id, user_id) values ('215', '7')
-- insert into Register (contest_id, user_id) values ('208', '7')
-- insert into Register (contest_id, user_id) values ('210', '2')
-- insert into Register (contest_id, user_id) values ('207', '2')
-- insert into Register (contest_id, user_id) values ('210', '7')

WITH total_user_count AS (
    SELECT
        COUNT(user_id) AS total
    FROM
        Users
)

SELECT
    Register.contest_id,
    ROUND(COUNT(Register.user_id) / t.total * 100, 2) AS percentage
FROM
    Register
LEFT JOIN
    total_user_count AS t
ON
    1 = 1
GROUP BY
    contest_id
ORDER BY
    percentage DESC,
    contest_id ASC