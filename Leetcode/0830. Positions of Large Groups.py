# https://leetcode.com/problems/positions-of-large-groups/

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        prev = 0
        index = 1
        char = s[0]
        result = []
        while index < len(s):
            if s[index] != char:
                if index - prev >= 3:
                    result.append([prev, index - 1])
                prev = index
                char = s[index]
            index += 1
        if index - prev >= 3:
            result.append([prev, index - 1])
        return result
