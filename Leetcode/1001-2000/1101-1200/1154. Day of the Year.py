# https://leetcode.com/problems/day-of-the-year/

import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        return (datetime.datetime(int(date[:4]), int(date[5:7]), int(date[-2:])) - datetime.datetime(int(date[:4]), 1, 1)).days + 1
