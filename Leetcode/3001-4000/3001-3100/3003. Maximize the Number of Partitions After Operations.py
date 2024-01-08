# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

from functools import lru_cache
import string


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:

        @lru_cache(None)
        def solve(first, i, isChanged):
            result = 0

            uniq = set([first])
            j = i + 1
            isDup = False
            while j < len(s):
                if s[j] not in uniq:
                    if len(uniq) == k:
                        break
                else:
                    isDup = True
                if len(uniq) == k - 1 and not isChanged and isDup and s[j] not in uniq:
                    result = max(result, solve(s[j], j, True) + 1)
                if len(uniq) == k and not isChanged:
                    for c in string.ascii_lowercase:
                        if c in uniq:
                            continue
                        result = max(result, solve(c, j, True) + 1)
                uniq.add(s[j])
                j += 1
            result = max(result,  solve(s[j], j, isChanged) + 1 if j < len(s) else 1)

            return result

        r = 0
        for c in string.ascii_lowercase:
            r = max(r, solve(c, 0, c != s[0]))
        return r
