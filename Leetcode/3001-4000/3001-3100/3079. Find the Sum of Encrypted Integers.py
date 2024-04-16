# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

from typing import List


class Solution:

    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            ss = str(num)
            m = max(map(int, ss))
            result += int(str(m) * len(ss))
        return result
