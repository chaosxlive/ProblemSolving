# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        index1, index2 = len(nums1) - 1, len(nums2) - 1
        distance = 0
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] <= nums2[index2]:
                if index2 - index1 > distance:
                    distance = index2 - index1
                index1 -= 1
            else:
                index2 -= 1
        return distance
