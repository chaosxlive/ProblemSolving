# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = {}
        for num in arr:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for num in target:
            if num not in count or count[num] == 0:
                return False
            else:
                count[num] -= 1

        return True
            
