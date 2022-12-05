-- https://leetcode.com/problems/find-the-team-size/
-- Write your MySQL query statement below

-- Create table If Not Exists Employee (employee_id int, team_id int)
-- Truncate table Employee
-- insert into Employee (employee_id, team_id) values ('1', '8')
-- insert into Employee (employee_id, team_id) values ('2', '8')
-- insert into Employee (employee_id, team_id) values ('3', '8')
-- insert into Employee (employee_id, team_id) values ('4', '7')
-- insert into Employee (employee_id, team_id) values ('5', '9')
-- insert into Employee (employee_id, team_id) values ('6', '9')

SELECT
    a.employee_id,
    b.cnt AS team_size
FROM
    Employee AS a,
    (
        SELECT 
            team_id,
            COUNT(team_id) AS cnt
        FROM
            Employee
        GROUP BY team_id
    ) AS b
WHERE a.team_id = b.team_id