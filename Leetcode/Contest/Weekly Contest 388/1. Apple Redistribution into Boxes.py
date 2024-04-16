from typing import List, Optional


class Solution:

    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        cnt = sum(apple)
        result = 0
        i = 0
        while cnt > 0:
            cnt -= capacity[i]
            result += 1
            i += 1
        return result
