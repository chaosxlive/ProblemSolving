# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        phoneKeys = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def getCombination(result, keyMap, digits, buffer, index):
            if index == len(digits):
                result.append("".join(buffer))
                return
            for c in keyMap[digits[index]]:
                buffer.append(c)
                getCombination(result, keyMap, digits, buffer, index + 1)
                buffer.pop()

        result = []
        getCombination(result, phoneKeys, digits, [], 0)
        return result
