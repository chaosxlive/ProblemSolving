# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        minDist = 100001
        dist = k
        for num in nums:
            if num == 1:
                if dist < k:
                    return False
                dist = 0
            else:
                dist += 1
        return True
