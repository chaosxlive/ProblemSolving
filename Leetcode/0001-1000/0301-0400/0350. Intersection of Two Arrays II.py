# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        return Counter([num for num in range(1001) for time in range(min(count1[num], count2[num]))]).elements()
