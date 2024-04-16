from collections import defaultdict
from typing import List


class RollingHash:

    def __init__(self, s):
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


class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        seen = defaultdict(int)
        result = 0
        for word in words:
            wordHash = RollingHash(word)
            for i in range(len(word)):
                L = len(word)
                prefix = wordHash.substr(0, i)
                # print(f'{prefix=}')
                suffix = wordHash.substr(L - i - 1, L - 1)
                # print(f'{suffix=}')
                if prefix == suffix and prefix in seen:
                    result += seen[prefix]
            seen[prefix] += 1
        return result
