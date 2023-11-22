-- https://leetcode.com/problems/nth-highest-salary/

-- Create table If Not Exists Employee (Id int, Salary int)
-- Truncate table Employee
-- insert into Employee (id, salary) values ('1', '100')
-- insert into Employee (id, salary) values ('2', '200')
-- insert into Employee (id, salary) values ('3', '300')

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        -- Write your MySQL query statement below.
        SELECT
            CASE
                WHEN
                    t2.row_count < N
                THEN
                    NULL 
                ELSE
                    t1.salary
            END
        FROM (
            SELECT
                DISTINCT salary
            FROM
                Employee
            ORDER BY
                salary DESC
            LIMIT
                N
        ) AS t1, (
            SELECT
                COUNT(DISTINCT salary) AS row_count
            FROM
                Employee
            LIMIT
                N
        ) AS t2
        ORDER BY
            salary ASC
        LIMIT
            1
    );
END