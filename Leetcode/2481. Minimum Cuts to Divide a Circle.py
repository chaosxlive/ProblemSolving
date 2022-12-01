# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution:
    def numberOfCuts(self, n: int) -> int:
        return 0 if n == 1 else n if n % 2 == 1 else n // 2
