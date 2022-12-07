# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        prevIdx = -1
        idx = 0
        while idx < len(number):
            if number[idx] == digit:
                prevIdx = idx
                if idx != len(number) - 1 and number[idx] < number[idx + 1]:
                    return number[:idx] + number[idx + 1:]
            idx += 1
        return number[:prevIdx] + number[prevIdx + 1:]
