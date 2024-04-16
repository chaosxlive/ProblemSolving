import math
from typing import List, Optional


class Solution:

    def minimumDeletions(self, word: str, k: int) -> int:
        cs = [0] * 26
        for c in word:
            cs[ord(c) - ord('a')] += 1
        result = math.inf
        q = sorted(set(cs))
        for target in q:
            if target == 0:
                continue
            temp = 0
            for c in cs:
                if c < target:
                    temp += c
                elif c > target + k:
                    temp += c - target - k
            result = min(result, temp)

        # for i in range(26):
        #     cnt = cs[i]
        #     if cnt == 0:
        #         continue
        #     # c = chr(i + ord('a'))
        #     temp = 0
        #     for j in range(26):
        #         J = cs[j]
        #         if J - cnt > k:
        #             temp += J - cnt - k
        #         elif cnt - J > k:
        #             temp += J
        #     result = min(result, temp)
        return result


# print(Solution().minimumDeletions("dabdcbdcdcd", 2))
