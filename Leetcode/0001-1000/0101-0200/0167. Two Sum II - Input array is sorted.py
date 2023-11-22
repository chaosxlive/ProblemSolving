# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        needs = {}
        for i, number in enumerate(numbers):
            if number in needs:
                return [needs[number] + 1, i + 1]
            else:
                if target - number not in needs:
                    needs[target - number] = i
