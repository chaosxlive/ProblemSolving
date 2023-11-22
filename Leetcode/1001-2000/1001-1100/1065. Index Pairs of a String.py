# https://leetcode.com/problems/index-pairs-of-a-string/

import re


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        return sorted([[m.start(), m.start() + len(word) - 1] for word in words for m in re.finditer('(?={0})'.format(word), text)])
