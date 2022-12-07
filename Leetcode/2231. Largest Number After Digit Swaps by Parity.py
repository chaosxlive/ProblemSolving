# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution:
    def largestInteger(self, num: int) -> int:
        nums = list(str(num))
        parities = []
        odds = []
        evens = []
        for n in nums:
            if int(n) % 2 == 0:
                parities.append(0)
                evens.append(n)
            else:
                parities.append(1)
                odds.append(n)
        odds.sort()
        evens.sort()
        result = []
        for i in range(len(nums)):
            if parities[i] == 0:
                result.append(evens.pop())
            else:
                result.append(odds.pop())
        return int(''.join(result))
