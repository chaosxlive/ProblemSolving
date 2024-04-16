from typing import List, Optional


class Solution:

    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            ss = str(num)
            m = max(map(int, ss))
            result += int(str(m) * len(ss))
        return result
