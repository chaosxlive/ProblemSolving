# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            temp = num
            isValid = True
            while temp > 0:
                div = temp % 10
                if div == 0 or num % div != 0:
                    isValid = False
                    break
                temp //= 10
            if isValid:
                result.append(num)
        return result