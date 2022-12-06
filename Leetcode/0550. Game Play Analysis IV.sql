-- https://leetcode.com/problems/game-play-analysis-iv/
-- Write your MySQL query statement below

-- Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
-- Truncate table Activity
-- insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('1', '3', '2017-06-25', '1')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')

SELECT 
    ROUND(COUNT(t2.player_id) / COUNT(t1.player_id), 2) AS fraction
FROM
    (
        SELECT 
            player_id,
            MIN(event_date) AS first_login_date
        FROM
            Activity
        GROUP BY
            player_id
    ) AS t1 
LEFT JOIN 
    Activity t2
ON 
    t1.player_id = t2.player_id AND
    t1.first_login_date = t2.event_date - 1