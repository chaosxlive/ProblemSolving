# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        def count(nums: List[int]):
            result = nums[0]
            if len(nums) > 1:
                result += nums[1] * 2 if nums[0] == 10 else nums[1]
            for i in range(2, len(nums)):
                result += nums[i] * 2 if nums[i - 1] == 10 or nums[i - 2] == 10 else nums[i]
            return result

        r1 = count(player1)
        r2 = count(player2)
        return 1 if r1 > r2 else 2 if r2 > r1 else 0
