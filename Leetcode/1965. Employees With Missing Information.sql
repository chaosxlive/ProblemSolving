-- https://leetcode.com/problems/employees-with-missing-information/
-- Write your MySQL query statement below

-- Create table If Not Exists Employees (employee_id int, name varchar(30))
-- Create table If Not Exists Salaries (employee_id int, salary int)
-- Truncate table Employees
-- insert into Employees (employee_id, name) values ('2', 'Crew')
-- insert into Employees (employee_id, name) values ('4', 'Haven')
-- insert into Employees (employee_id, name) values ('5', 'Kristian')
-- Truncate table Salaries
-- insert into Salaries (employee_id, salary) values ('5', '76071')
-- insert into Salaries (employee_id, salary) values ('1', '22517')
-- insert into Salaries (employee_id, salary) values ('4', '63539')

SELECT 
    t.employee_id
FROM 
    (
        SELECT
            Employees.employee_id
        FROM
            Employees
        LEFT JOIN
            Salaries
        ON
            Employees.employee_id = Salaries.employee_id
        WHERE
            Salaries.salary IS NULL

        UNION

        SELECT
            Salaries.employee_id
        FROM
            Salaries
        LEFT JOIN
            Employees
        ON
            Salaries.employee_id = Employees.employee_id
        WHERE
            Employees.name IS NULL
    ) AS t
ORDER BY
    t.employee_id