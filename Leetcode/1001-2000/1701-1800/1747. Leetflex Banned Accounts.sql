-- https://leetcode.com/problems/leetflex-banned-accounts/

-- Create table If Not Exists LogInfo (account_id int, ip_address int, login datetime, logout datetime)
-- Truncate table LogInfo
-- insert into LogInfo (account_id, ip_address, login, logout) values ('1', '1', '2021-02-01 09:00:00', '2021-02-01 09:30:00')
-- insert into LogInfo (account_id, ip_address, login, logout) values ('1', '2', '2021-02-01 08:00:00', '2021-02-01 11:30:00')
-- insert into LogInfo (account_id, ip_address, login, logout) values ('2', '6', '2021-02-01 20:30:00', '2021-02-01 22:00:00')
-- insert into LogInfo (account_id, ip_address, login, logout) values ('2', '7', '2021-02-02 20:30:00', '2021-02-02 22:00:00')
-- insert into LogInfo (account_id, ip_address, login, logout) values ('3', '9', '2021-02-01 16:00:00', '2021-02-01 16:59:59')
-- insert into LogInfo (account_id, ip_address, login, logout) values ('3', '13', '2021-02-01 17:00:00', '2021-02-01 17:59:59')
-- insert into LogInfo (account_id, ip_address, login, logout) values ('4', '10', '2021-02-01 16:00:00', '2021-02-01 17:00:00')
-- insert into LogInfo (account_id, ip_address, login, logout) values ('4', '11', '2021-02-01 17:00:00', '2021-02-01 17:59:59')

SELECT DISTINCT
    L1.account_id
FROM
    LogInfo AS L1,
    LogInfo AS L2
WHERE
    L1.account_id = L2.account_id
    AND
    L1.ip_address != L2.ip_address
    AND
    (
        L1.login BETWEEN L2.login AND L2.logout
        OR
        L1.logout BETWEEN L2.login AND L2.logout
    )