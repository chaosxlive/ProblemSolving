# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        x_rev = 0
        while temp != 0:
            x_rev = x_rev * 10 + temp % 10
            temp //= 10

        return x == x_rev