# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        idx = 0
        left = 1
        right = nums[idx]
        result = 0
        rest = k
        while rest > 0:
            cnt = right - left
            if cnt != 0:
                if cnt <= rest:
                    result += (left + (right - 1)) * cnt // 2
                else:
                    result += (left + (left + rest - 1)) * rest // 2
                rest = max(0, rest - cnt)
            idx += 1
            left = right + 1
            if idx >= len(nums):
                result += (left + (left + rest - 1)) * rest // 2
                break
            right = nums[idx]
        return result
