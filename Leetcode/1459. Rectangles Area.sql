-- https://leetcode.com/problems/rectangles-area/

-- Create table If Not Exists Points (id int, x_value int, y_value int)
-- Truncate table Points
-- insert into Points (id, x_value, y_value) values ('1', '2', '7')
-- insert into Points (id, x_value, y_value) values ('2', '4', '8')
-- insert into Points (id, x_value, y_value) values ('3', '2', '10')

SELECT
    P1.id AS p1,
    P2.id AS p2,
    ABS(P1.x_value - P2.x_value) * ABS(P1.y_value - P2.y_value) AS area
FROM
    Points AS P1,
    Points AS P2
WHERE
    P1.id < P2.id
    AND
    P1.x_value != P2.x_value
    AND
    P1.y_value != P2.y_value
ORDER BY
    area DESC,
    p1 ASC,
    p2 ASC
