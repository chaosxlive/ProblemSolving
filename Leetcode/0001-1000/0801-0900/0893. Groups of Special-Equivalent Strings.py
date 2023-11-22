# https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:

        def count(s):
            result = [0] * 52
            for i in range(len(s)):
                if i % 2 == 0:
                    result[ord(s[i]) - 97 + 26] += 1
                else:
                    result[ord(s[i]) - 97] += 1
            return tuple(result)

        seen = set()

        for word in words:
            seen.add(count(word))

        return len(seen)
