# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = [[] for i in range(501)]
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
        result = []
        for size in range(1, 500):
            if len(groups[size]) > 0:
                for s in range(0, len(groups[size]), size):
                    result.append(groups[size][s:s+size])
        return result
