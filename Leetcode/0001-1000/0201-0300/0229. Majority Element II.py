# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        majority1 = majority2 = 0.5
        for num in nums:
            if num == majority1:
                count1 += 1
            elif num == majority2:
                count2 += 1
            else:
                if count1 != 0 and count2 != 0:
                    count1 -= 1
                    count2 -= 1
                elif count1 != 0 and count2 == 0:
                    majority2 = num
                    count2 = 1
                else:
                    majority1 = num
                    count1 = 1
            if count2 > count1:
                majority1, majority2 = majority2, majority1
                count1, count2 = count2, count1
        result = []
        if nums.count(majority1) > len(nums) // 3:
            result.append(majority1)
        if nums.count(majority2) > len(nums) // 3:
            result.append(majority2)
        return result
