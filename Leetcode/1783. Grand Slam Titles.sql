-- https://leetcode.com/problems/grand-slam-titles

-- Create table If Not Exists Players (player_id int, player_name varchar(20))
-- Create table If Not Exists Championships (year int, Wimbledon int, Fr_open int, US_open int, Au_open int)
-- Truncate table Players
-- insert into Players (player_id, player_name) values ('1', 'Nadal')
-- insert into Players (player_id, player_name) values ('2', 'Federer')
-- insert into Players (player_id, player_name) values ('3', 'Novak')
-- Truncate table Championships
-- insert into Championships (year, Wimbledon, Fr_open, US_open, Au_open) values ('2018', '1', '1', '1', '1')
-- insert into Championships (year, Wimbledon, Fr_open, US_open, Au_open) values ('2019', '1', '1', '2', '2')
-- insert into Championships (year, Wimbledon, Fr_open, US_open, Au_open) values ('2020', '2', '1', '2', '2')

SELECT
    Players.player_id,
    Players.player_name,
    SUM(WinCount.cnt) AS grand_slams_count
FROM
    (
        SELECT
            Wimbledon AS player_id,
            COUNT(year) AS cnt
        FROM
            Championships
        GROUP BY
            Wimbledon

        UNION ALL

        SELECT
            Fr_open AS player_id,
            COUNT(year) AS cnt
        FROM
            Championships
        GROUP BY
            Fr_open

        UNION ALL

        SELECT
            US_open AS player_id,
            COUNT(year) AS cnt
        FROM
            Championships
        GROUP BY
            US_open

        UNION ALL

        SELECT
            Au_open AS player_id,
            COUNT(year) AS cnt
        FROM
            Championships
        GROUP BY
            Au_open
    ) AS WinCount
LEFT JOIN
    Players
ON
    WinCount.player_id = Players.player_id
GROUP BY
    WinCount.player_id