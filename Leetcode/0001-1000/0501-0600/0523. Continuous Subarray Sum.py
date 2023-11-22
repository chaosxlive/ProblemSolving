# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rest = saved = 0
        seen = set()
        for num in nums:
            rest = (rest + num) % k
            if rest in seen:
                return True
            seen.add(saved)
            saved = rest
        return False
        