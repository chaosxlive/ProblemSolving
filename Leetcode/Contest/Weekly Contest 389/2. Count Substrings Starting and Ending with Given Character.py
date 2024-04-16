from typing import List, Optional


class Solution:

    def countSubstrings(self, s: str, c: str) -> int:
        result = 0
        cnt = 0
        for i in s:
            if i == c:
                cnt += 1
                result += cnt
        return result
