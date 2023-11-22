-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

-- Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int)
-- Truncate table Employees
-- insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', 'None', '43')
-- insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41')
-- insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36')
-- insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', 'None', '37')

SELECT
    Employees.employee_id,
    Employees.name,
    A.employee_cnt AS reports_count,
    A.avg_age AS average_age
FROM
    (
        SELECT
            reports_to AS manager_id,
            ROUND(AVG(age)) AS avg_age,
            COUNT(employee_id) AS employee_cnt
        FROM
            Employees
        WHERE
            reports_to IS NOT NULL
        GROUP BY
            reports_to
    ) AS A
LEFT JOIN
    Employees
ON
    A.manager_id = Employees.employee_id
ORDER BY
    Employees.employee_id