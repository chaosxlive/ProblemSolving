# https://leetcode.com/problems/utf-8-validation/

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        while idx < len(data):
            if data[idx] & 128 == 0:
                idx += 1
            elif data[idx] & 224 == 192 and \
                idx + 1 < len(data) and \
                    data[idx + 1] & 192 == 128:
                idx += 2
            elif data[idx] & 240 == 224 and \
                idx + 2 < len(data) and \
                    data[idx + 1] & 192 == 128 and \
                    data[idx + 2] & 192 == 128:
                idx += 3
            elif data[idx] & 248 == 240 and \
                idx + 3 < len(data) and \
                    data[idx + 1] & 192 == 128 and \
                    data[idx + 2] & 192 == 128 and \
                    data[idx + 3] & 192 == 128:
                idx += 4
            else:
                return False
        return True
