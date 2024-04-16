# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/


class Solution:

    def getSmallestString(self, s: str, k: int) -> str:
        res = list(s)
        ord_a = ord('a')
        for i, c in enumerate(s):
            ci = ord(c) - ord_a
            if ci >= 13:
                if 26 - ci <= k:
                    res[i] = 'a'
                    k -= 26 - ci
                else:
                    res[i] = chr(ord_a + ci - k)
                    break
            else:
                if ci <= k:
                    res[i] = 'a'
                    k -= ci
                else:
                    res[i] = chr(ord_a + ci - k)
                    break
        return ''.join(res)
