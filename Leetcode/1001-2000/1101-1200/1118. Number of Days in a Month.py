# https://leetcode.com/problems/number-of-days-in-a-month/

import datetime


class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if month != 2:
            return [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]
        return 29 if (datetime.datetime(year, 1, 1) + datetime.timedelta(days=59)).month == 2 else 28
