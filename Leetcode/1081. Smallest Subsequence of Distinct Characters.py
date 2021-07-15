# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i

        result = []
        for i in range(len(s)):
            if s[i] not in result:
                while len(result) > 0 and result[-1] > s[i] and i < lastIndex[result[-1]]:
                    result.pop()
                result.append(s[i])
        return "".join(result)
