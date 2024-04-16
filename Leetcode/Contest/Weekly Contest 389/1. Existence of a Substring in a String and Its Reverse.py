from typing import List, Optional


class Solution:

    def isSubstringPresent(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s.find(s[i] + s[i - 1]) != -1:
                return True
        return False
