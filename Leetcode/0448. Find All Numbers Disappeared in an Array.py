# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        occurrence = set()

        for num in nums:
            occurrence.add(num)

        result= []
        for i in range(1, len(nums) + 1):
            if i not in occurrence:
                result.append(i)
        return result
