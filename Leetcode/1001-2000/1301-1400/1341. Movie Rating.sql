-- https://leetcode.com/problems/movie-rating/

-- Create table If Not Exists Movies (movie_id int, title varchar(30))
-- Create table If Not Exists Users (user_id int, name varchar(30))
-- Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date)
-- Truncate table Movies
-- insert into Movies (movie_id, title) values ('1', 'Avengers')
-- insert into Movies (movie_id, title) values ('2', 'Frozen 2')
-- insert into Movies (movie_id, title) values ('3', 'Joker')
-- Truncate table Users
-- insert into Users (user_id, name) values ('1', 'Daniel')
-- insert into Users (user_id, name) values ('2', 'Monica')
-- insert into Users (user_id, name) values ('3', 'Maria')
-- insert into Users (user_id, name) values ('4', 'James')
-- Truncate table MovieRating
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '3', '2020-01-12')
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '2', '4', '2020-02-11')
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '3', '2', '2020-02-12')
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '4', '1', '2020-01-01')
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '1', '5', '2020-02-17')
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '2', '2', '2020-02-01')
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '3', '2', '2020-03-01')
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '1', '3', '2020-02-22')
-- insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '2', '4', '2020-02-25')

SELECT
    results
FROM
    (
        SELECT
            Users.name AS results
        FROM
            MovieRating
        LEFT JOIN
            Users
        ON
            MovieRating.user_id = Users.user_id
        GROUP BY
            MovieRating.user_id
        ORDER BY
            COUNT(MovieRating.movie_id) DESC,
            Users.name ASC
        LIMIT
            1
    ) AS T1

UNION ALL

SELECT
    T2.title AS results
FROM
    (
        SELECT
            M.movie_id,
            M.title,
            AVG(M.rating) AS avg_score
        FROM
            (
                SELECT
                    Movies.movie_id,
                    Movies.title,
                    MovieRating.rating,
                    MovieRating.created_at
                FROM
                    MovieRating
                LEFT JOIN
                    Movies
                ON
                    MovieRating.movie_id = Movies.movie_id
            ) AS M
        WHERE
            M.created_at >= '2020-02-01' AND M.created_at <= '2020-02-29'
        GROUP BY
            M.movie_id
        ORDER BY
            avg_score DESC,
            M.title ASC
        LIMIT
            1
    ) AS T2