# https://leetcode.com/problems/validate-stack-sequences/

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx = 0
        stack = []
        for pushVal in pushed:
            if pushVal == popped[idx]:
                idx += 1
                while idx < len(popped) and len(stack) > 0 and stack[-1] == popped[idx]:
                    stack.pop()
                    idx += 1
            else:
                stack.append(pushVal)
        return len(stack) == 0
