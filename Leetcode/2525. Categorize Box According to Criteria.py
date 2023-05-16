# https://leetcode.com/problems/categorize-box-according-to-criteria/

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        isBulky = volume >= 1000000000 or length >= 10000 or width >= 10000 or height >= 10000
        isHeavy = mass >= 100
        if isBulky and isHeavy:
            return 'Both'
        if isBulky and not isHeavy:
            return 'Bulky'
        if not isBulky and isHeavy:
            return 'Heavy'
        return 'Neither'
