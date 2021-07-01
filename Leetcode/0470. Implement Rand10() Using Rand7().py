# https://leetcode.com/problems/implement-rand10-using-rand7/

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7() - 1) *  7 + rand7()
        if num > 40:
            return self.rand10()
        return 1 + (num % 10)
