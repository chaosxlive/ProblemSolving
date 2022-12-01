# https://leetcode.com/problems/count-number-of-texts/

class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        def calc(n):
            result = [1, 0, 0, 1]
            i = 1
            while i < n:
                result = [
                    result[3] % 1000000007,
                    result[0] % 1000000007,
                    result[1] % 1000000007,
                    (result[3] + result[0] + result[1]) % 1000000007
                ]
                i += 1
            return result[3]

        def calc79(n):
            result = [1, 0, 0, 0, 1]
            i = 1
            while i < n:
                result = [
                    result[4] % 1000000007,
                    result[0] % 1000000007,
                    result[1] % 1000000007,
                    result[2] % 1000000007,
                    (result[0] + result[1] + result[2] + result[4]) % 1000000007
                ]
                i += 1
            return result[4]

        left = right = 0
        result = 1
        while right < len(pressedKeys):
            if pressedKeys[left] != pressedKeys[right]:
                if pressedKeys[left] in ['7', '9']:
                    result *= calc79(right - left)
                else:
                    result *= calc(right - left)
                result %= 1000000007
                left = right
            right += 1
        if pressedKeys[left] in ['7', '9']:
            result *= calc79(right - left)
        else:
            result *= calc(right - left)
        result %= 1000000007
        return result
