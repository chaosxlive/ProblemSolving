-- https://leetcode.com/problems/trips-and-users/

-- Create table If Not Exists Trips (id int, client_id int, driver_id int, city_id int, status ENUM('completed', 'cancelled_by_driver', 'cancelled_by_client'), request_at varchar(50))
-- Create table If Not Exists Users (users_id int, banned varchar(50), role ENUM('client', 'driver', 'partner'))
-- Truncate table Trips
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('1', '1', '10', '1', 'completed', '2013-10-01')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('3', '3', '12', '6', 'completed', '2013-10-01')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('4', '4', '13', '6', 'cancelled_by_client', '2013-10-01')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('5', '1', '10', '1', 'completed', '2013-10-02')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('6', '2', '11', '6', 'completed', '2013-10-02')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('7', '3', '12', '6', 'completed', '2013-10-02')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('8', '2', '12', '12', 'completed', '2013-10-03')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('9', '3', '10', '12', 'completed', '2013-10-03')
-- insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03')
-- Truncate table Users
-- insert into Users (users_id, banned, role) values ('1', 'No', 'client')
-- insert into Users (users_id, banned, role) values ('2', 'Yes', 'client')
-- insert into Users (users_id, banned, role) values ('3', 'No', 'client')
-- insert into Users (users_id, banned, role) values ('4', 'No', 'client')
-- insert into Users (users_id, banned, role) values ('10', 'No', 'driver')
-- insert into Users (users_id, banned, role) values ('11', 'No', 'driver')
-- insert into Users (users_id, banned, role) values ('12', 'No', 'driver')
-- insert into Users (users_id, banned, role) values ('13', 'No', 'driver')

WITH
    T AS (
        SELECT
            id,
            request_at AS Day,
            status
        FROM
            Trips
        WHERE
            Trips.client_id IN (
                SELECT
                    users_id AS client_id
                FROM
                    Users
                WHERE
                    banned = 'No'
            )
            AND
            Trips.driver_id IN (
                SELECT
                    users_id AS driver_id
                FROM
                    Users
                WHERE
                    banned = 'No'
            )
    ),
    TotalRequest AS (
        SELECT
            Day,
            COUNT(*) AS cnt
        FROM
            T
        GROUP BY
            Day 
    ),
    CanceledRequest AS (
        SELECT
            Day,
            COUNT(*) AS cnt
        FROM
            T
        WHERE
            status != 'completed'
        GROUP BY
            Day
    ),
    DayRange AS (
        SELECT
            request_at AS Day
        FROM
            Trips
        WHERE
            request_at >= '2013-10-01'
            AND
            request_at <= '2013-10-03'
            AND
            Trips.client_id IN (
                SELECT
                    users_id AS client_id
                FROM
                    Users
                WHERE
                    banned = 'No'
            )
            AND
            Trips.driver_id IN (
                SELECT
                    users_id AS driver_id
                FROM
                    Users
                WHERE
                    banned = 'No'
            )
        GROUP BY
            request_at
    )

SELECT
    DayRange.Day,
    CASE
        WHEN
            TotalRequest.cnt = 0
            OR
            TotalRequest.cnt IS NULL
            OR
            CanceledRequest.cnt = 0
            OR
            CanceledRequest.cnt IS NULL
        THEN
            0
        ELSE
            ROUND(CanceledRequest.cnt / TotalRequest.cnt, 2)
    END AS 'Cancellation Rate'
FROM
    DayRange
LEFT JOIN
    TotalRequest
ON
    DayRange.Day = TotalRequest.Day
LEFT JOIN
    CanceledRequest
ON
    DayRange.Day = CanceledRequest.Day