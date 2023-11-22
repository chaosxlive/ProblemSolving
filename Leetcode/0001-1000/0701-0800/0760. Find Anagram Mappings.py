# https://leetcode.com/problems/find-anagram-mappings/

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(map(lambda x: x[1], sorted(map(lambda x: (x[0][0], x[1][0]), zip(sorted([(i, n) for i, n in enumerate(nums1)], key=lambda x: x[1]), sorted([(i, n) for i, n in enumerate(nums2)], key=lambda x: x[1]))))))
