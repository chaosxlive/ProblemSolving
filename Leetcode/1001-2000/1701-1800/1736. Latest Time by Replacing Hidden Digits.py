# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

class Solution:
    def maximumTime(self, time: str) -> str:
        result = [c for c in time]
        if time[0] == '?' and time[1] != '?':
            if int(time[1]) < 4:
                result[0] = '2'
            else:
                result[0] = '1'
        elif time[0] != '?' and time[1] == '?':
            if int(time[0]) == 2:
                result[1] = '3'
            else:
                result[1] = '9'
        elif time[0] == '?' and time[1] == '?':
            result[0] = '2'
            result[1] = '3'

        if time[3] == '?' and time[4] != '?':
            result[3] = '5'
        elif time[3] != '?' and time[4] == '?':
            result[4] = '9'
        elif time[3] == '?' and time[4] == '?':
            result[3] = '5'
            result[4] = '9'

        return ''.join(result)
