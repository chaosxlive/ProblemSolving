# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return ('#' + num).strip('0')[1:]
