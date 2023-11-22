# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.rowSum = [0] * (len(nums) + 1)
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            self.rowSum[i + 1] = currentSum


    def sumRange(self, left: int, right: int) -> int:
        return self.rowSum[right + 1] - self.rowSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)