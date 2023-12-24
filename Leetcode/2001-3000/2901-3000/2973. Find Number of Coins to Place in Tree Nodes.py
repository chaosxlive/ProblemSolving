# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

from typing import List


class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        result = [0] * len(cost)

        childrens = [[] for _ in range(len(cost))]
        for p, c in edges:
            childrens[p].append(c)
            childrens[c].append(p)

        def dfs(node, parent):
            cnt = 1

            subs = []

            for child in childrens[node]:
                if child == parent:
                    continue

                childCnt, childSubs = dfs(child, node)

                cnt += childCnt
                subs = sorted(subs + childSubs)
                if len(subs) > 6:
                    subs = subs[:3] + subs[-3:]

            if cnt < 3:
                result[node] = 1
            else:
                res = -1
                ns = subs + [cost[node]]
                for i in range(len(ns) - 2):
                    for j in range(i + 1, len(ns) - 1):
                        for k in range(j + 1, len(ns)):
                            res = max(res, ns[i] * ns[j] * ns[k])
                if res < 0:
                    result[node] = 0
                else:
                    result[node] = res

            subs = sorted(subs + [cost[node]])
            if len(subs) > 6:
                subs = subs[:3] + subs[-3:]

            return cnt, subs

        dfs(0, -1)

        return result
