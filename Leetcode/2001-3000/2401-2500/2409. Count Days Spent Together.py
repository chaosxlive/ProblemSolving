# https://leetcode.com/problems/count-days-spent-together/

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = ["", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        daysInMonth = ["", "31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
        result = 0
        for month in range(1, 13):
            for day in range(1, int(daysInMonth[month]) + 1):
                d = months[month] + "-" + ("0" + str(day))[-2:]
                if arriveAlice <= d <= leaveAlice and arriveBob <= d <= leaveBob:
                    result += 1
                    print(d)
        return result
