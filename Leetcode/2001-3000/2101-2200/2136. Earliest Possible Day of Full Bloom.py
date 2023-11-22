# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        result = 0
        currentTime = 0
        for i in sorted(range(len(plantTime)), key=lambda x: -growTime[x]):
            currentTime += plantTime[i]
            result = max(result, currentTime + growTime[i])
        return result
