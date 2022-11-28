# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = defaultdict(int)
        for [win, lose] in matches:
            loses[win] += 0
            loses[lose] += 1
        result = [[], []]
        for lose in sorted(loses.keys()):
            loseCnt = loses[lose]
            if loseCnt == 0:
                result[0].append(lose)
            elif loseCnt == 1:
                result[1].append(lose)
        return [result[0], result[1]]
