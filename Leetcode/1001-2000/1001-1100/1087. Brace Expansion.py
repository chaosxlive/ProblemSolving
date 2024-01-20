# https://leetcode.com/problems/brace-expansion/

from typing import List


class Solution:

    def expand(self, s: str) -> List[str]:
        result = ['']
        i = 0
        while True:
            j = s.find('{', i)
            if j == -1:
                result = [r + s[i:] for r in result]
                break
            else:
                k = s.find('}', j)
                subs = s[j + 1:k].split(',')
                p = s[i:j]
                result = [r + p + sub for r in result for sub in subs]
                i = k + 1
        result.sort()
        return result