# https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        i12 = set1.intersection(set2)
        i13 = set1.intersection(set3)
        i23 = set2.intersection(set3)

        return list(i12.union(i13).union(i23))
