# https://leetcode.com/problems/number-of-days-between-two-dates/

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeapYear(date):
            return date % 4 == 0 and (date % 100 != 0 or date % 400 == 0)

        def dateFrom19710101(date):
            year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
            result = day - 1
            for y in range(1971, year):
                result += 366 if isLeapYear(y) else 365
            result += [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month]
            if month >= 3 and isLeapYear(year):
                result += 1
            return result

        return abs(dateFrom19710101(date1) - dateFrom19710101(date2))
