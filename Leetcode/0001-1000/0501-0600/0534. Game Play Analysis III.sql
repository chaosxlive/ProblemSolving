-- https://leetcode.com/problems/game-play-analysis-iii/
-- Write your MySQL query statement below

-- Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
-- Truncate table Activity
-- insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('1', '3', '2017-06-25', '1')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')

SELECT
    t1.player_id,
    t1.event_date,
    SUM(t2.games_played) AS games_played_so_far
FROM
    Activity AS t1,
    Activity AS t2
WHERE
    t1.player_id = t2.player_id AND
    t1.event_date >= t2.event_date
GROUP BY
    t1.player_id,
    t1.event_date
