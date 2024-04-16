# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/


class Solution:

    def findLatestTime(self, s: str) -> str:
        h1, h2, _, m1, m2 = list(s)
        if h1 == '?' and h2 == '?':
            h1 = '1'
            h2 = '1'
        elif h1 == '?':
            if h2 == '0' or h2 == '1':
                h1 = '1'
            else:
                h1 = '0'
        elif h2 == '?':
            if h1 == '1':
                h2 = '1'
            else:
                h2 = '9'
        if m1 == '?' and m2 == '?':
            m1 = '5'
            m2 = '9'
        elif m1 == '?':
            m1 = '5'
        elif m2 == '?':
            m2 = '9'
        return ''.join([h1, h2, ':', m1, m2])
