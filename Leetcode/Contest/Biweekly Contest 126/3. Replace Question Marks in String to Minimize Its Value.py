from collections import Counter
from functools import lru_cache
import math
import string
from typing import List, Optional


class Solution:

    def minimizeStringValue(self, s: str) -> str:
        cnts = [0] * 26
        for c in s:
            if c != '?':
                cnts[ord(c) - ord('a')] += 1
        candidates = []
        for c in s:
            if c == '?':
                MIN = math.inf
                MIN_C = ''
                for l in string.ascii_lowercase:
                    lc = cnts[ord(l) - ord('a')]
                    if lc < MIN:
                        MIN = lc
                        MIN_C = l
                cnts[ord(MIN_C) - ord('a')] += 1
                candidates.append(MIN_C)
        candidates.sort()

        ss = list(s)
        j = 0
        for i, c in enumerate(ss):
            if c == '?':
                ss[i] = candidates[j]
                j += 1
        return ''.join(ss)


# # print(Solution().minimizeStringValue("???"))
# print(Solution().minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
# print(Solution().minimizeStringValue("eq?umjlasi"))

# for i in range(qCnt):

#         @lru_cache(None)
#         def solve(i, cnts):
#             cnts = list(cnts)
#             if i == len(s):
#                 return 0, ''
#             c = s[i]
#             resultN = math.inf
#             resultS = ''
#             if c == '?':
#                 for nc in string.ascii_lowercase:
#                     nci = ord(nc) - ord('a')
#                     cnts[nci] += 1
#                     resN, resS = solve(i + 1, tuple(cnts))
#                     if resN + cnts[nci] < resultN:
#                         resultN = resN + cnts[nci]
#                         resultS = nc + resS
#                     cnts[nci] -= 1
#                 return resultN, resultS
#             else:
#                 ci = ord(c) - ord('a')
#                 cnts[ci] += 1
#                 resN, resS = solve(i + 1, tuple(cnts))
#                 return resN, c + resS

#         N, S = solve(0, tuple([0] * 26))
#         return S
