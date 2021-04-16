# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if left == mid:
                print("same")
                break
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        print(left)
        print(right)
        
