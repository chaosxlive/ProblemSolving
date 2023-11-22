# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt_list = [0] * 101
        for n in nums:
            cnt_list[n] += 1
        
        for n in range(1, 101):
            cnt_list[n] += cnt_list[n - 1]

        result = []
        for n in nums:
            if n == 0:
                result.append(0)
            else:
                result.append(cnt_list[n - 1])
        
        return result