# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/


class Solution:

    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:

        def timeToNum(t: str) -> int:
            h, m = t.split(':')
            return 60 * int(h) + int(m)

        timeIn = timeToNum(loginTime)
        timeOut = timeToNum(logoutTime)
        if timeIn > timeOut:
            timeOut += 1440

        return max((timeOut // 15) - ((timeIn + 14) // 15), 0)
