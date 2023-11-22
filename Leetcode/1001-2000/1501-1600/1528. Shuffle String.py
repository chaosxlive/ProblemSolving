# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        index = 0
        while index < len(s):
            result[indices[index]] = s[index]
            index += 1
        
        return "".join(result)