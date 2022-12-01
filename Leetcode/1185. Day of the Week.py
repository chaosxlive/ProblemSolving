# https://leetcode.com/problems/day-of-the-week/

import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][datetime.datetime(year, month, day).weekday()]
