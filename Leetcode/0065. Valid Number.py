# https://leetcode.com/problems/valid-number/

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match('^(([\+\-]?((\d+\.\d*)|(\.\d+)))|([\+\-]?\d+))([eE]([\+\-]?\d+))?$', s)