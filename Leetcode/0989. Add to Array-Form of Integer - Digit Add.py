# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        index, carry = len(num) - 1, 0
        result = []
        while index >= 0 and k > 0:
            temp = num[index] + k % 10 + carry
            carry = temp // 10
            result.append(temp % 10)
            index -= 1
            k //= 10
        while index >= 0:
            temp = num[index] + carry
            carry = temp // 10
            result.append(temp % 10)
            index -= 1
        while k > 0:
            temp = k % 10 + carry
            carry = temp // 10
            result.append(temp % 10)
            k //= 10
        if carry != 0:
            result.append(carry)
        return result[::-1]
