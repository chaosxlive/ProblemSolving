# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = set()

        def convertTime(timePoint):
            return int(timePoint[:2]) * 60 + int(timePoint[-2:])

        for timePoint in timePoints:
            converted = convertTime(timePoint)
            if converted in times:
                return 0
            times.add(converted)
            times.add(converted + 1440)
        times = sorted(times)
        result = 1440
        for i in range(len(times) - 1):
            result = min(result, times[i + 1] - times[i])
        return result
