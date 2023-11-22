# https://leetcode.com/problems/sort-vowels-in-a-string/


class Solution:
    def sortVowels(self, s: str) -> str:
        cs = list(s)
        vs = sorted([c for c in s if c in 'AEIOUaeiou'])
        vsi = 0
        for i, c in enumerate(cs):
            if c in 'AEIOUaeiou':
                cs[i] = vs[vsi]
                vsi += 1
        return ''.join(cs)
