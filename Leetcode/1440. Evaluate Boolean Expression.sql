-- https://leetcode.com/problems/evaluate-boolean-expression/

-- Create Table If Not Exists Variables (name varchar(3), value int)
-- Create Table If Not Exists Expressions (left_operand varchar(3), operator ENUM('>', '<', '='), right_operand varchar(3))
-- Truncate table Variables
-- insert into Variables (name, value) values ('x', '66')
-- insert into Variables (name, value) values ('y', '77')
-- Truncate table Expressions
-- insert into Expressions (left_operand, operator, right_operand) values ('x', '>', 'y')
-- insert into Expressions (left_operand, operator, right_operand) values ('x', '<', 'y')
-- insert into Expressions (left_operand, operator, right_operand) values ('x', '=', 'y')
-- insert into Expressions (left_operand, operator, right_operand) values ('y', '>', 'x')
-- insert into Expressions (left_operand, operator, right_operand) values ('y', '<', 'x')
-- insert into Expressions (left_operand, operator, right_operand) values ('x', '=', 'x')

SELECT
    t.left_operand,
    t.operator,
    t.right_operand,
    CASE
        WHEN
            t.operator = '>'
        THEN
            IF(t.left_value > t.right_value, 'true', 'false')
        WHEN
            t.operator = '<'
        THEN
            IF(t.left_value < t.right_value, 'true', 'false')
        ELSE
            IF(t.left_value = t.right_value, 'true', 'false')
    END AS value
FROM
    (
        SELECT
            Expressions.left_operand,
            V1.value AS left_value,
            Expressions.operator,
            Expressions.right_operand,
            V2.value AS right_value
        FROM
            Expressions
        LEFT JOIN
            Variables AS V1
        ON
            Expressions.left_operand = V1.name
        LEFT JOIN
            Variables AS V2
        ON
            Expressions.right_operand = V2.name
    ) AS t