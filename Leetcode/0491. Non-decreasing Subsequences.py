# https://leetcode.com/problems/non-decreasing-subsequences/

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        seqs = []
        for num in nums:
            newSeqs = seqs[:]
            for seq in seqs:
                if num >= seq[-1]:
                    newSeq = (*seq, num)
                    newSeqs.append(newSeq)
            newSeqs.append((num, ))
            seqs = newSeqs
        return list(map(list, filter(lambda s: len(s) > 1, set(seqs))))
