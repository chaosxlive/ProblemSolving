# https://leetcode.com/problems/finding-3-digit-even-numbers/

from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        digitCounter = Counter(map(str, digits))
        for i in range(100, 1000, 2):
            n = str(i)
            tempCounter = Counter(n)
            valid = True
            for char, count in tempCounter.items():
                if digitCounter[char] < count:
                    valid = False
                    break
            if valid:
                result.append(i)
        return result
