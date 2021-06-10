# https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxNum, minNum = 0, 1000000001
        for num in nums:
            maxNum = max(maxNum, num)
            minNum = min(minNum, num)
        gap = (maxNum - minNum) // len(nums) + 1
        buckets = [[1000000001, 0] for b in range((maxNum - minNum) // gap + 1)]
        for num in nums:
            index = (num - minNum) // gap
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)
        result = 0
        prev = None
        for bucket in buckets:
            if bucket[0] != 1000000001:
                if prev != None:
                    result = max(bucket[0] - prev, result)
                result = max(bucket[1] - bucket[0], result)
                prev = bucket[1]
        return result
