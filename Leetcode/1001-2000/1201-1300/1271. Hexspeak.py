# https://leetcode.com/problems/hexspeak/

import re


class Solution:
    def toHexspeak(self, num: str) -> str:
        result = str(hex(int(num)))[2:].upper().replace('1', 'I').replace('0', 'O')
        if re.match(r'^[ABCDEFIO]*$', result) == None:
            return 'ERROR'
        return result
