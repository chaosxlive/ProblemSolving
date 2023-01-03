-- https://leetcode.com/problems/countries-you-can-safely-invest-in/

-- Create table If Not Exists Person (id int, name varchar(15), phone_number varchar(11))
-- Create table If Not Exists Country (name varchar(15), country_code varchar(3))
-- Create table If Not Exists Calls (caller_id int, callee_id int, duration int)
-- Truncate table Person
-- insert into Person (id, name, phone_number) values ('3', 'Jonathan', '051-1234567')
-- insert into Person (id, name, phone_number) values ('12', 'Elvis', '051-7654321')
-- insert into Person (id, name, phone_number) values ('1', 'Moncef', '212-1234567')
-- insert into Person (id, name, phone_number) values ('2', 'Maroua', '212-6523651')
-- insert into Person (id, name, phone_number) values ('7', 'Meir', '972-1234567')
-- insert into Person (id, name, phone_number) values ('9', 'Rachel', '972-0011100')
-- Truncate table Country
-- insert into Country (name, country_code) values ('Peru', '051')
-- insert into Country (name, country_code) values ('Israel', '972')
-- insert into Country (name, country_code) values ('Morocco', '212')
-- insert into Country (name, country_code) values ('Germany', '049')
-- insert into Country (name, country_code) values ('Ethiopia', '251')
-- Truncate table Calls
-- insert into Calls (caller_id, callee_id, duration) values ('1', '9', '33')
-- insert into Calls (caller_id, callee_id, duration) values ('2', '9', '4')
-- insert into Calls (caller_id, callee_id, duration) values ('1', '2', '59')
-- insert into Calls (caller_id, callee_id, duration) values ('3', '12', '102')
-- insert into Calls (caller_id, callee_id, duration) values ('3', '12', '330')
-- insert into Calls (caller_id, callee_id, duration) values ('12', '3', '5')
-- insert into Calls (caller_id, callee_id, duration) values ('7', '9', '13')
-- insert into Calls (caller_id, callee_id, duration) values ('7', '1', '3')
-- insert into Calls (caller_id, callee_id, duration) values ('9', '7', '1')
-- insert into Calls (caller_id, callee_id, duration) values ('1', '7', '7')

SELECT
    CountryCallAvg.country_name AS country
FROM
    (
        SELECT
            Country.name AS country_name,
            AVG(C.duration) AS duration
        FROM
            (
                SELECT
                    Calls.caller_id AS person_id,
                    Calls.duration
                FROM
                    Calls

                UNION

                SELECT
                    Calls.callee_id AS person_id,
                    Calls.duration
                FROM
                    Calls
            ) AS C
        LEFT JOIN
            (
                SELECT
                    Person.id AS person_id,
                    SUBSTRING(Person.phone_number, 1, 3) AS country_code
                FROM
                    Person
            ) AS P
        ON
            C.person_id = P.person_id
        LEFT JOIN
            Country
        ON
            P.country_code = Country.country_code
        GROUP BY
            Country.name
    ) AS CountryCallAvg,
    (
        SELECT
            AVG(Calls.duration) AS duration
        FROM
            Calls
    ) AS GlobalCallAvg
WHERE
    CountryCallAvg.duration > GlobalCallAvg.duration