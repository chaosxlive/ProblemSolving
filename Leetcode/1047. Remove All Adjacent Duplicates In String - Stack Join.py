# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if len(stack) == 0 or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()

        return "".join(stack)