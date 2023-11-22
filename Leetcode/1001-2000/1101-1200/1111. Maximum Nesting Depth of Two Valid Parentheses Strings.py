# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = [0] * len(seq)
        for i in range(len(seq)):
            if (seq[i - 1] == '(' and seq[i] == ')') or (seq[i - 1] == ')' and seq[i] == '('):
                result[i] = result[i - 1]
            else:
                result[i] = 1 if result[i - 1] == 0 else 0
        return result
