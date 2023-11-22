# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxList = set()
        for num in nums:
            if num not in maxList:
                if len(maxList) < 3:
                    maxList.add(num)
                else:
                    currentMin = min(maxList)
                    if num > currentMin:
                        maxList.remove(currentMin)
                        maxList.add(num)
        return max(maxList) if len(maxList) < 3 else min(maxList)