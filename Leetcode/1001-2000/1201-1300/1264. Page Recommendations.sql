-- https://leetcode.com/problems/page-recommendations/

-- Create table If Not Exists Friendship (user1_id int, user2_id int)
-- Create table If Not Exists Likes (user_id int, page_id int)
-- Truncate table Friendship
-- insert into Friendship (user1_id, user2_id) values ('1', '2')
-- insert into Friendship (user1_id, user2_id) values ('1', '3')
-- insert into Friendship (user1_id, user2_id) values ('1', '4')
-- insert into Friendship (user1_id, user2_id) values ('2', '3')
-- insert into Friendship (user1_id, user2_id) values ('2', '4')
-- insert into Friendship (user1_id, user2_id) values ('2', '5')
-- insert into Friendship (user1_id, user2_id) values ('6', '1')
-- Truncate table Likes
-- insert into Likes (user_id, page_id) values ('1', '88')
-- insert into Likes (user_id, page_id) values ('2', '23')
-- insert into Likes (user_id, page_id) values ('3', '24')
-- insert into Likes (user_id, page_id) values ('4', '56')
-- insert into Likes (user_id, page_id) values ('5', '11')
-- insert into Likes (user_id, page_id) values ('6', '33')
-- insert into Likes (user_id, page_id) values ('2', '77')
-- insert into Likes (user_id, page_id) values ('3', '77')
-- insert into Likes (user_id, page_id) values ('6', '88')

SELECT DISTINCT
    page_id AS recommended_page 
FROM
    Likes
WHERE
    (user_id) in (
        SELECT DISTINCT
            user_id
        FROM
            (
                SELECT
                    user2_id AS user_id
                FROM
                    Friendship
                WHERE
                    user1_id = 1

                UNION

                SELECT
                    user1_id AS user_id
                FROM
                    Friendship
                WHERE
                    user2_id = 1
            ) AS t
    )

    AND

    (page_id) NOT IN (
        SELECT
            page_id
        FROM
            Likes
        WHERE
            user_id = 1
    )