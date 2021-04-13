# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1, right1 = 0, len(nums1) - 1
        left2, right2 = 0, len(nums2) - 1

        if len(nums1) == 0:
            index = (left2 + right2) // 2
            if (left2 + right2) % 2 == 0:
                return nums2[index]
            else:
                return (nums2[index] + nums2[index + 1]) / 2
        if len(nums2) == 0:
            index = (left1 + right1) // 2
            if (left1 + right1) % 2 == 0:
                return nums1[index]
            else:
                return (nums1[index] + nums1[index + 1]) / 2

        if nums1[right1] < nums2[left2]:
            if len(nums1) == len(nums2):
                return (nums1[right1] + nums2[left2]) / 2
            elif len(nums1) > len(nums2):
                diffLen = len(nums1) - len(nums2)
                if diffLen % 2 == 0:
                    return (nums1[right1 - diffLen // 2] + nums1[right1 - diffLen // 2 + 1]) / 2
                else:
                    return nums1[right1 - diffLen // 2]
            else:
                diffLen = len(nums2) - len(nums1)
                if diffLen % 2 == 0:
                    return (nums2[left2 + diffLen // 2] + nums2[left2 + diffLen // 2 - 1]) / 2
                else:
                    return nums2[left2 + diffLen // 2]
        elif nums1[left1] > nums2[right2]:
            if len(nums1) == len(nums2):
                return (nums1[left1] + nums2[right2]) / 2
            elif len(nums1) > len(nums2):
                diffLen = len(nums1) - len(nums2)
                if diffLen % 2 == 0:
                    return (nums1[left1 + diffLen // 2] + nums1[left1 + diffLen // 2 - 1]) / 2
                else:
                    return nums1[left1 + diffLen // 2]
            else:
                diffLen = len(nums2) - len(nums1)
                if diffLen % 2 == 0:
                    return (nums2[right2 - diffLen // 2] + nums2[right2 - diffLen // 2 + 1]) / 2
                else:
                    return nums2[right2 - diffLen // 2]
        else:
            while left1 < right1 and left2 < right2:
                if nums1[left1] <= nums2[left2]:
                    left1 += 1
                else:
                    left2 += 1
                if nums1[right1] >= nums2[right2]:
                    right1 -= 1
                else:
                    right2 -= 1

            if left1 == right1:
                while left2 < right2:
                    if nums2[left2] <= nums1[left1] <= nums2[right2]:
                        left2 += 1
                        right2 -= 1
                    elif nums1[left1] < nums2[left2]:
                        right2 -= 1
                        index = (left2 + right2) // 2
                        if (left2 + right2) % 2 == 0:
                            return nums2[index]
                        else:
                            return (nums2[index] + nums2[index + 1]) / 2
                    elif nums2[right2] < nums1[left1]:
                        left2 += 1
                        index = (left2 + right2) // 2
                        if (left2 + right2) % 2 == 0:
                            return nums2[index]
                        else:
                            return (nums2[index] + nums2[index + 1]) / 2
                if left2 == right2:
                    return (nums1[left1] + nums2[left2]) / 2
                else:
                    return nums1[left1]
            elif left2 == right2:
                while left1 < right1:
                    if nums1[left1] <= nums2[left2] <= nums1[right1]:
                        left1 += 1
                        right1 -= 1
                    elif nums2[left2] < nums1[left1]:
                        right1 -= 1
                        index = (left1 + right1) // 2
                        if (left1 + right1) % 2 == 0:
                            return nums1[index]
                        else:
                            return (nums1[index] + nums1[index + 1]) / 2
                    elif nums1[right1] < nums2[left2]:
                        left1 += 1
                        index = (left1 + right1) // 2
                        if (left1 + right1) % 2 == 0:
                            return nums1[index]
                        else:
                            return (nums1[index] + nums1[index + 1]) / 2
                if left1 == right1:
                    return (nums1[left1] + nums2[left2]) / 2
                else:
                    return nums2[left2]
            elif left1 > right1:
                index = (left2 + right2) // 2
                if (left2 + right2) % 2 == 0:
                    return nums2[index]
                else:
                    return (nums2[index] + nums2[index + 1]) / 2
            elif left2 > right2:
                index = (left1 + right1) // 2
                if (left1 + right1) % 2 == 0:
                    return nums1[index]
                else:
                    return (nums1[index] + nums1[index + 1]) / 2
