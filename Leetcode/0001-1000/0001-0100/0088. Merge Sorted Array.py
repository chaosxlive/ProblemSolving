# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        ptr1, ptr2, ptrW = m - 1, n - 1, m + n - 1
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ptrW] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptrW] = nums2[ptr2]
                ptr2 -= 1

            ptrW -= 1
        
        while ptr2 >= 0:
            nums1[ptrW] = nums2[ptr2]
            ptr2 -= 1
            ptrW -= 1
            