# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

import math

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        result = []
        for i in range(math.ceil((len(s) / k))):
            result.append(str(sum(map(int, list(s[i * k:(i + 1) * k])))))
        return self.digitSum(''.join(result), k)
