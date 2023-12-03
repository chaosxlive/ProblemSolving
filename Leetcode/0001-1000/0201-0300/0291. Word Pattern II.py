# https://leetcode.com/problems/word-pattern-ii/


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        mp = {}
        seen = set()

        def check(idxP, idxS):
            if idxP == len(pattern) and idxS == len(s):
                return True
            if idxP >= len(pattern) or idxS >= len(s):
                return False
            cp = pattern[idxP]
            if cp in mp:
                if s[idxS:idxS + len(mp[cp])] != mp[cp]:
                    return False
                return check(idxP + 1, idxS + len(mp[cp]))
            for l in range(1, len(s) - idxS + 1):
                w = s[idxS:idxS + l]
                if w in seen:
                    continue
                mp[cp] = w
                seen.add(w)
                if check(idxP + 1, idxS + l):
                    return True
                seen.remove(w)
                del mp[cp]
            return False

        return check(0, 0)
