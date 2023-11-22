# https://leetcode.com/problems/confusing-number/

class Solution:
    def confusingNumber(self, n: int) -> bool:
        num = str(n)
        left, right = 0, len(num) - 1
        isDifferent = False
        while left < len(num):
            if num[left] == '0':
                if num[right] != '0':
                    isDifferent = True
            elif num[left] == '1':
                if num[right] != '1':
                    isDifferent = True
            elif num[left] == '6':
                if num[right] != '9':
                    isDifferent = True
            elif num[left] == '8':
                if num[right] != '8':
                    isDifferent = True
            elif num[left] == '9':
                if num[right] != '6':
                    isDifferent = True
            else:
                return False
            left += 1
            right -= 1
        return isDifferent
