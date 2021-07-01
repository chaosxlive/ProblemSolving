# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        s = set()
        for n in nums:
            if n in s:
                result.append(n)
            s.add(n)
        for i in range(1, len(nums) + 1):
            if i not in s:
                result.append(i)
                return result
