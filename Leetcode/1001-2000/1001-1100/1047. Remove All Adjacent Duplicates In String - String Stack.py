# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ""
        for c in S:
            if len(stack) == 0 or c != stack[-1]:
                stack += c
            else:
                stack = stack[0:-1]

        return stack