# https://leetcode.com/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        stackNumber = []
        stackAlphabet = []
        for c in s:
            if '0' <= c <= '9':
                stackNumber.append(c)
            else:
                stackAlphabet.append(c)
        
        if abs(len(stackNumber) - len(stackAlphabet)) > 1: return ""

        result = []
        while len(stackNumber) > 0 and len(stackAlphabet) > 0:
            result.append(stackNumber.pop())
            result.append(stackAlphabet.pop())
        if len(stackNumber) > 0:
            result.append(stackNumber.pop())
        if len(stackAlphabet) > 0:
            result = [stackAlphabet.pop()] + result

        return "".join(result)
