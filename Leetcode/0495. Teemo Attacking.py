# https://leetcode.com/problems/teemo-attacking/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        effectEnd = 0
        for time in timeSeries:
            if time >= effectEnd:
                result += duration
                effectEnd = time + duration
            else:
                result += time + duration - effectEnd
                effectEnd = time + duration
        return result
