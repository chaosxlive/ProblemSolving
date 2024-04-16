from math import inf
from typing import Optional, List


# Rolling Hash
class RollingHash:

    def __init__(self, s):
        self.s = s
        self.length = len(s)
        self.mod1 = 10**9 + 7
        self.mod2 = 10**9 + 9
        self.p1 = 31
        self.p2 = 37
        self.hash1 = [0] * self.length
        self.hash2 = [0] * self.length

        h1 = h2 = 0
        p_pow1 = p_pow2 = 1
        for i in range(self.length):
            h1 = (h1 + (ord(s[i]) - ord('a') + 1) * p_pow1) % self.mod1
            h2 = (h2 + (ord(s[i]) - ord('a') + 1) * p_pow2) % self.mod2
            p_pow1 = (p_pow1 * self.p1) % self.mod1
            p_pow2 = (p_pow2 * self.p2) % self.mod2
            self.hash1[i] = h1
            self.hash2[i] = h2

    def prefix(self, index):
        return (self.hash1[index], self.hash2[index])

    def substr(self, l, r):
        # [l, r] is included
        if l == 0:
            return (self.hash1[r], self.hash2[r])
        temp1 = self.hash1[r] - self.hash1[l - 1]
        temp2 = self.hash2[r] - self.hash2[l - 1]
        temp1 += self.mod1 if temp1 < 0 else 0
        temp2 += self.mod2 if temp2 < 0 else 0
        temp1 = (temp1 * pow(pow(self.p1, l, self.mod1), self.mod1 - 2, self.mod1)) % self.mod1
        temp2 = (temp2 * pow(pow(self.p2, l, self.mod2), self.mod2 - 2, self.mod2)) % self.mod2
        return (temp1, temp2)

    def __eq__(self, other):
        return self.prefix(self.length - 1) == other.prefix(other.length - 1)


class PrefixTreeNode:

    def __init__(self, idx = -1) -> None:
        self.idx = idx
        self.children = {}


class Solution:

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        result = [0] * len(wordsQuery)

        ws = list(map(lambda x: x[::-1], wordsContainer))
        
        lbi = 0
        for i in range(1, len(ws)):
            if len(ws[i]) < len(ws[lbi]):
                lbi = i

        root = PrefixTreeNode(lbi)
        for i, w in enumerate(ws):
            ptr = root
            L = len(w)
            for c in w:
                if c not in ptr.children:
                    ptr.children[c] = PrefixTreeNode(i)
                ptr = ptr.children[c]
                if L < len(ws[ptr.idx]):
                    ptr.idx = i

        qs = list(map(lambda x: x[::-1], wordsQuery))

        for i, q in enumerate(qs):
            ptr = root
            for c in q:
                if c not in ptr.children:
                    break
                ptr = ptr.children[c]
            result[i] = ptr.idx

        return result
        # result = [0] * len(wordsQuery)
        # ws = list(map(lambda x: x[::-1], wordsContainer))
        # rs = [RollingHash(w) for w in ws]

        # lbi = 0
        # for i in range(1, len(ws)):
        #     if len(ws[i]) < len(ws[lbi]):
        #         lbi = i

        # for i, q in enumerate(map(lambda x: x[::-1], wordsQuery)):
        #     resIdx = -1
        #     resLCSL = 0
        #     resQL = inf
        #     qr = RollingHash(q)
        #     L = len(q)
        #     for j, r in enumerate(rs):
        #         maxL = min(L, len(r.s))
        #         for lcsL in reversed(range(max(1, resLCSL), maxL + 1)):
        #             if qr.prefix(lcsL - 1) == r.prefix(lcsL - 1):
        #                 if lcsL > resLCSL:
        #                     resIdx = j
        #                     resLCSL = lcsL
        #                     resQL = r.length
        #                 elif lcsL == resLCSL and r.length < resQL:
        #                     resIdx = j
        #                     resQL = r.length
        #     result[i] = lbi if resIdx == -1 else resIdx

        # return result
