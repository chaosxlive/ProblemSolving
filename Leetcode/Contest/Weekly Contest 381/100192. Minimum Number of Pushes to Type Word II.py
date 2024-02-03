from collections import Counter
from typing import List, Optional


class Solution:

    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        cnts = sorted(c.values(), reverse=True)
        result = 0
        for i, cnt in enumerate(cnts):
            if i < 8:
                result += cnt
            elif i < 16:
                result += cnt * 2
            elif i < 24:
                result += cnt * 3
            else:
                result += cnt * 4
        return result


# print(Solution().minimumPushes('aabbccddeeffgghhiiiiii'))
