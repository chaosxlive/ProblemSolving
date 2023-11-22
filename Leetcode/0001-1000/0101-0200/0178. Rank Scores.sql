-- https://leetcode.com/problems/rank-scores/

-- Create table If Not Exists Scores (id int, score DECIMAL(3,2))
-- Truncate table Scores
-- insert into Scores (id, score) values ('1', '3.5')
-- insert into Scores (id, score) values ('2', '3.65')
-- insert into Scores (id, score) values ('3', '4.0')
-- insert into Scores (id, score) values ('4', '3.85')
-- insert into Scores (id, score) values ('5', '4.0')
-- insert into Scores (id, score) values ('6', '3.65')

WITH S AS (
    SELECT DISTINCT
        score
    FROM
        Scores
), Ranks AS (
    SELECT
        score,
        row_number() over(
            ORDER BY 
                score DESC
        ) AS row_num
    FROM
        S
)

SELECT
    Scores.score,
    Ranks.row_num AS `rank`
FROM
    Scores
LEFT JOIN
    Ranks
ON
    Scores.score = Ranks.score
ORDER BY
    `rank` ASC