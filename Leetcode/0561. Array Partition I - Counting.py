# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        count = [0] * 20002
        for num in nums:
            count[10000 + num] += 1
        isCounted = False
        result = 0
        for index in range(len(count)):
            if count[index] > 0:
                if isCounted:
                    count[index] -= 1
                if count[index] % 2 == 0:
                    isCounted = False
                else:
                    isCounted = True
            result += (count[index] + 1) // 2 * (index - 10000)
        return result
