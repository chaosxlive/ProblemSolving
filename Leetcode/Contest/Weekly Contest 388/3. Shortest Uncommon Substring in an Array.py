from collections import defaultdict
from typing import List, Optional


class Solution:

    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        counter = defaultdict(int)
        for w in arr:
            for i in range(len(w)):
                for l in range(1, len(w) - i + 1):
                    counter[w[i:i + l]] += 1
        
        print(counter)

        INF = 'zzzzzzzzzzzzzzzzzzzz'
        result = [INF] * len(arr)

        for j, w in enumerate(arr):
            selfCnt = defaultdict(int)
            for i in range(len(w)):
                for l in range(1, len(w) - i + 1):
                    selfCnt[w[i:i + l]] += 1
            for i in range(len(w)):
                for l in range(1, len(w) - i + 1):
                    s = w[i:i + l]
                    if counter[s] == selfCnt[s]:
                        if len(s) < len(result[j]):
                            result[j] = s
                        elif len(s) == len(result[j]):
                            result[j] = min(result[j], s)

        return list(map(lambda x: '' if x == INF else x, result))


# print(Solution().shortestSubstrings(["vbb", "grg", "lexn", "oklqe", "yxav"]))
