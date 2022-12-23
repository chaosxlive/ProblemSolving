-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

-- Create table If Not Exists ActorDirector (actor_id int, director_id int, timestamp int)
-- Truncate table ActorDirector
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '0')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '1')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '2')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '3')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '4')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '5')
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '6')

SELECT
    t.actor_id,
    t.director_id
FROM 
    (
        SELECT
            actor_id,
            director_id,
            COUNT(timestamp) AS cnt
        FROM 
            ActorDirector
        GROUP BY
            actor_id,
            director_id
    ) AS t
WHERE
    t.cnt >= 3