# https://leetcode.com/problems/missing-ranges/

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        length = len(nums)
        if length == 0:
            return [f"{lower}"] if lower == upper else [f"{lower}->{upper}"]
        result = []
        nums = [lower - 1] + nums + [upper + 1]
        length += 2
        for i in range(length - 1):
            if nums[i + 1] != nums[i] + 1:
                if nums[i + 1] == nums[i] + 2:
                    result.append(f"{nums[i] + 1}")
                else:
                    result.append(f"{nums[i] + 1}->{nums[i + 1] - 1}")
        return result
