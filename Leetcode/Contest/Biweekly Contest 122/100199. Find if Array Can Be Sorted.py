from typing import List


class Solution:

    def canSortArray(self, nums: List[int]) -> bool:

        def countSetBits(n):
            result = 0
            while n > 0:
                if n & 1:
                    result += 1
                n >>= 1
            return result

        bs = list(map(countSetBits, nums))

        while True:
            isChanged = False
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    if bs[i] != bs[i - 1]:
                        return False
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    isChanged = True
                    break
            if not isChanged:
                return True
