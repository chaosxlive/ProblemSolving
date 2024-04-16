# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    # Definition of commonSetBits API.
    def commonSetBits(num: int) -> int:
        return num


class Solution:

    def findNumber(self) -> int:
        result = 0
        for i in range(31):
            bit = 1 << i
            if commonSetBits(bit) > 0:
                result |= bit
        return result
