# https://leetcode.com/problems/letter-case-permutation/

from functools import reduce


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        chars = []
        for c in s:
            if 'a' <= c <= 'z':
                chars.append([c, chr(ord(c) - 32)])
            elif 'A' <= c <= 'Z':
                chars.append([c, chr(ord(c) + 32)])
            else:
                chars.append([c])

        result = reduce(lambda arr1, arr2: {c1 + c2 for c1 in arr1 for c2 in arr2}, chars)
        return list(result)
