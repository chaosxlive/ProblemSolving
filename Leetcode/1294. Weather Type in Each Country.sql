-- https://leetcode.com/problems/weather-type-in-each-country/

-- Create table If Not Exists Countries (country_id int, country_name varchar(20))
-- Create table If Not Exists Weather (country_id int, weather_state int, day date)
-- Truncate table Countries
-- insert into Countries (country_id, country_name) values ('2', 'USA')
-- insert into Countries (country_id, country_name) values ('3', 'Australia')
-- insert into Countries (country_id, country_name) values ('7', 'Peru')
-- insert into Countries (country_id, country_name) values ('5', 'China')
-- insert into Countries (country_id, country_name) values ('8', 'Morocco')
-- insert into Countries (country_id, country_name) values ('9', 'Spain')
-- Truncate table Weather
-- insert into Weather (country_id, weather_state, day) values ('2', '15', '2019-11-01')
-- insert into Weather (country_id, weather_state, day) values ('2', '12', '2019-10-28')
-- insert into Weather (country_id, weather_state, day) values ('2', '12', '2019-10-27')
-- insert into Weather (country_id, weather_state, day) values ('3', '-2', '2019-11-10')
-- insert into Weather (country_id, weather_state, day) values ('3', '0', '2019-11-11')
-- insert into Weather (country_id, weather_state, day) values ('3', '3', '2019-11-12')
-- insert into Weather (country_id, weather_state, day) values ('5', '16', '2019-11-07')
-- insert into Weather (country_id, weather_state, day) values ('5', '18', '2019-11-09')
-- insert into Weather (country_id, weather_state, day) values ('5', '21', '2019-11-23')
-- insert into Weather (country_id, weather_state, day) values ('7', '25', '2019-11-28')
-- insert into Weather (country_id, weather_state, day) values ('7', '22', '2019-12-01')
-- insert into Weather (country_id, weather_state, day) values ('7', '20', '2019-12-02')
-- insert into Weather (country_id, weather_state, day) values ('8', '25', '2019-11-05')
-- insert into Weather (country_id, weather_state, day) values ('8', '27', '2019-11-15')
-- insert into Weather (country_id, weather_state, day) values ('8', '31', '2019-11-25')
-- insert into Weather (country_id, weather_state, day) values ('9', '7', '2019-10-23')
-- insert into Weather (country_id, weather_state, day) values ('9', '3', '2019-12-23')

SELECT
    Countries.country_name,
    CASE
        WHEN
            W.weather <= 15
        THEN
            'Cold'
        WHEN
            W.weather >= 25
        THEN
            'Hot'
        ELSE
            'Warm'
    END AS weather_type
FROM
    (
        SELECT
            Weather.country_id AS country_id,
            AVG(Weather.weather_state) AS weather
        FROM
            Weather
        WHERE
            Weather.day >= '2019-11-01'
            AND
            Weather.day <= '2019-11-30'
        GROUP BY
            Weather.country_id
    ) AS W
LEFT JOIN
    Countries
ON
    W.country_id = Countries.country_id