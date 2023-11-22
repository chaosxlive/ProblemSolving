# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = {c: i for i, c in enumerate(s)}
        result = ['!']
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            while c < result[-1] and i < lastIndex[result[-1]]:
                seen.remove(result.pop())
            result.append(c)
            seen.add(c)
        return "".join(result[1:])
