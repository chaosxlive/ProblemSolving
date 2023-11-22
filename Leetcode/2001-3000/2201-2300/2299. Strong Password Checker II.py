# https://leetcode.com/problems/strong-password-checker-ii/description/

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        flag = 0
        for i, c in enumerate(password):
            ordC = ord(c)
            if 97 <= ordC <= 122:
                flag |= 1
            elif 65 <= ordC <= 90:
                flag |= 2
            elif 48 <= ordC <= 57:
                flag |= 4
            elif c in "!@#$%^&*()-+":
                flag |= 8
            if i != 0 and password[i] == password[i - 1]:
                return False
        return flag == 15
