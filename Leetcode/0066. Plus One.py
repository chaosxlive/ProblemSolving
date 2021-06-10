# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index, carry = len(digits) - 1, 1
        while index >= 0 and carry == 1:
            digits[index] += carry
            carry = digits[index] // 10
            digits[index] %= 10
            index -= 1
        if carry != 0:
            digits = [1] + digits
        return digits