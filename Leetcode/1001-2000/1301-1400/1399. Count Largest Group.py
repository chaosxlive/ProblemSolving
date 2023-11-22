# https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = [0] * 40
        for i in range(1, n + 1):
            digitSum = 0
            while i > 0:
                digitSum += i % 10
                i //= 10
            count[digitSum] += 1
        
        result = 0
        maxCount = 0
        for num in count:
            if num > maxCount:
                maxCount = num
                result = 1
            elif num == maxCount:
                result += 1
        return result