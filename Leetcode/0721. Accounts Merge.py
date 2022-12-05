# https://leetcode.com/problems/accounts-merge/

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        result = []

        uf = {}
        holder = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry

        for account in accounts:
            if len(account) == 2:
                result.append(account)
            else:
                holder[account[1]] = account[0]
                for i in range(2, len(account)):
                    holder[account[i]] = account[0]
                    union(account[1], account[i])

        temp = defaultdict(list)
        for email in uf.keys():
            r = find(email)
            temp[r].append(email)
        for [key, emails] in temp.items():
            result.append([holder[key]] + sorted(emails))
        return result
