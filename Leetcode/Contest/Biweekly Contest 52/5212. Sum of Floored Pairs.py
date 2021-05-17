# https://leetcode.com/contest/biweekly-contest-52/problems/sum-of-floored-pairs/

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        freqNum = [0] * 100001
        prefreqNum = [0] * 100001
        for num in nums:
            freqNum[num] += 1
        for i in range(1, 100000):
            prefreqNum[i] = prefreqNum[i - 1] + freqNum[i]

        result = 0
        for i in range(1, 100000):
            for j in range(i, 100001, i):
                result += (j // i - 1) * (prefreqNum[j - 1] - prefreqNum[j - i - 1]) * freqNum[i]

        return result % 1000000007

# TLE