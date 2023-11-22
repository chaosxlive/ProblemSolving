# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)
        median = nums[(left + right) // 2]
        smallers, equals, largers = [], [], []

        for num in nums:
            if num < median:
                smallers.append(num)
            elif num > median:
                largers.append(num)
            else:
                equals.append(num)

        if len(largers) >= k:
            return self.findKthLargest(largers, k)
        if len(equals) >= k - len(largers):
            return median
        return self.findKthLargest(smallers, k - len(largers) - len(equals))
