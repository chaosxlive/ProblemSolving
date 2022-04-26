# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev = lambda x: int(str(x)[::-1])
        return rev(rev(num)) == num
