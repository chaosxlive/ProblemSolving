# https://leetcode.com/problems/repeated-dna-sequences/

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()
        for i in range(len(s) - 9):
            part = s[i:i + 10]
            if part in seen:
                result.add(part)
            seen.add(part)
        return list(result)
