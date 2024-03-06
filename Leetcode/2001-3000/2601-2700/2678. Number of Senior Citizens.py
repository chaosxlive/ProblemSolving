# https://leetcode.com/problems/number-of-senior-citizens/

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len(list(filter(lambda s: int(s[11:13]) > 60, details)))
