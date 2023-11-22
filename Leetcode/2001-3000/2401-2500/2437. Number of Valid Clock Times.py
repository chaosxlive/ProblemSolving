# https://leetcode.com/problems/number-of-valid-clock-times/

class Solution:
    def countTime(self, time: str) -> int:
        # Hours
        h = 0
        tH = time[:2]
        if tH == '??':
            h = 24
        elif tH[0] == '?':
            if tH[1] in '0123':
                h = 3
            else:
                h = 2
        elif tH[1] == '?':
            if tH[0] in '01':
                h = 10
            elif tH[0] == '2':
                h = 4
        elif 0 <= int(tH) < 24:
            h = 1
        # Minutes
        m = 0
        tM = time[-2:]
        if tM == '??':
            m = 60
        elif tM[0] == '?':
            m = 6
        elif tM[1] == '?':
            if 0 <= int(tM[0]) < 6:
                m = 10
        elif 0 <= int(tM) < 60:
            m = 1
        return h * m
