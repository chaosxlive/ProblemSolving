# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        result = 2147483647
        isFound = False
        for i in range(startIndex, len(words)):  # Right
            if words[i] == target:
                isFound = True
                result = min(result, i - startIndex, len(words) - i + startIndex)
        for i in range(0, startIndex):  # Left
            if words[i] == target:
                isFound = True
                result = min(result, len(words) - startIndex + i, startIndex - i)
        return result if isFound else -1
