-- https://leetcode.com/problems/department-highest-salary/

-- Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int)
-- Create table If Not Exists Department (id int, name varchar(255))
-- Truncate table Employee
-- insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '70000', '1')
-- insert into Employee (id, name, salary, departmentId) values ('2', 'Jim', '90000', '1')
-- insert into Employee (id, name, salary, departmentId) values ('3', 'Henry', '80000', '2')
-- insert into Employee (id, name, salary, departmentId) values ('4', 'Sam', '60000', '2')
-- insert into Employee (id, name, salary, departmentId) values ('5', 'Max', '90000', '1')
-- Truncate table Department
-- insert into Department (id, name) values ('1', 'IT')
-- insert into Department (id, name) values ('2', 'Sales')

SELECT
    E.department_name AS Department,
    E.name AS Employee,
    E.salary AS Salary
FROM
    (
        SELECT
            Employee.name AS name,
            Employee.salary AS salary,
            Department.id AS department_id,
            Department.name AS department_name
        FROM
            Employee
        LEFT JOIN
            Department
        ON
            Employee.departmentId = Department.id
    ) AS E,
    (
        SELECT
            Employee.departmentId,
            MAX(Employee.salary) AS most_salary
        FROM
            Employee
        GROUP BY
            Employee.departmentId
    ) AS HighestSalary
WHERE
    E.department_id = HighestSalary.departmentId
    AND
    E.salary = HighestSalary.most_salary
