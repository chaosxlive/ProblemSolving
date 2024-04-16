# https://leetcode.com/problems/find-all-people-with-secret/

from collections import defaultdict
from typing import List


class UnionFind:

    def __init__(self) -> None:
        self.uf = {}

    def find(self, x):
        if x not in self.uf:
            self.uf[x] = x
        elif self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.uf[rx] = ry

    def hasSecret(self, x):
        return self.find(0) == self.find(x)


class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ufSecret = UnionFind()
        ufSecret.union(0, firstPerson)
        meetingsByTime = defaultdict(list)

        for a, b, t in meetings:
            meetingsByTime[t].append((a, b))

        for t in sorted(meetingsByTime.keys()):
            meetingList = meetingsByTime[t]
            ufTime = UnionFind()
            for a, b in meetingList:
                ufTime.union(a, b)
            isGroupHasSecret = defaultdict(bool)
            groups = defaultdict(list)
            for a in ufTime.uf.keys():
                groups[ufTime.find(a)].append(a)
                if ufSecret.find(a) == ufSecret.find(0):
                    isGroupHasSecret[ufTime.find(a)] = True
            for groupKey in groups.keys():
                if isGroupHasSecret[groupKey]:
                    group = groups[groupKey]
                    for i in range(1, len(group)):
                        ufSecret.union(group[0], group[i])

        return [0, *(i for i in range(1, n) if ufSecret.find(0) == ufSecret.find(i))]
