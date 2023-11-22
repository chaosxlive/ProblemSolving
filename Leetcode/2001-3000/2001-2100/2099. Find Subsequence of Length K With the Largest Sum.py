# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return list(map(lambda x: x[1], sorted(sorted(enumerate(nums), key=lambda x: x[1], reverse=True)[:k], key=lambda x: x[0])))
