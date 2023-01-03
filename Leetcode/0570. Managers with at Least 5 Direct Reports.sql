-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

-- Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int)
-- Truncate table Employee
-- insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', 'None')
-- insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101')
-- insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101')
-- insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101')
-- insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101')
-- insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101')

SELECT
    Employee.name AS name
FROM
    (
        SELECT
            managerId
        FROM
            Employee
        GROUP BY
            managerId
        HAVING
            COUNT(*) >= 5
    ) AS ManagerTable
LEFT JOIN
    Employee
ON
    Employee.id = ManagerTable.managerId
WHERE
    name IS NOT NULL