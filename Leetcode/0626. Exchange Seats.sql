-- https://leetcode.com/problems/exchange-seats/
-- Write your MySQL query statement below

-- Create table If Not Exists seat(id int, student varchar(255))
-- Truncate table seat
-- insert into seat (id, student) values ('1', 'Abbot')
-- insert into seat (id, student) values ('2', 'Doris')
-- insert into seat (id, student) values ('3', 'Emerson')
-- insert into seat (id, student) values ('4', 'Green')
-- insert into seat (id, student) values ('5', 'Jeames')

SELECT
    (CASE
        WHEN id != total_rows AND MOD(id, 2) != 0 THEN id + 1
        WHEN id != total_rows AND MOD(id, 2) = 0 THEN id - 1
        ELSE (CASE
            WHEN MOD(total_rows, 2) = 0 THEN id - 1
            ELSE id
        END)
    END) AS id,
    student
FROM
    seat,
    (SELECT
        COUNT(*) AS total_rows
    FROM
        seat) AS seat_counts
ORDER BY 
    id ASC;

