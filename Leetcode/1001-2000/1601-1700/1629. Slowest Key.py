# https://leetcode.com/problems/slowest-key/

from collections import defaultdict


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = defaultdict(lambda: 0)
        duration[keysPressed[0]] = releaseTimes[0]
        for index in range(1, len(releaseTimes)):
            duration[keysPressed[index]] = max(duration[keysPressed[index]], releaseTimes[index] - releaseTimes[index - 1])
        maxChar = keysPressed[0]
        maxDuration = releaseTimes[0]
        for k, d in duration.items():
            if d > maxDuration or (d == maxDuration and k > maxChar):
                maxDuration = d
                maxChar = k
        return maxChar