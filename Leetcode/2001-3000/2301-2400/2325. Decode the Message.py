# https://leetcode.com/problems/decode-the-message/

from collections import defaultdict


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cMap = defaultdict(lambda: '')
        cIdx = 97
        cMap[' '] = ' '
        for k in key:
            if cMap[k] == '':
                cMap[k] = chr(cIdx)
                cIdx += 1
        result = []
        for c in message:
            result.append(cMap[c])
        return ''.join(result)
